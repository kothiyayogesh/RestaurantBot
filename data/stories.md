## say goodbye
* goodbye
  - utter_goodbye

## Restaurant path 1

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - utter_affirm_location
    - action_set_location
    - slot{"location":"Hyderabad"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_get_cuisine_show_restaurants
    - utter_did_that_help
* affirm
    - utter_goodbye
* goodbye

## Restaurant path 2

* greet
    - utter_greet
* mood_great
    - utter_assist
* telling_location_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - action_show_restaurants
    - utter_did_that_help
* goodbye

## Restaurant path 3

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - utter_affirm_location
    - action_set_location
    - slot{"location":"Bangalore"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"mexican"}
    - slot{"cuisine":"mexican"}
    - action_get_cuisine_show_restaurants
    - utter_did_that_help
* goodbye

## Restaurant path 4

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - utter_affirm_location
    - action_set_location
    - slot{"location":"Mumbai"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - action_get_cuisine_show_restaurants
    - utter_did_that_help
* affirm
    - utter_goodbye
* goodbye

## Restaurant path 5

* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location":"Mumbai"}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - action_get_cuisine_show_restaurants
    - utter_did_that_help
* affirm
    - utter_goodbye

## Restaurant path 6

* greet
    - utter_greet
* mood_great
    - utter_assist
* telling_location_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - utter_affirm_info
    - action_show_restaurants
    - utter_did_that_help
* affirm
    - utter_goodbye

## Restaurant path 6

* telling_location_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_affirm_info
    - action_show_restaurants
    - utter_did_that_help
* affirm
    - utter_goodbye
