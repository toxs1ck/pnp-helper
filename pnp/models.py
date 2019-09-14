from datetime import datetime
from pnp import db, login_manager
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


permission_table = db.Table('permission', Base.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('roles_id', db.Integer, db.ForeignKey('roles.id'))
)


class User(db.Model, UserMixin):
    # ID for unique identification
    id = db.Column(db.Integer, primary_key=True)

    # user registration information
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # user information
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(40), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    # game related information
    joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    games = db.relationship('Game', backref='author', lazy=True)

    # permissions
    role = db.relationship("role", secondary=permission_table)

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"


class Role(db.Model):
    # ID for unique identification
    id = db.Column(db.Integer, primary_key=True)

    # role information
    name = db.Column(db.String(20), unique=True, nullable=False)

    # users
    users = db.relationship('User', backref='role', lazy=True)


class Game(db.Model):
    # ID for unique identification
    id = db.Column(db.Integer, primary_key=True)

    # game information
    name = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text)

    # user who created the game
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # characters of the game
    character = db.relationship('Character', backref='game', lazy=True)

    def __repr__(self):
        return f"Game('{self.name}, {self.created}')"


class Character(db.Model):
    # ID for unique identification
    id = db.Column(db.Integer, primary_key=True)

    # character information
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(40), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    race = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.String(30), nullable=False)
    height = db.Column(db.String(30), nullable=False)
    hair = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(30), nullable=False)

    # game information
    played_in = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

    def __repr__(self):
        return f"Character('{self.first_name}, {self.second_name}, {self.game}')"