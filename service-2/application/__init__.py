from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/shooter', methods=['GET'])
def shooter():
    directions = ["Left", "Middle", "Right"]
    return Response(random.choices(directions), mimetype="text/plain")

