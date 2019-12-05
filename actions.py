from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.forms import FormAction
import requests
import ast

class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "tableBooking_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["num_people", "phone_no", "time"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "num_people": [
                self.from_entity(
                    entity="number", intent=["telling_numpeople"]
                ),
     
            ],
            "phone_no": [
                self.from_entity(entity="phone_no",intent=["telling_phoneno"]),
                
                
               
            ],
            "time": [
                self.from_entity(entity="time", intent=["telling_datetime"]),
                
            ],
        }



    # @staticmethod
    # def is_int(string: Text) -> bool:
    #     """Check if a string is an integer"""

    #     try:
    #         int(string)
    #         return True
    #     except ValueError:
    #         return False

  

    # def validate_num_people(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate num_people value."""

    #     if self.is_int(value) and int(value) > 0:
    #         return {"num_people": value}
    #     else:
    #         dispatcher.utter_template("utter_wrong_num_people", tracker)
    #         # validation failed, set slot to None
    #         return {"num_people": None}

    # def validate_outdoor_seating(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate outdoor_seating value."""

    #     if isinstance(value, str):
    #         if "out" in value:
    #             # convert "out..." to True
    #             return {"outdoor_seating": True}
    #         elif "in" in value:
    #             # convert "in..." to False
    #             return {"outdoor_seating": False}
    #         else:
    #             dispatcher.utter_template("utter_wrong_outdoor_seating", tracker)
    #             # validation failed, set slot to None
    #             return {"outdoor_seating": None}

    #     else:
    #         # affirm/deny was picked up as T/F
    #         return {"outdoor_seating": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_submit", tracker)
        return []


class Zomato:

    def __init__(self):
        self.api_key=""  ## Update Zomato API key here
        self.base_url = "https://developers.zomato.com/api/v2.1/"


    def getLocationInfo(self,location_name,latitude,longitude):
        
        #list storing entity_id,entity_type,city_id...
        location_info=[]

        queryString={"query":location_name,"lat":latitude,"lon":longitude}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}

        r = requests.get(self.base_url+"locations",params=queryString, headers=headers)

        data=r.json()

	
        if len(data['location_suggestions']) == 0:
            raise Exception('invalid_location')
            
        else:
            location_info.append(data["location_suggestions"][0]["city_id"])
            location_info.append(data["location_suggestions"][0]["entity_id"])
            location_info.append(data["location_suggestions"][0]["entity_type"])
            return location_info

    def get_cuisines(self, location_info,latitude,longitude):
        """
        Takes City ID as input.
        Returns dictionary of all cuisine names and their respective cuisine IDs in a given city.
        """


        headers = {'Accept': 'application/json', 'user-key': self.api_key}

        queryString={"lat":latitude,"lon":longitude,"city_id":location_info[0]}

        r = (requests.get(self.base_url +"cuisines",params=queryString,headers=headers).content).decode("utf-8")

        a = ast.literal_eval(r)
        all_cuisines_in_a_city = a['cuisines']

        cuisines={}

        for cuisine in all_cuisines_in_a_city:
            current_cuisine = cuisine['cuisine']
            cuisines[current_cuisine['cuisine_name'].lower()] = current_cuisine['cuisine_id']

        return cuisines


    def get_cuisine_id(self,cuisine_name,location_info,latitude,longitude):
        '''
        Takes cuisine name and city id as argument.
        Returns the cuisine id for that cuisine.
        '''
        cusines = self.get_cuisines(location_info,latitude,longitude)

        return cusines[cuisine_name.lower()]


    def get_all_restraunts(self,location_name,latitude,longitude,cuisine):
        '''
        Takes city name and cuisine name as arguments.
        Returns a list of 5 restaurants.
        '''
        # here we get city_id,entity_id,entity_type....
        location_info=self.getLocationInfo(location_name,latitude,longitude)
        cuisine_id=self.get_cuisine_id(cuisine,location_info,latitude,longitude)

        queryString={"lat":latitude,"lon":longitude,"entity_type":location_info[2], "entity_id":location_info[1], "cuisines":cuisine_id, "count":10}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r = requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_ofall_rest=r.json()["restaurants"]

        names_of_all_rest=[]
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])

        return names_of_all_rest

    def get_all_restraunts_catId(self,location_name,latitude,longitude,cuisine,cat_id):

        location_info=self.getLocationInfo(location_name,latitude,longitude)
        cuisine_id=self.get_cuisine_id(cuisine,location_info,latitude,longitude)

        queryString={"category":cat_id,"lat":latitude,"lon":longitude,"entity_type":location_info[2], "entity_id":location_info[1], "cuisines":cuisine_id, "count":10}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r = requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_ofall_rest=r.json()["restaurants"]

        names_of_all_rest=[]
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])

        return names_of_all_rest

    def get_all_restraunts_without_cuisne(self,location_name,latitude,longitude):

        '''
        Takes city name as arguments.
        Returns a list of 5 restaurants.
        '''

        location_info=self.getLocationInfo(location_name,latitude,longitude)
        
        queryString={"lat":latitude,"lon":longitude,"entity_type":location_info[2],"entity_id":location_info[1],"count":10}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r =requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_ofall_rest=r.json()["restaurants"]
        names_of_all_rest=[]
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])

        return names_of_all_rest


    def get_all_restraunts_without_cuisne_Catid(self,location_name,latitude,longitude,catid):
        location_info=self.getLocationInfo(location_name,latitude,longitude)
        
        queryString={"category":catid,"lat":latitude,"lon":longitude,"entity_type":location_info[2],"entity_id":location_info[1],"count":10}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r =requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_ofall_rest=r.json()["restaurants"]
        names_of_all_rest=[]
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])

        return names_of_all_rest



