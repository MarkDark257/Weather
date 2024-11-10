import datetime
import requests
from typing import Dict

# Backgrounds color
DEFAULT_COLOR = (0.5, 0.5, 0.5, 0.5)
CLEAR_COLOR = (0, 0.5, 1, 0.8)
CLOUDS_COLOR = (0.286, 0.463, 0.639, 1)
EXTREME_COLOR = (0.18, 0.267, 0.349 , 1)

# Icons
SUN = "./icons/sun.png"
CLOUDS = "./icons/cloudy.png"
RAIN = "./icons/rainy.png"
EXTREME = "./icons/extreme-weather.png"
ERROR = "./icons/404-error.png"


# Request
LAT = 52.96
LON = 10.56
APIKEY = 'b40ce6c7fa6d3d87eebf9c6c063bd1dc'
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APIKEY}"

class WModel(object):
    def __init__(self):
        self._weather_data = dict()

    def get_weather(self):
        self._formating_data(self._request())
        return self._weather_data

    def _request(self):
        print(">>> weather_request()")

        response = requests.get(URL)

        if response.status_code == 200:
            return response.json()
        else:
            self._error_app(response.status_code)

    def _direction(self, deg):
        if (deg >= 0 and deg < 22.5) and (deg > 337.5 and deg <= 360):
            return "North"
        elif deg >= 22.5 and deg < 67.5:
            return "North-East"
        elif deg > 67.5 and deg < 112.5:
            return "East"
        elif deg > 112.5 and deg < 157.5:
            return "South-East"
        elif deg > 157.5 and deg < 202.5:
            return "South"
        elif deg > 202.5 and deg < 247.5:
            return "South-West"
        elif deg > 247.5 and deg < 292.5:
            return "West"
        elif deg > 292.5 and deg < 337.5:
            return "North-West"

    def _formating_data(self, json_response):
        print(">>> _formating_data()")
        print(">>> ", json_response["name"])

        self._weather_data["city_name"] = f"{json_response['name']}"
        self._weather_data["current_weather"] = json_response['weather'][0]['main']
        self._weather_data["current_temperature"] = f"{round(json_response['main']['temp'] - 273)}°C"
        self._weather_data["feels_like"] = f"{round(json_response['main']['feels_like'] - 273)}°C"
        self._weather_data["max_temperature"] = f"{round(json_response['main']['temp_max'] - 273)}°C"
        self._weather_data["min_temperature"] = f"{round(json_response['main']['temp_min'] - 273)}°C"
        self._weather_data["wind_direction"] = f"Wind: {self._direction(json_response['wind']['deg'])} "
        self._weather_data["wind_speed"] = f"Speed(m/s): {json_response['wind']['speed']} Gust: {json_response['wind']['gust']} "
        self._weather_data["visibility"] = f"Visibility: {json_response['visibility']}m"
        self._weather_data["pressure"] = f"Pressure: {json_response['main']['pressure']}mbar"
        self._weather_data["humidity"] = f"Humidity: {json_response['main']['humidity']}%"
        self._weather_data["sunrise"] = json_response['sys']['sunrise']
        self._weather_data["sunset"] = json_response['sys']['sunset']

        if self._weather_data["current_weather"] == "Clear":
            self._weather_data["image_source"] = SUN
            self._weather_data["background_color"] = CLEAR_COLOR
        elif self._weather_data["current_weather"] == "Clouds":
            self._weather_data["image_source"] = CLOUDS
            self._weather_data["background_color"] = CLOUDS_COLOR
        elif self._weather_data["current_weather"] == "Rain":
            self._weather_data["image_source"] = RAIN
            self._weather_data["background_color"] = CLOUDS_COLOR
        elif self._weather_data["current_weather"] == "Extreme":
            self._weather_data["image_source"] = EXTREME
            self._weather_data["background_color"] = EXTREME_COLOR
        else:
            print(">>> ", {self._weather_data["current_weather"]})
            self._error_app()
    
    def _error_app(self, errmsg):
        print(">>> error_app()")
        self._weather_data = {
            "city_name" : errmsg,
            "current_weather" : "N/A",
            "current_temperature" : "N/A",
            "feels_like" : "N/A",
            "max_temperature" : "N/A",
            "min_temperature" : "N/A",
            "wind_direction" : "N/A",
            "wind_speed" : "N/A",
            "visibility" : "N/A",
            "pressure" : "N/A",
            "humidity" : "N/A",
            "sunrise" : "N/A",
            "sunset" : "N/A",
            "img_source" : ERROR,
            "background_color" : DEFAULT_COLOR
        }

    #             city_name = f"{weather_data['name']}"
    #             temperature = f"{round(weather_data['main']['temp'] - 273)}°C"
    #             max_temperature = f"{round(weather_data['main']['temp_max'] - 273)}°C"
    #             min_temperature = f"{round(weather_data['main']['temp_min'] - 273)}°C"
                
    #             weather = weather_data['weather'][0]['main']
    #             feels_like = f"{round(weather_data['main']['feels_like'] - 273)}°C"
                
    #             print(">>>> ".format( weather_data['wind']['deg']))

    #             wind = f"Wind: {direction(weather_data['wind']['deg'])} "
    #             wind_speed = f"Speed(m/s): {weather_data['wind']['speed']} Gust: {weather_data['wind']['gust']} "
    #             visibility = f"Visibility: {weather_data['visibility']}m"
    #             pressure = f"Pressure: {weather_data['main']['pressure']}mbar"
    #             humidity = f"Humidity: {weather_data['main']['humidity']}%"
    #             sunrise = weather_data['sys']['sunrise']
    #             sunset = weather_data['sys']['sunset']
    #         else:
    #             print(f">>> {responce.status_code}")
    #             error_app()