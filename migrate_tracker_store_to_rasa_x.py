import argparse
import json
from typing import Text, Optional
import os
import logging

import questionary
from sqlalchemy import func
from sqlalchemy.orm import Session
from tqdm import tqdm

from rasa.cli.utils import print_error, print_success
from rasa.core.domain import Domain
from rasa.core.tracker_store import TrackerStore, InMemoryTrackerStore, SQLTrackerStore
from rasa.core.trackers import DialogueStateTracker
from rasa.core.utils import AvailableEndpoints

from rasax.community.database import ConversationStatistic
from rasax.community.services.event_service import EventService
import rasax.community.database.utils as db_utils
import rasax.community.sql_migrations as sql_migrations

logger = logging.getLogger(__name__)

"""This script migrates Rasa (Core) tracker stores to Rasa X.
What it can do:
- migrate any persistent tracker stores to a Rasa X compatible database.
- migrate any persistent tracker store to a SQL tracker store 
- migrate any persistent tracker store to a SQLite tracker store which is compatible 
  with the local version of Rasa X which can be installed from `pip`.
How to use it:
Run the script with `python migrate_tracker_store_to_rasa_x.py`.
The script will prompt you for all the required information.
"""


def _create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Script to migrate from a Rasa Core tracker store to Rasa X.",
    )
    parser.add_argument(
        "--max-trackers",
        type=int,
        default=None,
        help="Number of trackers to migrate. By default this migrates all trackers.",
    )

    return parser


def _get_path_to_old_endpoints_config() -> Optional[Text]:
    return questionary.text(
        "Please provide the path to your endpoints "
        "configuration which "
        "specifies the credentials for your old tracker store:",
        default="endpoints.yml",
    ).ask()


def _get_is_local() -> bool:
    return questionary.confirm(
        "Do you want to migrate to the local version of Rasa X?"
    ).ask()


def _get_path_to_new_endpoints_config() -> Optional[Text]:
    return questionary.text(
        "Please provide the path to your endpoints "
        "configuration which "
        "specifies the credentials for your new tracker store:",
        default="new_endpoints.yml",
    ).ask()


def _migrate_tracker_store_to_rasa_x(
    old_endpoints_file: Text,
    new_endpoints_file: Optional[Text],
    is_local: bool,
    max_number_of_trackers: Optional[int],
) -> None:
    old_tracker_store = _get_tracker_store_from_endpoints_config(old_endpoints_file)

    reuse_old_tracker_store = old_endpoints_file == new_endpoints_file
    if reuse_old_tracker_store:
        print(
            "Old and new endpoints file is the same. "
            "I will skip migrating the tracker store and only migrate the events to Rasa X."
        )

    # Initialize Rasa X tracker store in any case
    rasa_x_tracker_store = _get_rasa_x_tracker_store(new_endpoints_file)

    # Disable warnings regarding not existing slots
    logging.getLogger("rasa.core.trackers").setLevel(logging.CRITICAL)

    if not reuse_old_tracker_store and rasa_x_tracker_store.keys():
        should_migrate = questionary.confirm(
            "Found existing trackers in your Rasa X tracker store. Do you "
            "still want to migrate the new trackers?"
        )

        if not should_migrate:
            exit(1)

    db_session = db_utils.get_database_session(is_local)
    sql_migrations.run_migrations(db_session)
    event_service = EventService(db_session)

    sender_ids = old_tracker_store.keys()

    if max_number_of_trackers:
        sender_ids = sender_ids[:max_number_of_trackers]

    print_success("Start migrating {} trackers.".format(len(sender_ids)))

    nr_skipped_trackers = 0

    for sender_id in tqdm(sender_ids):
        tracker = old_tracker_store.retrieve(sender_id)

        if not reuse_old_tracker_store:
            if rasa_x_tracker_store.retrieve(sender_id):
                nr_skipped_trackers += 1
                logging.debug(
                    "Tracker for sender '{}' already exists. Skipping the "
                    "migration for it.".format(sender_id)
                )

            else:
                # Migrate tracker store to new tracker store format
                rasa_x_tracker_store.save(tracker)

        # Replay events of tracker
        _replay_tracker_events(tracker, event_service)

    # Set latest event id so that the `SQLiteEventConsumer` only consumes not already
    # migrated events
    set_latest_event_id(db_session, rasa_x_tracker_store)

    print_success(
        "Finished migrating trackers ({} were skipped since they were "
        "already migrated).".format(nr_skipped_trackers)
    )


