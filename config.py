# Backgrounds color
DEFAULT_COLOR = (0.5, 0.5, 0.5, 0.5)
CLEAR_COLOR = (0, 0.5, 1, 0.8)
CLOUDS_COLOR = (0.286, 0.463, 0.639, 1)
RAIN_COLOR = (0.2, 0.2, 0.2, 1)
EXTREME_COLOR = (0.18, 0.267, 0.349 , 1)

# Icons
SUN = "./assets/icons/sun.png"
CLOUDS = "./assets/icons/cloudy.png"
RAIN = "./assets/icons/rainy.png"
EXTREME = "./assets/icons/extreme-weather.png"
ERROR = "./assets/icons/error.png"

design = {
    "window": {
        "height": 768,
        "width": 1278,
        "resizable": False
    },
    "background_color": {
        "DEFAULT_COLOR": (0.5, 0.5, 0.5, 0.5),
        "CLEAR_COLOR": (0, 0.5, 1, 0.8),
        "CLOUDS_COLOR": (0.286, 0.463, 0.639, 1),
        "RAIN_COLOR": (0.2, 0.2, 0.2, 1),
        "EXTREME_COLOR": (0.18, 0.267, 0.349 , 1),
    },
    "icons": {
        "SUN": "./assets/icons/sun.png",
        "CLOUDS": "./assets/icons/cloudy.png",
        "RAIN": "./assets/icons/rainy.png",
        "EXTREME": "./assets/icons/extreme-weather.png",
        "ERROR": "./assets/icons/error.png"
    }
}

# Request
LAT = 52.96
LON = 10.56
import os

APIKEY = os.getenv('OPENWEATHER_API_KEY')
if not APIKEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable not set")
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APIKEY}"

api = {
    "lat": 52.96,
    "lon": 10.56,
    "api-key": APIKEY,
    "url": "https://api.openweathermap.org/data/2.5/weather?"
}