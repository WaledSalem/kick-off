from flask import render_template
import requests

from application import app

@app.route('/', methods=['GET'])
def index():
    # Gets a shot
    shot = requests.get("http://localhost:5001/shooter")
    # Gets the dive
    dive = requests.get("http://localhost:5002/goalie")
    # Gets the chance
    chance = requests.get("http://localhost:5003/chance")

    return render_template('index.html', shot=shot.text, dive=dive.text, chance=chance.text)