def _get_tracker_store_from_endpoints_config(endpoints_file: Text) -> TrackerStore:
    if (
        not endpoints_file
        or not os.path.isfile(endpoints_file)
        or not os.path.exists(endpoints_file)
    ):
        print_error(
            "File '{}' was not found. Please specify a valid file with "
            "'--endpoints <file>'.".format(endpoints_file)
        )
        exit(1)

    endpoints = AvailableEndpoints.read_endpoints(endpoints_file)

    tracker_store = TrackerStore.find_tracker_store(
        Domain.empty(), endpoints.tracker_store
    )

    if not tracker_store or isinstance(tracker_store, InMemoryTrackerStore):
        print_error(
            "No valid tracker store config given. Please provide a valid "
            "tracker store configuration as it is described here: "
            "https://rasa.com/docs/core/0.14.4/tracker_stores/"
        )
        exit(1)

    return tracker_store


def _get_rasa_x_tracker_store(endpoints_file: Optional[Text]) -> TrackerStore:
    if endpoints_file and os.path.exists(endpoints_file):
        return _get_tracker_store_from_endpoints_config(endpoints_file)
    else:
        return SQLTrackerStore(Domain.empty(), db="tracker.db")


def _replay_tracker_events(
    tracker: DialogueStateTracker, event_service: EventService
) -> None:
    """Migrates the `events`, `logs`, `sessions` collections."""

    for event in tracker.events:
        event_dict = event.as_dict()
        # add sender id to event
        event_dict["sender_id"] = str(tracker.sender_id)
        stringified_event = json.dumps(event_dict)
        # Update events + most of conversations metadata
        _ = event_service.save_event(stringified_event)


def set_latest_event_id(
    db_session: Session, rasa_x_tracker_store: SQLTrackerStore
) -> None:
    (max_event_id,) = rasa_x_tracker_store.session.query(
        func.max(SQLTrackerStore.SQLEvent.id)
    ).first()

    existing = db_session.query(ConversationStatistic).first()

    if existing:
        existing.latest_event_id = max_event_id
        db_session.commit()

        logging.debug("Set max event id to '{}'.".format(max_event_id))


if __name__ == "__main__":
    parser = _create_argument_parser()
    args = parser.parse_args()

    print_success(
        "Welcome to Rasa X 🚀 \n\nThis script will migrate your old tracker "
        "store to the new SQL based Rasa X tracker store."
    )
    print_success("Let's start!\n")

    path_to_old_endpoints_file = _get_path_to_old_endpoints_config()
    is_local = _get_is_local()
    path_to_new_endpoints_file = None
    if not is_local:
        path_to_new_endpoints_file = _get_path_to_new_endpoints_config()
        _ = questionary.confirm(
            "You decided to migrate to a dockerized version of Rasa X. "
            "To migrate to a Rasa X SQL database, you have provide the database "
            "credentials. "
            "You can do so by setting the environment variables "
            "'DB_DRIVER' (e.g. 'postgresql'), "
            "'DB_USER' (e.g. 'admin'), "
            "'DB_PASSWORD' (e.g. 'password'), "
            "'DB_HOST' (e.g. 'localhost'), "
            "'DB_PORT' (e.g. '5432'), "
            "'DB_DATABASE' (e.g. 'rasa'). Have you done that?"
        )

    _migrate_tracker_store_to_rasa_x(
        path_to_old_endpoints_file,
        path_to_new_endpoints_file,
        is_local,
        args.max_trackers,
    )