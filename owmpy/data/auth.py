"""Authenticate OpenWeatherMap API key"""

import requests

class AuthenticateAPIKey(object):
    """Class for authenticating OpenWeatherMap API key

    Attributes
    ----------
    key : str
        OpenWeatherMap API key

    Methods
    -------
    _authenticate()
        Verify the API key
    """
    def __init__(self, key: str):
        """
        Parameters
        ----------
        key : str
            OpenWeatherMap API key
        """
        self.key = key
        self.api = "https://api.openweathermap.org/data/2.5"
        self.units = ["standard", "metric", "imperial"]
        self.langs = {
            "af": "afrikaans",
            "al": "albanian",
            "ar": "arabic",
            "az": "azerbaijani",
            "bg": "bulgarian",
            "ca": "catalan",
            "cz": "czech",
            "da": "danish",
            "de": "german",
            "el": "greek",
            "en": "english",
            "es": "spanish",
            "eu": "basque",
            "fa": "persian",
            "fi": "finnish",
            "fr": "french",
            "gl": "galician",
            "he": "hebrew",
            "hi": "hindi",
            "hr": "croatian",
            "hu": "hungarian",
            "id": "indonesian",
            "it": "italian",
            "ja": "japanese",
            "kr": "korean",
            "la": "latvian",
            "lt": "lithuanian",
            "mk": "macedonian",
            "no": "norwegian",
            "nl": "dutch",
            "pl": "polish",
            "pt": "portuguese",
            "ro": "romanian",
            "ru": "russian",
            "se": "swedish",
            "sv": "swedish",
            "sk": "slovak",
            "sl": "slovenian",
            "sp": "spanish",
            "sr": "serbian",
            "th": "thai",
            "tr": "turkish",
            "ua": "ukrainian",
            "uk": "ukranian",
            "vi": "vietnamese",
            "zu": "Zulu"
        }

    def _authenticate(self) -> bool:
        """Authenticate the API key by making a dummy request

        Returns
        -------
        bool
            True if API key exists else False
        """
        try:
            DATA = requests.get(
                url = f"{self.api}/weather?q=delhi&appid={self.key}"
            ).json()
            if DATA["cod"] == 200:
                return True
            else:
                return False

        except:
            return False
