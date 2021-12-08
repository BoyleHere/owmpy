import os
import unittest
from dotenv import load_dotenv, find_dotenv
from owmpy import AuthenticateAPIKey

load_dotenv(find_dotenv())
KEY = os.getenv("OWM_API_KEY")

class TestAuthenticateAPIKey(unittest.TestCase):
    def test__authenticate(self):
        RESULT = AuthenticateAPIKey(key = KEY)._authenticate()
        self.assertEqual(RESULT, True)
