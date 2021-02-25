from application import db
from application.models import Chances

db.session.remove()
db.drop_all()
db.create_all()