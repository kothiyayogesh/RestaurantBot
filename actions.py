from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted

import requests
import ast


class Zomato:

    def __init__(self):
        self.api_key="797e936d8ac687c396be2fec2a356217"
        self.base_url = "https://developers.zomato.com/api/v2.1/"


    def getLocationInfo(self,location):
        '''
        Takes city name as argument.
        Returns the corressponding city_id.
        '''
        #list storing latitude,longitude...
        location_info=[]
        print(location)
        queryString={"query":location}
        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r = requests.get(self.base_url+"locations",params=queryString, headers=headers)
        data=r.json()
       # print(data)

        if len(data['location_suggestions']) == 0:
            raise Exception('invalid_location')
            
        else:
            location_info.append(data["location_suggestions"][0]["latitude"])
            location_info.append(data["location_suggestions"][0]["longitude"])
            location_info.append(data["location_suggestions"][0]["entity_id"])
            location_info.append(data["location_suggestions"][0]["entity_type"])
            return location_info

    def get_cuisines(self, location_info):
        """
        Takes City ID as input.
        Returns dictionary of all cuisine names and their respective cuisine IDs in a given city.
        """

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        queryString={"lat":location_info[0],"lon":location_info[1]}
        r = (requests.get(self.base_url +"cuisines",params=queryString,headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)
        all_cuisines_in_a_city=a['cuisines']


        cuisines={}

        for cuisine in all_cuisines_in_a_city:
            current_cuisine=cuisine['cuisine']
            cuisines[current_cuisine['cuisine_name'].lower()]=current_cuisine['cuisine_id']


        return cuisines


    def get_cuisine_id(self,cuisine_name,location_info):
        '''
        Takes cuisine name and city id as argument.
        Returns the cuisine id for that cuisine.
        '''
        cusines=self.get_cuisines(location_info)
        return cusines[cuisine_name.lower()]


    def get_all_restraunts(self,location,cuisine):
        '''
        Takes city name and cuisine name as arguments.
        Returns a list of 20 restaurants.
        '''
        location_info=self.getLocationInfo(location)
        cuisine_id=self.get_cuisine_id(cuisine,location_info)

        print(location_info)
        print(cuisine_id)

        queryString={"entity_type":location_info[3],"entity_id":location_info[2],"cuisines":cuisine_id,"count":5}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r =requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_ofall_rest=r.json()["restaurants"]
        names_of_all_rest=[]
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])


        return names_of_all_rest

    def get_all_restraunts_without_cuisne(self,location):
        '''
        Takes city name and cuisine name as arguments.
        Returns a list of 20 restaurants.
        '''
        location_info=self.getLocationInfo(location)
        
        queryString={"entity_type":location_info[3],"entity_id":location_info[2],"count":5}

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
       self.bing_api_key="Aiw0X2IXCnSru_O00Rl8c8v6nULH-Z7r1HdFOVW3MQZEJoq6U2kQ_SVabSQui1GU"

    def getLocationInfo(self,query):
        
        list_cities=[]
        queryString={"query":query,"key":self.bing_api_key}
        r = requests.get(self.bing_baseurl,params=queryString)
        data=r.json()
        print(data)
        return data["resourceSets"][0]["resources"][0]["point"]["coordinates"],data["resourceSets"][0]["resources"][0]["name"]
        
        #for x in all_locations["annotations"]:
        #    list_cities.append(x["label"])
            
        #return list_cities

class ActionSetLocation(Action):


    def name(self):
        return "action_set_location"

    def run(self, dispatcher,tracker,domain):
        user_input=tracker.latest_message['text']
        le=LocationExtractor()
        location_name=le.getLocationInfo(str(user_input))
        print(location_name)
        
        return [SlotSet("location",location_name[0])]


class ActionSetCuisine_showRestaurants(Action):
    def name(self):
        return "action_get_cuisine_show_restaurants"


    def run(self, dispatcher,tracker,domain):
        cuisine_type=tracker.get_slot('cuisine')
        location_name=tracker.get_slot('location')
        print(cuisine_type)
        print(location_name)

        zom=Zomato()

        list_all_restaurants=zom.get_all_restraunts(str(location_name),str(cuisine_type))
        
        for r in list_all_restaurants:
            dispatcher.utter_message(r)

        return []
 

class GetRestaurantsWithoutCuisine(Action):

    def name(self):
        return "action_restaurants_nocuisine"


    def run(self, dispatcher,tracker,domain):

        location_name=tracker.get_slot('location')
        
        print(location_name)

        zom=Zomato()

        list_all_restaurants=zom.get_all_restraunts_without_cuisne(str(location_name))
        
        for r in list_all_restaurants:
            dispatcher.utter_message(r)

        return []




class ActionShowRestaurants(Action):

    def name(self):
        return "action_show_restaurants"

    def run(self, dispatcher,tracker,domain):
        zo=Zomato()
        le=LocationExtractor()
        user_input=tracker.latest_message['text']
        cuisine_type=tracker.get_slot('cuisine')
        location_name=le.getLocationInfo(str(user_input))
        print(user_input)
        print(cuisine_type)
        print(location_name)
        list_all_restaurants=zo.get_all_restraunts(location_name[0],str(cuisine_type))
        
        for r in list_all_restaurants:
            dispatcher.utter_message(r)

        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted

