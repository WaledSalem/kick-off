from flask import Flask, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/chance', methods=['GET'])
def chance():
    # Gets a shot
    shot_response = requests.get("http://localhost:5001/shooter")
    shot = (shot_response.text)
    # Gets the dive
    dive_response = requests.get("http://localhost:5002/goalie")
    dive = (dive_response.text)
    # Gets shot_dive
    shot_dive = shot + "-" + dive
    chance = None
    if shot_dive == "Left-Left":
        chance = "63%"
    elif shot_dive == "Left-Middle":
        chance = "100%"
    elif shot_dive == "Left-Right":
        chance = "94%"
    elif shot_dive == "Middle-Left":
        chance = "81%"
    elif shot_dive == "Middle-Middle":
        chance = "0%"
    elif shot_dive == "Middle-Right":
        chance = "89%"
    elif shot_dive == "Right-Left":
        chance = "90%"
    elif shot_dive == "Right-Middle":
        chance = "100%"
    elif shot_dive == "Right-Right":
        chance = "44%"
    return Response(chance, mimetype="text/plain") 
