## restaurant path
* greet	
  - utter_greet

* mood_great
  - utter_assist

* restaurant_search
  - utter_ask_location

* telling_location
  - utter_affirm_location
  - action_set_location
  - utter_ask_cuisine

* telling_cuisine
  - action_get_cuisine_show_restaurants
  - utter_did_that_help

* goodbye
  - utter_goodbye

## restaurant path 2

* restaurant_search
  - utter_ask_location

* telling_location
  - utter_affirm_location
  - action_set_location
  - utter_ask_cuisine

* telling_cuisine
  - action_get_cuisine_show_restaurants
  
  - utter_did_that_help

* goodbye
  - utter_goodbye

## restaurant path 3

* mood_great
  - utter_assist

* restaurant_search
  - utter_ask_location

* telling_location
  - utter_affirm_location
  - action_set_location
  - utter_ask_cuisine

* telling_cuisine
  - action_get_cuisine_show_restaurants
  
  - utter_did_that_help

* goodbye
  - utter_goodbye

## restaurant path 4
* greet 
  - utter_greet

* restaurant_search
  - utter_ask_location

* telling_location
  - utter_affirm_location
  - action_set_location
  - utter_ask_cuisine

* telling_cuisine
  - action_get_cuisine_show_restaurants
  
  - utter_did_that_help

* goodbye
  - utter_goodbye


## restaurant path 5
* greet
  - utter_greet

* mood_great
  - utter_assist


* telling_location_cuisine
  - utter_affirm_info
  - action_show_restaurants

* goodbye
  - utter_goodbye


## restaurant path 6
* greet
  - utter_greet

* telling_location_cuisine
  - utter_affirm_info
  - action_show_restaurants

* goodbye
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_assist

* goodbye
  - utter_goodbye

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  
  - utter_did_that_help


## sad path 2
* greet
  - utter_greet
* mood_unhappy
  
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye


