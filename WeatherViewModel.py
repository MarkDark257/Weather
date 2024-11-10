import os
from os import sys
import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.resources import resource_add_path, resource_find

from WeatherModel import WModel


kv_path = os.path.join(os.path.dirname(__file__), 'WeatherView.kv')
if os.path.exists(kv_path):
    Builder.load_file(kv_path)
    print("kv file loaded successefully")
else:
    print("kv file not found")

if getattr(sys, 'frozen', False):
    basedir = sys._MEIPASS
    resource_add_path(os.path.join(basedir))
else:
    resource_add_path(os.path.dirname(__file__))


# Window
WINDOWS_H = 768
WINDOWS_W = 1278

class WViewModel(BoxLayout):
    def __init__(self, **kwargs):
        print(">>> __init__")
        super(WViewModel, self).__init__(**kwargs)

        Window.size = (WINDOWS_W, WINDOWS_H)
        Window.resizable = False

    def update_weather(self, weather_data):
        text_template = "[color=ffffff]{}[/color]"
        current_datetime = datetime.datetime.now()

        self.ids.city.text = text_template.format("[b]" + weather_data["city_name"] + "[/b]")
        
        self.ids.curr_month.text = text_template.format(current_datetime.strftime('%B') + " " + current_datetime.strftime('%d') + 
                "\n" + text_template.format((current_datetime.strftime('%A'))))
        
        self.ids.curr_temp.text = text_template.format("[b]" + weather_data["current_temperature"] + "[/b]")
        self.ids.flike.text = text_template.format("Feels like " + weather_data["feels_like"])

        self.ids.weather_image.source = weather_data["image_source"]
        self.ids.curr_weather.text = text_template.format("[b]" + weather_data["current_weather"] + "[/b]")

        self.ids.id_wind.text = text_template.format(weather_data["wind_direction"])
        self.ids.id_wind_speed.text = text_template.format(weather_data["wind_speed"])
        self.ids.id_visibility.text = text_template.format(weather_data["visibility"])
        self.ids.id_pressure.text = text_template.format(weather_data["pressure"])
        self.ids.id_humidity.text = text_template.format(weather_data["humidity"])
        self.ids.id_sunrise.text = text_template.format("Sunrise: {}".format(current_datetime.fromtimestamp(weather_data["sunrise"]).strftime("%H:%M")))
        self.ids.id_sunset.text = text_template.format("Sunset: {}".format(current_datetime.fromtimestamp(weather_data["sunset"]).strftime("%H:%M")))

        Window.clearcolor = weather_data["background_color"]

class MyApp(App):
    def build(self):
        self.model = WModel()
        self.view = WViewModel()
        
        self.view.update_weather(self.model.get_weather())

        return self.view

if __name__ == "__main__":
    MyApp().run()