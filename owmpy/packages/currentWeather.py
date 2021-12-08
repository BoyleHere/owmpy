"""Fetch current weather data for one location

Access current weather data for any location on Earth including
200,000 cities.
"""

import requests
from typing import Union
from owmpy.data.auth import AuthenticateAPIKey
from owmpy.data.models import OWM, Error
from owmpy.utils.convert import ConvertToJSON
from owmpy.utils.exceptions import APIAuthenticationError, APIFetchError

class CurrentWeatherData(AuthenticateAPIKey, ConvertToJSON):
    """Class for fetching the current weather data using
    the OpenWeatherMap API

    Attributes
    ----------
    key : str
        OpenWeatherMap API key

    Methods
    -------
    byCityName(city, country = None, state = None, units = None, language = None, type = None)
        Fetch data with city name
    byCityID(id, units = None, language = None, type = None)
        Fetch data with city ID (http://bulk.openweathermap.org/sample/city.list.json.gz)
    byCoords(latitude, longitude, units = None, language = None, type = None)
        Fetch data with coordinates of a city
    byZipCode(zip, units = None, language = None, type = None)
        Fetch data with Zip code of a city
    """

    def __init__(self, key: str):
        """
        Parameters
        ----------
        key : str
            OpenWeatherMap API key
        """
        AuthenticateAPIKey.__init__(self, key)
        if self._authenticate() is False:
            raise APIAuthenticationError

    def byCityName(
        self,
        city: str,
        country: str = None,
        state: str = None,
        units: str = None,
        language: str = None,
        type: str = None
    ) -> Union[bool, OWM, dict]:
        """Get data by using a city name as parameter

        Parameters
        ----------
        city : str
            City to fetch data for
        country : str, optional
            Country of the city
        state : str, optional
            State of the city
        units : str, optional
            Unit of measurement
        language : str, optional
            Language of fetched data
        type : str, optional
            Type of return data

        Returns
        -------
        OWM
            Dataclass formatted with fetched data
        dict
            Dictionary/JSON of fetched data
        bool
            False if any error occurs
        """
        try:
            if state is not None and country is not None:
                URL = f"{self.api}/weather?q={city},{state},{country}&appid={self.key}"
            elif country is not None:
                URL = f"{self.api}/weather?q={city},{country}&appid={self.key}"
            elif state is not None:
                URL = f"{self.api}/weather?q={city},{state}&appid={self.key}"
            else:
                URL = f"{self.api}/weather?q={city}&appid={self.key}"
            if units is not None:
                units = units.lower()
                if units in self.units:
                    URL += f"&units={units}"
            if language is not None:
                language = language.lower()
                if language in self.langs.keys():
                    URL += f"&lang={language}"
                elif language in self.langs.values():
                    for lang in self.langs:
                        if self.langs[lang] == language:
                            URL += f"&lang={lang}"
                            break
            DATA = requests.get(url = URL).json()
            if DATA["cod"] == 200:
                if type is not None:
                    if type.lower() in ["dict", "json"]:
                        return DATA
                else:
                    ConvertToJSON.__init__(self, DATA)
                    return self._toOMW()
            else:
                return Error(code = DATA["cod"], message = DATA["message"])

        except:
            raise APIFetchError

    def byCityID(
        self,
        id: int,
        units: str = None,
        language: str = None,
        type: str = None
    ) -> Union[bool, OWM, dict]:
        """Get data by using a city ID as parameter

        Parameters
        ----------
        id : int
            ID of city
        units : str, optional
            Unit of measurement
        language : str, optional
            Language of fetched data
        type : str, optional
            Type of return data

        Returns
        -------
        OWM
            Dataclass formatted with fetched data
        dict
            Dictionary/JSON of fetched data
        bool
            False if any error occurs
        """
        try:
            URL = f"{self.api}/weather?id={id}&appid={self.key}"
            if units is not None:
                units = units.lower()
                if units in self.units:
                    URL += f"&units={units}"
            if language is not None:
                language = language.lower()
                if language in self.langs.keys():
                    URL += f"&lang={language}"
                elif language in self.langs.values():
                    for lang in self.langs:
                        if self.langs[lang] == language:
                            URL += f"&lang={lang}"
                            break
            DATA = requests.get(url = URL).json()
            if DATA["cod"] == 200:
                if type is not None:
                    if type.lower() in ["dict", "json"]:
                        return DATA
                else:
                    ConvertToJSON.__init__(self, DATA)
                    return self._toOMW()
            else:
                return Error(code = DATA["cod"], message = DATA["message"])

        except:
            raise APIFetchError

    def byCoords(
        self,
        latitude: float,
        longitude: float,
        units: str = None,
        language: str = None,
        type: str = None
    ) -> Union[bool, OWM, dict]:
        """Get data by using latitude and longitude as parameters

        Parameters
        ----------
        latitude: float
            Latitude of the location
        longitude: float
            Longitude of the location
        units : str, optional
            Unit of measurement
        language : str, optional
            Language of fetched data
        type : str, optional
            Type of return data

        Returns
        -------
        OWM
            Dataclass formatted with fetched data
        dict
            Dictionary/JSON of fetched data
        bool
            False if any error occurs
        """
        try:
            URL = f"{self.api}/weather?lat={latitude}&lon={longitude}&appid={self.key}"
            if units is not None:
                units = units.lower()
                if units in self.units:
                    URL += f"&units={units}"
            if language is not None:
                language = language.lower()
                if language in self.langs.keys():
                    URL += f"&lang={language}"
                elif language in self.langs.values():
                    for lang in self.langs:
                        if self.langs[lang] == language:
                            URL += f"&lang={lang}"
                            break
            DATA = requests.get(url = URL).json()
            if DATA["cod"] == 200:
                if type is not None:
                    if type.lower() in ["dict", "json"]:
                        return DATA
                else:
                    ConvertToJSON.__init__(self, DATA)
                    return self._toOMW()
            else:
                return Error(code = DATA["cod"], message = DATA["message"])

        except:
            raise APIFetchError

    def byZipCode(
        self,
        zip: int,
        country: str = None,
        units: str = None,
        language: str = None,
        type: str = None
    ) -> Union[bool, OWM, dict]:
        """Get data by using Zip code as parameter

        Parameters
        ----------
        zip : int
            Zip code of city
        units : str, optional
            Unit of measurement
        language : str, optional
            Language of fetched data
        type : str, optional
            Type of return data

        Returns
        -------
        OWM
            Dataclass formatted with fetched data
        dict
            Dictionary/JSON of fetched data
        bool
            False if any error occurs
        """
        try:
            if country is not None:
                URL = f"{self.api}/weather?zip={zip},{country}&appid={self.key}"
            else:
                URL = f"{self.api}/weather?zip={zip}&appid={self.key}"
            if units is not None:
                units = units.lower()
                if units in self.units:
                    URL += f"&units={units}"
            if language is not None:
                language = language.lower()
                if language in self.langs.keys():
                    URL += f"&lang={language}"
                elif language in self.langs.values():
                    for lang in self.langs:
                        if self.langs[lang] == language:
                            URL += f"&lang={lang}"
                            break
            DATA = requests.get(url = URL).json()
            if DATA["cod"] == 200:
                if type is not None:
                    if type.lower() in ["dict", "json"]:
                        return DATA
                else:
                    ConvertToJSON.__init__(self, DATA)
                    return self._toOMW()
            else:
                return Error(code = DATA["cod"], message = DATA["message"])

        except:
            raise APIFetchError
