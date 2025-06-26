# File: model/Weather.py
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Weather:
    city_name: str = ""
    current_weather: str = ""
    current_temp: str = ""
    feels_like: float = 0.0
    max_temp: float = 0.0
    min_temp: float = 0.0
    wind_direction: str = ""
    wind_speed: float = 0.0
    visibility: float = 0.0
    pressure: float = 0.0
    humidity: int = 0
    sunrise: datetime = field(default_factory=datetime.now)
    sunset: datetime = field(default_factory=datetime.now)