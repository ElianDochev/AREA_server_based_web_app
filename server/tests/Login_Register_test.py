import unittest
import requests
from Base_test import Base_test

BASE_URL = 'http://127.0.0.1:8080'
REGISTER_URL = BASE_URL + '/register'
LOGIN_URL = BASE_URL + '/login'


class TestAPI(Base_test, unittest.TestCase):
    def test_register(self):
        # sucessful registration
        self.assertEqual(self.status_code, 201, "Failed to register user")

        # Attempt to register the same user again
        register_data = {'username': self.username, 'password': self.password}
        response = requests.post(REGISTER_URL, json=register_data)
        self.assertEqual(response.status_code, 409, "Registered the same user twice")

    def test_login(self):
        # Attempt to log in with the registered username and password
        login_data = {'username': self.username, 'password': self.password}
        response = requests.post(LOGIN_URL, json=login_data)
        self.assertEqual(response.status_code, 200, "Failed to log in user")
        self.assertIn('token', response.json(), "token not found in response")
        token = response.json().get('token')

        # Attempt to log in with an invalid username and password
        wrong_login_data = {'username': self.username, 'password': 'wrong_password'}
        response = requests.post(LOGIN_URL, json=wrong_login_data)
        self.assertEqual(response.status_code, 401, "Logged in with invalid credentials")

        # attempt to log in with JWT token
        headers = {'Authorization': 'Bearer ' + token}
        response = requests.post(LOGIN_URL, headers=headers, json={})
        self.assertEqual(response.status_code, 200, "Failed to log in user with token")
        with open('token.txt', 'w') as f:
            f.write(token)