import requests
import ast


class Zomato:

    def __init__(self):
        self.api_key="797e936d8ac687c396be2fec2a356217"
        self.base_url = "https://developers.zomato.com/api/v2.1/"


    def getLocationInfo(self,location):
        '''
        Takes city name as argument.
        Returns the corressponding city_id.
        '''
        #list storing latitude,longitude...
        location_info=[]
        print(location)
        queryString={"query":location}
        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r = requests.get(self.base_url+"locations",params=queryString, headers=headers)
        data=r.json()
       # print(data)

        if len(data['location_suggestions']) == 0:
            raise Exception('invalid_location')
            
        else:
            location_info.append(data["location_suggestions"][0]["latitude"])
            location_info.append(data["location_suggestions"][0]["longitude"])
            location_info.append(data["location_suggestions"][0]["entity_id"])
            location_info.append(data["location_suggestions"][0]["entity_type"])
            return location_info

    def get_cuisines(self, location_info):
        """
        Takes City ID as input.
        Returns dictionary of all cuisine names and their respective cuisine IDs in a given city.
        """

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        queryString={"lat":location_info[0],"lon":location_info[1]}
        r = (requests.get(self.base_url +"cuisines",params=queryString,headers=headers).content).decode("utf-8")
        a = ast.literal_eval(r)
        all_cuisines_in_a_city=a['cuisines']


        cuisines={}

        for cuisine in all_cuisines_in_a_city:
            current_cuisine=cuisine['cuisine']
            cuisines[current_cuisine['cuisine_name'].lower()]=current_cuisine['cuisine_id']


        return cuisines


    def get_cuisine_id(self,cuisine_name,location_info):
        '''
        Takes cuisine name and city id as argument.
        Returns the cuisine id for that cuisine.
        '''
        cusines=self.get_cuisines(location_info)
        return cusines[cuisine_name.lower()]


    def get_all_restraunts(self,location,cuisine):
        '''
        Takes city name and cuisine name as arguments.
        Returns a list of 20 restaurants.
        '''
        location_info=self.getLocationInfo(location)
        cuisine_id=self.get_cuisine_id(cuisine,location_info)

        print(location_info)
        print(cuisine_id)

        queryString={"entity_type":location_info[3],"entity_id":location_info[2],"cuisines":cuisine_id,"count":5}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r =requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_ofall_rest=r.json()["restaurants"]
        names_of_all_rest=[]
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])


        return names_of_all_rest

    def get_all_restraunts_without_cuisne(self,location):
        '''
        Takes city name and cuisine name as arguments.
        Returns a list of 20 restaurants.
        '''
        location_info=self.getLocationInfo(location)
        
        queryString={"entity_type":location_info[3],"entity_id":location_info[2],"count":5}

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
       self.bing_api_key="Aiw0X2IXCnSru_O00Rl8c8v6nULH-Z7r1HdFOVW3MQZEJoq6U2kQ_SVabSQui1GU"

    def getLocationInfo(self,query):
        
        list_cities=[]
        queryString={"query":query,"key":self.bing_api_key}
        r = requests.get(self.bing_baseurl,params=queryString)
        data=r.json()
        print(data)
        return data["resourceSets"][0]["resources"][0]["point"]["coordinates"],data["resourceSets"][0]["resources"][0]["name"]
        
        #for x in all_locations["annotations"]:
        #    list_cities.append(x["label"])
            
        #return list_cities

class ActionSetLocation(Action):


    def name(self):
        return "action_set_location"

    def run(self, dispatcher,tracker,domain):
        user_input=tracker.latest_message['text']
        le=LocationExtractor()
        location_name=le.getLocationInfo(str(user_input))
        print(location_name)
        
        return [SlotSet("location",location_name[0])]


class ActionSetCuisine_showRestaurants(Action):
    def name(self):
        return "action_get_cuisine_show_restaurants"


    def run(self, dispatcher,tracker,domain):
        cuisine_type=tracker.get_slot('cuisine')
        location_name=tracker.get_slot('location')
        print(cuisine_type)
        print(location_name)

        zom=Zomato()

        list_all_restaurants=zom.get_all_restraunts(str(location_name),str(cuisine_type))
        
        for r in list_all_restaurants:
            dispatcher.utter_message(r)

        return []
 

class GetRestaurantsWithoutCuisine(Action):

    def name(self):
        return "action_restaurants_nocuisine"


    def run(self, dispatcher,tracker,domain):

        location_name=tracker.get_slot('location')
        
        print(location_name)

        zom=Zomato()

        list_all_restaurants=zom.get_all_restraunts_without_cuisne(str(location_name))
        
        for r in list_all_restaurants:
            dispatcher.utter_message(r)

        return []




class ActionShowRestaurants(Action):

    def name(self):
        return "action_show_restaurants"

    def run(self, dispatcher,tracker,domain):
        zo=Zomato()
        le=LocationExtractor()
        user_input=tracker.latest_message['text']
        cuisine_type=tracker.get_slot('cuisine')
        location_name=le.getLocationInfo(str(user_input))
        print(user_input)
        print(cuisine_type)
        print(location_name)
        list_all_restaurants=zo.get_all_restraunts(location_name[0],str(cuisine_type))
        
        for r in list_all_restaurants:
            dispatcher.utter_message(r)

        return []
