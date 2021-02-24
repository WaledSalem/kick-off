from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_chance_left(self):
        with patch("requests.get") as g:
            url = 'http://localhost:5001/shooter'
            url = 'http://localhost:5002/goalie'
            g.return_value.text = "Left"               
            
            response = self.client.get(url_for("chance"))
            self.assertIn(b'63%', response.data)

    def test_chance_middle(self):
        with patch("requests.get") as g:
            url = 'http://localhost:5001/shooter'
            url = 'http://localhost:5002/goalie'
            g.return_value.text = "Middle"               
            
            response = self.client.get(url_for("chance"))
            self.assertIn(b'0%', response.data)

    def test_chance_right(self):
        with patch("requests.get") as g:
            url = 'http://localhost:5001/shooter'
            url = 'http://localhost:5002/goalie'
            g.return_value.text = "Right"               
            
            response = self.client.get(url_for("chance"))
            self.assertIn(b'44%', response.data)
