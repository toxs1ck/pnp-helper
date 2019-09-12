from datetime import datetime
from pnp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(40), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    games = db.relationship('Game', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character = db.relationship('Character', backref='game', lazy=True)

    def __repr__(self):
        return f"Game('{self.name}, {self.created}')"


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(40), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    race = db.Column(db.String(50))
    role = db.Column(db.String(50))
    gender = db.Column(db.String(30))
    age = db.Column(db.Integer)
    weight = db.Column(db.String(30))
    height = db.Column(db.String(30))
    hair = db.Column(db.String(50))
    body = db.Column(db.String(30))
    played_in = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

    def __repr__(self):
        return f"Character('{self.first_name}, {self.second_name}, {self.game}')"