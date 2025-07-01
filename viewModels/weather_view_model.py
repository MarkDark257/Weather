import os
from os import sys
import datetime
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.resources import resource_add_path, resource_find
from config import design
from model.weather import Weather
# Icons
from config import SUN, CLOUDS, RAIN, EXTREME, ERROR
# Background colors
from config import DEFAULT_COLOR, CLEAR_COLOR, CLOUDS_COLOR, RAIN_COLOR, EXTREME_COLOR

kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'weather_view.kv')
if os.path.exists(kv_path):
    Builder.load_file(kv_path)
    print(">>> kv file loaded successfully")
else:
    print(">>> kv file not found at", kv_path)

if getattr(sys, 'frozen', False):
    basedir = sys._MEIPASS
    resource_add_path(os.path.join(basedir))
else:
    resource_add_path(os.path.dirname(__file__))

class WeatherViewModel(BoxLayout):
    _weather_data: Weather

    def __init__(self, model: Weather, **kwargs):
        print(">>> __init__")
        super(WeatherViewModel, self).__init__(**kwargs)
        self._weather_data = model
        Window.size = (design["window"]["width"], design["window"]["height"])
        Window.resizable = False

    def update_weather(self):
        print(">>> update_weather()")
        text_template = "[color=ffffff]{}[/color]"
        current_datetime = datetime.datetime.now()
        self.ids.city.text = text_template.format("[b]" + self._weather_data.city_name + "[/b]")
        self.ids.curr_month.text = text_template.format(current_datetime.strftime('%B') + " " + current_datetime.strftime('%d') + "\n" + text_template.format((current_datetime.strftime('%A'))))
        self.ids.curr_temp.text = text_template.format("[b]" + self._weather_data.current_temp + "[/b]")
        self.ids.flike.text = text_template.format("Feels like " + self._weather_data.feels_like)
        self.ids.weather_image.source, Window.clearcolor = self._map_visuals(self._weather_data.current_weather)
        self.ids.curr_weather.text = text_template.format("[b]" + self._weather_data.current_weather + "[/b]")
        self.ids.id_wind.text = text_template.format(self._weather_data.wind_direction)
        self.ids.id_wind_speed.text = text_template.format(self._weather_data.wind_speed)
        self.ids.id_visibility.text = text_template.format(self._weather_data.visibility)
        self.ids.id_pressure.text = text_template.format(self._weather_data.pressure)
        self.ids.id_humidity.text = text_template.format(self._weather_data.humidity)
        self.ids.id_sunrise.text = text_template.format("Sunrise: {}".format(current_datetime.fromtimestamp(self._weather_data.sunrise).strftime("%H:%M")))
        self.ids.id_sunset.text = text_template.format("Sunset: {}".format(current_datetime.fromtimestamp(self._weather_data.sunset).strftime("%H:%M")))


    def _map_visuals(self, weather_type: str):
        mapping = {
            "Clear": (SUN, CLEAR_COLOR),
            "Clouds": (CLOUDS, CLOUDS_COLOR),
            "Rain": (RAIN, RAIN_COLOR),
            "Extreme": (EXTREME, EXTREME_COLOR),
        }
        return mapping.get(weather_type, (ERROR, DEFAULT_COLOR))