from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_shooter(self):
        directions = [b"Left", b"Middle", b"Right"]
        response = self.client.get(url_for('shooter'))
        self.assertIn(response.data, directions)