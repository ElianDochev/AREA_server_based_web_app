import unittest
import datetime
import sys
sys.path.append("..")
from modules.utils.jsonToken import createToken, decodeToken, UnpackToken

class TestYourClass(unittest.TestCase):
    def test_createToken(self):
        username = "test_user"
        short_token = createToken(username, Long=False)
        long_token = createToken(username, Long=True)

        self.assertIsNotNone(short_token)
        self.assertIsNotNone(long_token)
        self.assertNotEqual(short_token, long_token)

    def test_decodeToken(self):
        username = "test_user"
        token = createToken(username, Long=False)

        decoded_payload = decodeToken(token)

        self.assertIsInstance(decoded_payload, dict)
        self.assertEqual(decoded_payload["username"], username)

    def test_UnpackToken(self):
        username = "test_user"
        token = createToken(username, Long=False)
        unpacked_payload = UnpackToken(token, unpack=False)

        self.assertIsInstance(unpacked_payload, dict)
        self.assertEqual(unpacked_payload["username"], username)

        expired_token = createToken(username, Long=False)
        expired_payload = UnpackToken(expired_token, unpack=False)

        self.assertFalse(expired_payload)

if __name__ == '__main__':
    unittest.main()
