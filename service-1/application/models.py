from application import db

class Chances(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shot = db.Column(db.String(20), nullable=False)
    dive = db.Column(db.String(20), nullable=False)
    chance = db.Column(db.String(20), nullable=False)