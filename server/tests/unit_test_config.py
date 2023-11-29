import unittest
from unittest.mock import patch
import sys
sys.path.append("..")
from modules.config.config import Config  # Replace 'your_module' with the actual module path
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.db = SQLAlchemy(self.app)

    def test_get_app(self):
        # Test getting the Flask app.
        app = self.config.GetApp()
        self.assertIs(app, self.app)

    def test_get_api(self):
        # Test getting the Flask-RESTPlus API.
        api = self.config.GetApi()
        self.assertIs(api, self.api)

    def test_get_db(self):
        # Test getting the SQLAlchemy database.
        db = self.config.GetDb()
        self.assertIs(db, self.db)

if __name__ == '__main__':
    unittest.main()
