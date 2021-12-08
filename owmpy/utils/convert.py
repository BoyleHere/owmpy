from typing import Union
from owmpy.data.models import OWM

class ConvertToJSON(object):
    def __init__(self, data: dict):
        self.data = data

    def _toOMW(self) -> Union[bool, OWM]:
        try:
            RESULT = OWM(
                coords = OWM.Coords(
                    latitude = self.data["coord"]["lat"],
                    longitude = self.data["coord"]["lon"]
                ),
                weather = OWM.Weather(
                    main = self.data["weather"][0]["main"],
                    description = self.data["weather"][0]["description"]
                ),
                main = OWM.Main(
                    temperature = self.data["main"]["temp"],
                    feels_like = self.data["main"]["feels_like"],
                    minimum = self.data["main"]["temp_min"],
                    maximum = self.data["main"]["temp_max"],
                    pressure = self.data["main"]["pressure"],
                    humidity = self.data["main"]["humidity"],
                    sea_level = self.data["main"]["sea_level"] \
                        if "sea_level" in self.data["main"] else None,
                    ground_level = self.data["main"]["grnd_level"] \
                        if "grnd_level" in self.data["main"] else None
                ),
                visibility = self.data["visibility"],
                wind = OWM.Wind(
                    speed = self.data["wind"]["speed"] if "wind" in self.data \
                        and "speed" in self.data["wind"] else None,
                    degree = self.data["wind"]["deg"] if "wind" in self.data \
                        and "degree" in self.data["wind"] else None,
                    gust = self.data["wind"]["gust"] if "wind" in self.data \
                        and "gust" in self.data["wind"] else None
                ) if "wind" in self.data else None,
                clouds = self.data["clouds"]["all"],
                rain = OWM.Rain(
                    one_hour = self.data["rain"]["1h"] if "rain" in self.data \
                        and "1h" in self.data["rain"] else None,
                    three_hours = self.data["rain"]["3h"] if "rain" in self.data \
                        and "3h" in self.data["rain"] else None
                ) if "rain" in self.data else None,
                snow = OWM.Snow(
                    one_hour = self.data["snow"]["1h"] if "snow" in self.data \
                        and "1h" in self.data["snow"] else None,
                    three_hours = self.data["snow"]["3h"] if "snow" in self.data \
                        and "3h" in self.data["snow"] else None
                ) if "snow" in self.data else None,
                sys = OWM.Sys(
                    country = self.data["sys"]["country"] \
                        if "country" in self.data["sys"] else None,
                    sunrise = self.data["sys"]["sunrise"],
                    sunset = self.data["sys"]["sunset"]
                ),
                datetime = self.data["dt"],
                timezone = self.data["timezone"],
                id = self.data["id"],
                name = self.data["name"]
            )
            return RESULT

        except:
            return False
