from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/goalie', methods=['GET'])
def goalie():
    directions = ["Left", "Middle", "Right"]
    return Response(random.choices(directions), mimetype="text/plain")
