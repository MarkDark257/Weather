# Backgrounds color
DEFAULT_COLOR = (0.5, 0.5, 0.5, 0.5)
CLEAR_COLOR = (0, 0.5, 1, 0.8)
CLOUDS_COLOR = (0.286, 0.463, 0.639, 1)
RAIN_COLOR = (0.2, 0.2, 0.2, 1)
EXTREME_COLOR = (0.18, 0.267, 0.349 , 1)

# Icons
SUN = "./icons/sun.png"
CLOUDS = "./icons/cloudy.png"
RAIN = "./icons/rainy.png"
EXTREME = "./icons/extreme-weather.png"
ERROR = "./icons/404-error.png"

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
        "EXTREME_COLOR": (0.18, 0.267, 0.349 , 1),
    },
    "icons": {
        "SUN": "./icons/sun.png",
        "CLOUDS": "./icons/cloudy.png",
        "RAIN": "./icons/rainy.png",
        "EXTREME": "./icons/extreme-weather.png",
        "ERROR": "./icons/404-error.png"
    }
}

# Request
LAT = 52.96
LON = 10.56
APIKEY = 'b40ce6c7fa6d3d87eebf9c6c063bd1dc'
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APIKEY}"

api = {
    "lat": 52.96,
    "lon": 10.56,
    "api-key": 'b40ce6c7fa6d3d87eebf9c6c063bd1dc',
    "url": "https://api.openweathermap.org/data/2.5/weather?"
}