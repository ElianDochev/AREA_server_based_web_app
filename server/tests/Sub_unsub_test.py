import unittest
import requests
from Base_test import Base_test

BASE_URL = 'http://127.0.0.1:8080'
SUBSCRIBE_URL = BASE_URL + '/subscribe'
UNSUBSCRIBE_URL = BASE_URL + '/unsubscribe'

class TestSub(Base_test, unittest.TestCase):
    def setUp(self):
        self.service_name = "testSub"

    def test_subscription(self):
        # Subscribe to a service
        headers = {'Authorization': 'Bearer ' + self.token}
        subscribe_data = {"service": self.service_name, "service_args": {"enabled": True}}
        response = requests.post(SUBSCRIBE_URL, json=subscribe_data, headers=headers)
        self.assertEqual(response.status_code, 200,
                         "Failed to subscribe to service error: " + (response.json().get('message')) if response else "no Response")
        self.assertEqual(response.json().get('message'),
                         'Service added successfully.',
                         "Failed to subscribe to service error: " + (response.json().get('message')) if response else "no Response")
    def test_unsub(self):
        headers = {'Authorization': 'Bearer ' + self.token}
        unsubscribe_data = {'service': self.service_name}
        response = requests.post(UNSUBSCRIBE_URL, json=unsubscribe_data, headers=headers)
        self.assertEqual(response.status_code, 200, "Failed to unsubscribe from service error: " + (response.json().get('message')) if response else "no Response")
        self.assertEqual(response.json().get('message'), 'Service removed successfully.',
                        "Failed to unsubscribe from service error: " + (response.json().get('message')) if response else "no Response")