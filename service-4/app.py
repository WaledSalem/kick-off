from flask import Flask, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chance():
    # Gets an shoot
    shoot = requests.get("http://localhost:5001/")
    # Gets the dive
    dive = requests.get("http://localhost:5002/")
    chance = None
    if shoot == "Left" and dive == "Left":
        chance = "63%"
    elif shoot == "Left" and dive == "Middle":
        chance = "100%"
    elif shoot == "Left" and dive == "Right":
        chance = "94%"
    elif shoot == "Middle" and dive == "Left":
        chance = "81%"
    elif shoot == "Middle" and dive == "Middle":
        chance = "0%"
    elif shoot == "Middle" and dive == "Right":
        chance = "89%"
    elif shoot == "Right" and dive == "Left":
        chance = "90%"
    elif shoot == "Right" and dive == "Middle":
        chance = "100%"
    elif shoot == "Right" and dive == "Right":
        chance = "44%"
    return Response(chance, mimetype="text/plain") 


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)