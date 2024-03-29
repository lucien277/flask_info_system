import datetime
from .model import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


