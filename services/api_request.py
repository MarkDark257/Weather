import requests;
from config import URL
from interfaces.i_request import IRequest;

class ApiRequest(IRequest):
    def __init__(self):
        pass

    def request(self):
        print(">>> weather_request()")
        response = requests.get(URL)
        return response