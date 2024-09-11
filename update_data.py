import datetime
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

# city_name = f"{weather_data['name']}"
#             background_colortemperature = f"{round(weather_data['main']['temp'] - 273)}°C"
#             background_colormax_temperature = f"{round(weather_data['main']['temp_max'] - 273)}°C"
#             background_colormin_temperature = f"{round(weather_data['main']['temp_min'] - 273)}°C"
            
#             background_colorweather = weather_data['weather'][0]['main']
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

def direction(self, deg):
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



def update_app():
    print(">>> update_app()")

    background_colorweather = ""

    if background_colorweather == "Clear":
        img_source = SUN
        background_color = CLEAR_COLOR
    elif background_colorweather == "Clouds":
        img_source = CLOUDS
        background_color = CLOUDS_COLOR
    elif background_colorweather == "Rain":
        img_source = RAIN
        background_color = CLOUDS_COLOR
    elif background_colorweather == "Extreme":
        img_source = EXTREME
        background_color = EXTREME_COLOR
    else:
        print(f">>> {background_colorweather}")
        error_app()

    text_template = "[color=ffffff]{}[/color]"
    background_colordatetime = datetime.datetime.now()

    def error_app(self):
        print(">>> error_app()")
        city_name = "N/A"
        current_temperature = "N/A"
        current_max_temperature = "N/A"
        current_min_temperature = "N/A"
        current_wind_speed = "N/A"
        current_weather = "N/A"
        feels_like = "N/A"
        img_source = ERROR
        wind = "N/A"
        wind_speed = "N/A"
        visibility = "N/A"
        pressure = "N/A"
        humidity = "N/A"
        sunrise = "N/A"
        sunset = "N/A"
        ba = DEFAULT_COLOR