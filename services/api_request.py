import requests;
from config import URL
from interfaces.i_request import IRequest;

class ApiRequest(IRequest):
    def __init__(self):
        pass

    def request(self) -> dict:
        print(">>> weather_request()")
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            self._error_app(response.status_code)