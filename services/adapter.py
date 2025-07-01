from interfaces.i_request import IRequest
from model.weather import Weather
from config import *

class Adapter():
    _request: IRequest
    _weather_data: Weather

    def __init__(self, request: IRequest, model: Weather):
        self._request = request
        self._weather_data = model

        response = self._api_request()
        if response.status_code == 200:
            self._filter_response(response.json())
        else:
            self._error_app("Error fetching data")
        print(">>> Adapter initialized")

    def get_weather_data(self) -> Weather:
        return self._weather_data

    def _api_request(self) -> dict:
        response = self._request.request()
        if response:
            print(">>> Response received")
            return response
        else:
            self._error_app("Error fetching data")
            return {}

    def _direction(self, deg):
        if (deg < 22.5):
            return "North"
        if (deg < 67.5):
            return "North-East"
        if (deg < 112.5):
            return "East"
        if (deg < 157.5):
            return "South-East"
        if (deg < 202.5):
            return "South"
        if (deg < 247.5):
            return "South-West"
        if (deg < 292.5):
            return "West"
        if (deg < 337.5):
            return "North-West"
        else:
            return "North"

    def _filter_response(self, json_response):
        print(">>> _filter_response()")
        print(">>> ", json_response["name"])

        main = json_response["main"]

        self._weather_data.city_name = json_response["name"]
        self._weather_data.current_weather = json_response['weather'][0]['main']
        self._weather_data.current_temp = f"{self._kelvin_to_celsius_str(main.get('temp'))}"
        self._weather_data.feels_like = f"{self._kelvin_to_celsius_str(main.get('feels_like'))}"
        self._weather_data.max_temp = f"{self._kelvin_to_celsius_str(main.get('temp_max'))}"
        self._weather_data.min_temp = f"{self._kelvin_to_celsius_str(main.get('temp_min'))}"
        self._weather_data.wind_direction = f"Wind: {self._direction(json_response['wind']['deg'])} "
        self._weather_data.wind_speed = f"Speed(m/s): {json_response['wind']['speed']} Gust: {json_response['wind']['gust']} "
        self._weather_data.visibility = f"Visibility: {json_response['visibility']}m"
        self._weather_data.pressure = f"Pressure: {main.get('pressure')}mbar"
        self._weather_data.humidity = f"Humidity: {main.get('humidity')}%"
        self._weather_data.sunrise = json_response['sys']['sunrise']
        self._weather_data.sunset = json_response['sys']['sunset']
    
    def _kelvin_to_celsius_str(self, k: float) -> str:
        return f"{round(k - 273.15)}°C"
    
    def _error_app(self, errmsg="Error fetching data"):
        print(">>> error_app()")
        self._weather_data = Weather(city_name=errmsg)
