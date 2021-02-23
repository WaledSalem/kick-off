from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Gets a shot
    shot = requests.get("http://localhost:5001/shooter")
    # Gets the dive
    dive = requests.get("http://localhost:5002/goalie")
    # Gets the chance
    chance = requests.get("http://localhost:5003/chance")

    return render_template('index.html', shot=shot.text, dive=dive.text, chance=chance.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)