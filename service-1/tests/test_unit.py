from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestResponse(TestBase):
    def test_shooter(self):
    # We will mock request.get and request.post
        with patch("requests.get") as g:
            url = 'http://localhost:5001/shooter'
            g.return_value.text = "Left"
            response = self.client.get(url_for("index"))
            self.assertIn(b'The Shooter direction is Left', response.data)

class TestRead(TestBase):
    def test_Read_get(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
