from kivy.app import App;
from model.weather import Weather;
from services.adapter import Adapter;
from services.api_request import ApiRequest
from viewModels.weather_view_model import WeatherViewModel;

class MyApp(App):
    _weather_data: Weather;

    def build(self):
        self.model = Weather();
        self.apiRequest = ApiRequest();
        self.adapter = Adapter(self.apiRequest, self.model);
        self._weather_data = self.adapter.get_weather_data();
        self.view = WeatherViewModel(self._weather_data);
        self.view.update_weather();
        return self.view;

if __name__ == "__main__":
    MyApp().run();