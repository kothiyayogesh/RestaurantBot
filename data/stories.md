## 1say goodbye
* goodbye
  - utter_goodbye

## 2greet_restaurantSearch_tellingLocation_tellingCuisine_tellingCategory

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location_name":"Mumbai"}
    - slot{"latitude":18.9401702881}
    - slot{"longitude":72.8348617554}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
    - utter_affirm_category
    - action_show_restaurants
    - utter_thanks

## 3greet_tellingLocationCuisine_tellingCategory

* greet
    - utter_greet
* mood_great
    - utter_assist
* telling_location_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - action_set_location
    - slot{"location_name":"Faridabad"}
    - slot{"latitude":28.3924694061}
    - slot{"longitude":77.3127593994}
    - utter_affirm_location
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
	- utter_affirm_category
    - action_show_restaurants
    - utter_thanks

## 4restaurantSearch_tellingLocation_tellingCuisine_tellingCategory

* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location_name":"Mumbai"}
    - slot{"latitude":18.940170288085938}
    - slot{"longitude":72.8348617553711}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
	- utter_affirm_category
    - action_show_restaurants
    - utter_thanks

## 5tellingLocationCuisine_tellingCategory

* telling_location_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_set_location
    - slot{"location_name":"Faridabad"}
    - slot{"latitude":28.3924694061}
    - slot{"longitude":77.3127593994}
    - utter_affirm_location
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
	- utter_affirm_category
    - action_show_restaurants
    - utter_thanks



## 6greet_restaurantSearch_denyLocation_tellingLocation_tellingCuisine_tellingCategory

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* deny
    - utter_location_denied
* telling_location
    - action_set_location
    - slot{"location_name":"Hyderabad"}
    - slot{"latitude":17.3659992218}
    - slot{"longitude":78.4759979248}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
    - utter_affirm_category
    - action_show_restaurants
    - utter_thanks

## 7restaurantSearch_denyLocation_tellingLocation_tellingCuisine_tellingCategory

* restaurant_search
    - utter_ask_location
* deny
    - utter_location_denied
* telling_location
    - action_set_location
    - slot{"location_name":"Mumbai"}
    - slot{"latitude":18.940170288085938}
    - slot{"longitude":72.8348617553711}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"south indian"}
    - slot{"cuisine":"south indian"}
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
    - utter_affirm_category
    - action_show_restaurants
    - utter_thanks

## 8greet_restaurantSearch_tellingLocation_denyCuisine_tellingCategory_showRestaurantsWithoutCuisine

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location_name":"Punjab"}
    - slot{"latitude":30.843242645263672}
    - slot{"longitude":75.41748046875}
    - utter_affirm_location
    - utter_ask_cuisine
* deny
    - utter_itsok
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
    - utter_affirm_category
    - action_restaurants_nocuisine_withCategory
    - utter_thanks

## 9greet_restaurantSearch_denyLocation_denyLocation_bye

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* deny
    - utter_location_denied
* deny
    - utter_tryAfter_sometime
    - utter_goodbye

## 10tellingLocation_tellingCuisine_tellingCategory

* telling_location
    - action_set_location
    - slot{"location_name":"Mumbai"}
    - slot{"latitude":18.940170288085938}
    - slot{"longitude":72.8348617553711}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
    - utter_affirm_category
    - action_show_restaurants
    - utter_thanks

## 11tellingCuisine_tellingLocation_tellingCategory_showRestaurants

* telling_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location_name":"Hyderabad"}
    - slot{"latitude":17.3659992218}
    - slot{"longitude":78.4759979248}
    - utter_affirm_location
    - utter_ask_category
* telling_category{"category":"cafes"}
    - slot{"category":"cafes"}
    - utter_affirm_category
    - action_show_restaurants
    - utter_thanks


## 12greet_restaurantSearch_tellingLocation_tellingCuisine_denyCategory

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location_name":"Mumbai"}
    - slot{"latitude":18.9401702881}
    - slot{"longitude":72.8348617554}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_ask_category
* deny
    - utter_itsok
    - action_show_restaurants
    - utter_thanks

## 13greet_tellingLocationCuisine_denyCategory

* greet
    - utter_greet
* mood_great
    - utter_assist
* telling_location_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - action_set_location
    - slot{"location_name":"Faridabad"}
    - slot{"latitude":28.3924694061}
    - slot{"longitude":77.3127593994}
    - utter_affirm_location
    - utter_ask_category
* deny
    - utter_itsok
    - action_show_restaurants
    - utter_thanks

## 14restaurantSearch_tellingLocation_tellingCuisine_denyCategory

* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location_name":"Mumbai"}
    - slot{"latitude":18.940170288085938}
    - slot{"longitude":72.8348617553711}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - utter_ask_category
* deny
    - utter_itsok
    - action_show_restaurants
    - utter_thanks

## 15tellingLocationCuisine_denyCategory

* telling_location_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_set_location
    - slot{"location_name":"Faridabad"}
    - slot{"latitude":28.3924694061}
    - slot{"longitude":77.3127593994}
    - utter_affirm_location
    - utter_ask_category
* deny
    - utter_itsok
    - action_show_restaurants
    - utter_thanks


## 16greet_restaurantSearch_denyLocation_tellingLocation_tellingCuisine_denyCategory

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* deny
    - utter_location_denied
* telling_location
    - action_set_location
    - slot{"location_name":"Hyderabad"}
    - slot{"latitude":17.3659992218}
    - slot{"longitude":78.4759979248}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_ask_category
* deny
    - utter_itsok
    - action_show_restaurants
    - utter_thanks



## 17restaurantSearch_denyLocation_tellingLocation_tellingCuisine_denyCategory

* restaurant_search
    - utter_ask_location
* deny
    - utter_location_denied
* telling_location
    - action_set_location
    - slot{"location_name":"Mumbai"}
    - slot{"latitude":18.940170288085938}
    - slot{"longitude":72.8348617553711}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"south indian"}
    - slot{"cuisine":"south indian"}
    - utter_ask_category
* deny
    - utter_itsok
    - action_show_restaurants
    - utter_thanks


## 18greet_restaurantSearch_tellingLocation_denyCuisine_denyCategory_showRestaurantsWithoutCuisine

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location_name":"Punjab"}
    - slot{"latitude":30.843242645263672}
    - slot{"longitude":75.41748046875}
    - utter_affirm_location
    - utter_ask_cuisine
* deny
    - utter_itsok
    - utter_ask_category
* deny
    - utter_itsok
    - action_restaurants_nocuisine_nocat
    - utter_thanks


## 19tellingLocation_tellingCuisine_denyCategory

* telling_location
    - action_set_location
    - slot{"location_name":"Mumbai"}
    - slot{"latitude":18.940170288085938}
    - slot{"longitude":72.8348617553711}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_ask_category
* deny
    - utter_itsok
    - action_show_restaurants
    - utter_thanks

