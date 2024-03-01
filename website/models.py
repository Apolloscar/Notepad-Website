from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# how notes will be formatted
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data= db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    # need to pass id of existing user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# How users will be formatted
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # each user must have unique email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    # will have ID of all the notes for the user
    notes = db.relationship('Note')