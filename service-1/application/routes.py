from flask import render_template
import requests

from application import app, db
from application.models import Chances

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/index', methods=['GET'])
def index():
    # Gets a shot
    shot = requests.get("http://localhost:5001/shooter")
    # Gets the dive
    dive = requests.get("http://localhost:5002/goalie")
    # Gets the chance
    chance = requests.get("http://localhost:5003/chance")

    db_data = Chances(shot=shot.text, dive=dive.text, chance=chance.text)
    db.session.add(db_data)
    db.session.commit()
    #score_record=db_data.query.all()

    return render_template('index.html', shot=shot.text, dive=dive.text, chance=chance.text)

@app.route('/read', methods=['GET'])
def read():
    heading = ('ID', 'Shot', 'Dive', 'Chance')
    all_chances = Chances.query.all()
    chance = Chances.id
    return render_template('read.html', heading=heading,
                           all_chances=all_chances, chance=chance)
