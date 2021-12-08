"""Dataclass models for storing data fetched from the
OpenWeatherMap API from JSON"""

from typing import Optional, Union
from dataclasses import dataclass

@dataclass
class OWM():
    """Class for storing data fetched from API"""
    @dataclass
    class Coords():
        longitude: float
        latitude: float

    @dataclass
    class Weather():
        main: str
        description: str

    @dataclass
    class Main():
        temperature: float
        feels_like: float
        minimum: float
        maximum: float
        pressure: int
        humidity: int
        sea_level: Optional[Union[int, None]]
        ground_level: Optional[Union[int, None]]

    @dataclass
    class Wind():
        speed: Optional[Union[float, None]]
        degree: Optional[Union[int, None]]
        gust: Optional[Union[float, None]]

    @dataclass
    class Rain():
        one_hour: Optional[Union[int, None]]
        three_hours: Optional[Union[int, None]]

    @dataclass
    class Snow():
        one_hour: Optional[Union[int, None]]
        three_hours: Optional[Union[int, None]]

    @dataclass
    class Sys():
        country: str
        sunrise: int
        sunset: int

    coords: Coords
    weather: Weather
    main: Main
    visibility: int
    wind: Optional[Union[Wind, None]]
    clouds: int
    rain: Optional[Union[Rain, None]]
    snow: Optional[Union[Snow, None]]
    datetime: int
    sys: Sys
    timezone: int
    id: int
    name: str

@dataclass
class Error():
    """Class for storing API errors"""
    code: int
    message: str
