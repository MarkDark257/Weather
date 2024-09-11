import requests


# Request
LAT = 52.96
LON = 10.56
APIKEY = 'b40ce6c7fa6d3d87eebf9c6c063bd1dc'
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APIKEY}"

def weather_request(self):
    print(">>> weather_request()")
    try:
        response = requests.get(URL)
    except ValueError as verr:
        show_error(verr)

    if response.status_code == 200:
        weather_data = response.json()
    else:
