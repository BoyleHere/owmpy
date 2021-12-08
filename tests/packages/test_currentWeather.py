import os
import unittest
from dotenv import load_dotenv, find_dotenv
from owmpy import CurrentWeatherData

load_dotenv(find_dotenv())
KEY = os.getenv("OWM_API_KEY")

class TestCurrentWeatherData(unittest.TestCase):
    def test_byCityName(self):
        RESULT = CurrentWeatherData(key = KEY).byCityName(city = "delhi")
        self.assertEqual(RESULT.sys.country, "IN")
        self.assertEqual(RESULT.coords.longitude, 77.2167)
        self.assertEqual(RESULT.coords.latitude, 28.6667)
        self.assertEqual(RESULT.id, 1273294)

    def test_byCityID(self):
        RESULT = CurrentWeatherData(key = KEY).byCityID(id = 1273294)
        self.assertEqual(RESULT.sys.country, "IN")
        self.assertEqual(RESULT.coords.longitude, 77.2167)
        self.assertEqual(RESULT.coords.latitude, 28.6667)
        self.assertEqual(RESULT.name, "Delhi")

    def test_byCoords(self):
        RESULT = CurrentWeatherData(key = KEY).byCoords(latitude = 28.6692, longitude = 77.4538)
        self.assertEqual(RESULT.sys.country, "IN")
        self.assertEqual(RESULT.id, 1271308)
        self.assertEqual(RESULT.name, "Ghaziabad")

    def test_byZipCode(self):
        RESULT = CurrentWeatherData(key = KEY).byZipCode(zip = 10001)
        self.assertEqual(RESULT.sys.country, "US")
        self.assertEqual(RESULT.coords.longitude, -73.9967)
        self.assertEqual(RESULT.coords.latitude, 40.7484)
        self.assertEqual(RESULT.id, 0)
        self.assertEqual(RESULT.name, "New York")
