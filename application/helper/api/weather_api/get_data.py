import datetime as dt
from multiprocessing import current_process
from urllib import response
import requests

API_KEY = open('./weather_api/api_key', 'r').read()
CITY = "Hanoi"
NUM_DAY = "5"

def get_info(response, type):
    if type == 0:
        info = response["current"]
        temp = info["temp_c"]
        wind_kph = info["wind_kph"]
        return temp, wind_kph
    else:
        num_day = int(NUM_DAY)
        list_info = response["forecast"]["forecastday"]
        for i in range (0, num_day):
            info = list_info[i]

            day = info["date"] 
            print(f"ngay thu {day} :")

            temp = info["day"]["avgtemp_c"]
            print(f"-- nhiet do {temp}")

            maxwind_kph = info["day"]["maxwind_kph"]
            print(f"-- toc do gio {maxwind_kph}")

            daily_will_it_rain = info["day"]["daily_will_it_rain"]
            print(f"-- rain: {daily_will_it_rain}")
            

            
if __name__ == "__main__":
    url = f'https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days={NUM_DAY}&aqi=yes&alerts=yes'
    response = requests.get(url).json()
    
    print("---curent")
    info_current = get_info(response, type=0)
    text1 = f"Thoi tiet hien tai nhiet do {info_current[0]} va toc do gio {info_current[1]}"
    print(text1)

    print("---predict")
    get_info(response, type=1)
    








