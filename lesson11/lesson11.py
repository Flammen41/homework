import json
from pprint import pprint

import requests

# get JSON string data from CityBike NYC using web requests library
json_response = requests.get("https://feeds.citibikenyc.com/stations/stations.json")
# check type of json_response object
print(json_response)
print(type(json_response.text))
#print(json_response.text)
# load data in loads() function of json library
bike_dict = json.loads(json_response.text)
#check type of news_dict
pprint(type(bike_dict))
# now get stationBeanList key data from dict
pprint(bike_dict['stationBeanList'])
bikelist = []
for i in bike_dict['stationBeanList']:
     bikelist.append(i)
#
print(bike_dict['stationBeanList'][100]['id'])
#
# fulton = bike_dict['stationBeanList'][100]
# print(type(fulton))
# print(fulton['stationName'])