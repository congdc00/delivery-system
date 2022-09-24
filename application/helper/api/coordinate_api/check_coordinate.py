from geopy.geocoders import Nominatim
from pprint import pprint
import json



def get_info(path):
    with open(path) as f:
        data = json.load(f)
        data_location = data["info_customer"]["location"]
        
        street = data_location["street"]
        district = data_location["district"]
        city = data_location["city"]
        nation = data_location["nation"]

    
    return street, district, city, nation


def get_coordinate():
    path = "../data_example/customer01/info.json"
    street, district, city, nation = get_info(path)

    name_location =street + ", " + district + ", " + city +", "+ nation
    app = Nominatim(user_agent="tutorial")
    location = app.geocode(name_location).raw

    coordinate_x = location['lat']
    coordinate_y = location['lon']

    # print raw data
    return coordinate_x, coordinate_y