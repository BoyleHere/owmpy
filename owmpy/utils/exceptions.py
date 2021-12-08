class APIAuthenticationError(Exception):
    """Raised when the OpenWeatherMap API key is invalid"""
    def __str__(self):
        return "Invalid API key"

class APIFetchError(Exception):
    """Raised when owmpy is unable to fetch data from the API"""
    def __str__(self):
        return "Unable to fetch data from OpenWeatherMap"