class LocationExtractor:
    
    def __init__(self):

        self.bing_baseurl="http://dev.virtualearth.net/REST/v1/Locations"
        self.bing_api_key="" ## Update Bing API key here

    def getLocationInfo(self, query, tracker):

        
        list_cities=[]
        queryString={"query":query,"key":self.bing_api_key}
        r = requests.get(self.bing_baseurl,params=queryString)
        data = r.json()
       
        if (r.status_code != 200) :

            dispatcher.utter_template('utter_ask_location', tracker)
            return []
        else:
            cordinates=data["resourceSets"][0]["resources"][0]["point"]["coordinates"]
            location_name=data["resourceSets"][0]["resources"][0]["name"].split(",")[0]

            return cordinates,location_name

class ActionSetLocation(Action):


    def name(self):

        return "action_set_location"

    def run(self, dispatcher,tracker,domain):

        user_input=tracker.latest_message['text']

        le = LocationExtractor()
        location_cordinates,location_name = le.getLocationInfo(str(user_input), tracker)

        return [SlotSet("location_name",location_name),SlotSet("latitude",location_cordinates[0]),SlotSet("longitude",location_cordinates[1])]

		
class GetRestaurantsWithoutCuisine(Action):

    def name(self):
        return "action_restaurants_nocuisine_nocat"


    def run(self, dispatcher,tracker,domain):
        
        location_name = tracker.get_slot('location_name')
        latitude=tracker.get_slot('latitude')
        longitude=tracker.get_slot('longitude')

        
        zom = Zomato()

        list_all_restaurants = zom.get_all_restraunts_without_cuisne(str(location_name),float(latitude),float(longitude))
        
        
        # dispatcher.utter_message("We found the top 10 rated restaurants for you !!!")

        # i=1
        # for res in list_all_restaurants:
        #     dispatcher.utter_message(str(i)+" ) "+res)
        #     i+=1

        temp_str = ""
        
        for r in range(0,len(list_all_restaurants)-1):
        	temp_str = temp_str + str(list_all_restaurants[r]) + ", "
        
        temp_str = temp_str + "and " + str(list_all_restaurants[-1])

        dispatcher.utter_message("We found " + str(temp_str) + " at " + location_name +" location. Have a great time :)")


        return []


class GetRestaurantsWithoutCuisineWithCategory(Action):

    def name(self):
        return "action_restaurants_nocuisine_withCategory"


    def run(self, dispatcher,tracker,domain):
        categories={"delivery":1,"dine-out":2,"nightlife":3,"catching-up":4,"takeaway":5,"cafes":6,"daily menus":7,"breakfast":8,"lunch":9,"dinner":10,"pubs & bars":11,"pocket friendly delivery":13,"clubs & lounges":14}

        location_name = tracker.get_slot('location_name')
        latitude=tracker.get_slot('latitude')
        longitude=tracker.get_slot('longitude')
        category=tracker.get_slot('category')

        
        zom = Zomato()

        cat_id=categories.get(category.lower())
        print(cat_id)

        list_all_restaurants=zom.get_all_restraunts_without_cuisne_Catid(str(location_name),float(latitude),float(longitude),cat_id)

            
        
        
        # dispatcher.utter_message("We found the top 10 rated restaurants for you !!!")

        # i=1
        # for res in list_all_restaurants:
        #     dispatcher.utter_message(str(i)+" ) "+res)
        #     i+=1

        temp_str = ""
        
        for r in range(0,len(list_all_restaurants)-1):
        	temp_str = temp_str + str(list_all_restaurants[r]) + ", "
        
        temp_str = temp_str + "and " + str(list_all_restaurants[-1])

        dispatcher.utter_message("We found " + str(temp_str) + " at " + location_name +" location. Have a great time :)")

        return []





class ActionShowRestaurants(Action):

    def name(self):
        return "action_show_restaurants"

    def run(self, dispatcher,tracker,domain):

        categories={"delivery":1,"dine-out":2,"nightlife":3,"catching-up":4,"takeaway":5,"cafes":6,"daily menus":7,"breakfast":8,"lunch":9,"dinner":10,"pubs & bars":11,"pocket friendly delivery":13,"clubs & lounges":14}
        zo = Zomato()
        le = LocationExtractor()
        user_input = tracker.latest_message['text']

        location_name = tracker.get_slot('location_name')
        latitude=tracker.get_slot('latitude')
        longitude=tracker.get_slot('longitude')
        category=tracker.get_slot('category')
        cuisine_type=tracker.get_slot('cuisine')
	
	#i don't understand why these two if's are used...
        if (not location_name) :
            location_name = le.getLocationInfo(str(user_input), tracker)

        if not location_name :
            ### Utter template
            dispatcher.utter_template('utter_ask_location', tracker)
        
        else:
            

            if category is None:
                print(category)
                list_all_restaurants=zo.get_all_restraunts(str(location_name),float(latitude),float(longitude),str(cuisine_type))


            else:
                cat_id=categories.get(category.lower())
                print(cat_id)

                list_all_restaurants=zo.get_all_restraunts_catId(str(location_name),float(latitude),float(longitude),str(cuisine_type),cat_id)

            

            # dispatcher.utter_message("We found the top 10 rated restaurants for you !!!")

            # i=1
            # for res in list_all_restaurants:
            # 	dispatcher.utter_message(str(i)+" ) "+res)
            # 	i+=1
        

        	for r in range(0,len(list_all_restaurants)-1):
            	temp_str = temp_str + str(list_all_restaurants[r]) + ", "    
        
            temp_str = temp_str + "and " + str(list_all_restaurants[-1])
        	dispatcher.utter_message("We found " + str(temp_str) + " of " + cuisine_type + " cuisine at "+ location_name +" location. Have a great time :)")

        return []
