import random
import string
import requests
import unittest

# Generate random username and password
def random_string(length):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_credentials():
    username = random_string(10)
    password = random_string(15)
    return username, password

BASE_URL = 'http://127.0.0.1:8080'
REGISTER_URL = BASE_URL + '/register'

class Base_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.username, cls.password = generate_credentials()
        data = {'username': cls.username, 'password': cls.password}
        response = requests.post(REGISTER_URL, json=data)
        cls.token = response.json().get("token")
        cls.status_code = response.status_code