import unittest
from unittest.mock import patch, MagicMock
import sys
sys.path.append("..")
from modules.database.DBsetup import CreateDb, UserModel, ServiceModel

class TestUserModel(unittest.TestCase):
    def test_user_model_init(self):
        # Test the initialization of the UserModel class.
        username = 'test_user'
        password = 'test_password'
        user = UserModel(username, password)

        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)
        self.assertEqual(user.user_services, {})
        self.assertIsNone(user.github_account_email)
        self.assertFalse(user.is_admin)

    def test_user_model_serialize(self):
        # Test the serialize method of the UserModel class.
        user = UserModel('test_user', 'test_password')
        serialized_data = user.serialize()

        self.assertIsInstance(serialized_data, dict)
        self.assertEqual(serialized_data['username'], 'test_user')
        self.assertEqual(serialized_data['password'], 'test_password')
        self.assertEqual(serialized_data['services'], {})
        self.assertFalse(serialized_data['is_admin'])

if __name__ == '__main__':
    unittest.main()