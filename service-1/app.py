from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Gets an shoot
    shoot = requests.get("http://localhost:5001/")
    # Gets the dive
    #dive = requests.get("http://localhost:5001/goalie")

    #return render_template('index.html', shoot=shoot.text, dive=dive.text)
    return render_template('index.html', shoot=shoot.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)