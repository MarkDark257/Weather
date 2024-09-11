import requests
import os
import datetime
from kivy.app import App
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.lang import Builder
from os import sys
from kivy.resources import resource_add_path, resource_find

kv_path = os.path.join(os.path.dirname(__file__), 'weather.kv')

Builder.load_file(kv_path)

if getattr(sys, 'frozen', False):
    # Если приложение собрано с помощью PyInstaller
    basedir = sys._MEIPASS
    resource_add_path(os.path.join(basedir))
else:
    # Если приложение запускается из исходного кода
    resource_add_path(os.path.dirname(__file__))

# Window
WINDOWS_H = 768
WINDOWS_W = 1278

# # Backgrounds color
# DEFAULT_COLOR = (0.5, 0.5, 0.5, 0.5)
# CLEAR_COLOR = (0, 0.5, 1, 0.8)
# CLOUDS_COLOR = (0.286, 0.463, 0.639, 1)
# EXTREME_COLOR = (0.18, 0.267, 0.349 , 1)

# # Request
# LAT = 52.96
# LON = 10.56
# APIKEY = 'b40ce6c7fa6d3d87eebf9c6c063bd1dc'
# URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APIKEY}"

# # Text
# TEXT_COLOR = "ffffff"

# # Icons
# SUN = "./icons/sun.png"
# CLOUDS = "./icons/cloudy.png"
# RAIN = "./icons/rainy.png"
# EXTREME = "./icons/extreme-weather.png"
# ERROR = "./icons/404-error.png"

class Weather(BoxLayout):
    def __init__(self, **kwargs):
        print(">>> __init__")
        super(Weather, self).__init__(**kwargs)

        Window.size = (WINDOWS_W, WINDOWS_H)
        Window.resizable = False

        # Get current data
        self.weather_request()

        # And update all
        self.update_app()


    # def weather_request(self):
    #     print(">>> weather_request()")
    #     response = requests.get(URL)
    #     if response.status_code == 200:
    #         weather_data = response.json()

    #         self.city_name = f"{weather_data['name']}"
    #         self.current_temperature = f"{round(weather_data['main']['temp'] - 273)}°C"
    #         self.current_max_temperature = f"{round(weather_data['main']['temp_max'] - 273)}°C"
    #         self.current_min_temperature = f"{round(weather_data['main']['temp_min'] - 273)}°C"
            
    #         self.current_weather = weather_data['weather'][0]['main']
    #         self.feels_like = f"{round(weather_data['main']['feels_like'] - 273)}°C"
            
    #         print(">>>> ".format( weather_data['wind']['deg']))

    #         self.wind = f"Wind: {self.direction(weather_data['wind']['deg'])} "
    #         self.wind_speed = f"Speed(m/s): {weather_data['wind']['speed']} Gust: {weather_data['wind']['gust']} "
    #         self.visibility = f"Visibility: {weather_data['visibility']}m"
    #         self.pressure = f"Pressure: {weather_data['main']['pressure']}mbar"
    #         self.humidity = f"Humidity: {weather_data['main']['humidity']}%"
    #         self.sunrise = weather_data['sys']['sunrise']
    #         self.sunset = weather_data['sys']['sunset']
    #     else:
    #         print(f">>> {self.responce.status_code}")
    #         self.error_app()

    # def direction(self, deg):
    #     if (deg >= 0 and deg < 22.5) and (deg > 337.5 and deg <= 360):
    #         return "North"
    #     elif deg >= 22.5 and deg < 67.5:
    #         return "North-East"
    #     elif deg > 67.5 and deg < 112.5:
    #         return "East"
    #     elif deg > 112.5 and deg < 157.5:
    #         return "South-East"
    #     elif deg > 157.5 and deg < 202.5:
    #         return "South"
    #     elif deg > 202.5 and deg < 247.5:
    #         return "South-West"
    #     elif deg > 247.5 and deg < 292.5:
    #         return "West"
    #     elif deg > 292.5 and deg < 337.5:
    #         return "North-West"



    # def update_app(self):
    #     print(">>> update_app()")

    #     weather_color_clear = (0, 0.5, 1, 0.8)
    #     weather_color_clouds = (0.286, 0.463, 0.639, 1)
    #     weather_color_extreme = (0.18, 0.267, 0.349 , 1)

    #     if self.current_weather == "Clear":
    #         self.img_source = SUN
    #         Window.clearcolor = CLEAR_COLOR
    #     elif self.current_weather == "Clouds":
    #         self.img_source = CLOUDS
    #         Window.clearcolor = CLOUDS_COLOR
    #     elif self.current_weather == "Rain":
    #         self.img_source = RAIN
    #         Window.clearcolor = CLOUDS_COLOR
    #     elif self.current_weather == "Extreme":
    #         self.img_source = EXTREME
    #         Window.clearcolor = EXTREME_COLOR
    #     else:
    #         print(f">>> {self.current_weather}")
    #         self.error_app()

        # text_template = "[color=ffffff]{}[/color]"
        # current_datetime = datetime.datetime.now()

        self.ids.city.text = text_template.format("[b]" + self.city_name + "[/b]")
        self.ids.curr_month.text = text_template.format(current_datetime.strftime('%B') + " " + current_datetime.strftime('%d') + 
                "\n" + text_template.format((current_datetime.strftime('%A'))))
        #self.ids.curr_day_of_week.text = text_template.format(current_datetime.strftime('%A'))
        self.ids.curr_temp.text = text_template.format("[b]" + self.current_temperature + "[/b]")
        self.ids.flike.text = text_template.format("Feels like " + self.feels_like)

        self.ids.weather_image.source = self.img_source
        self.ids.curr_weather.text = text_template.format("[b]" + self.current_weather + "[/b]")

        self.ids.id_wind.text = text_template.format(self.wind)
        self.ids.id_wind_speed.text = text_template.format(self.wind_speed)
        self.ids.id_visibility.text = text_template.format(self.visibility)
        self.ids.id_pressure.text = text_template.format(self.pressure)
        self.ids.id_humidity.text = text_template.format(self.humidity)
        self.ids.id_sunrise.text = text_template.format("Sunrise: {}".format(current_datetime.fromtimestamp(self.sunrise).strftime("%H:%M")))
        self.ids.id_sunset.text = text_template.format("Sunset: {}".format(current_datetime.fromtimestamp(self.sunset).strftime("%H:%M")))


    # def error_app(self):
    #     print(">>> error_app()")
    #     self.city_name = "N/A"
    #     self.current_temperature = "N/A"
    #     self.current_max_temperature = "N/A"
    #     self.current_min_temperature = "N/A"
    #     self.current_wind_speed = "N/A"
    #     self.current_weather = "N/A"
    #     self.feels_like = "N/A"
    #     self.img_source = ERROR
    #     self.wind = "N/A"
    #     self.wind_speed = "N/A"
    #     self.visibility = "N/A"
    #     self.pressure = "N/A"
    #     self.humidity = "N/A"
    #     self.sunrise = "N/A"
    #     self.sunset = "N/A"
    #     Window.clearcolor = DEFAULT_COLOR


class MyApp(App):
    def build(self):
        #Window.clearcolor = (0, 0.5, 1, 0.8)
        return Weather()

if __name__ == "__main__":
    MyApp().run()
