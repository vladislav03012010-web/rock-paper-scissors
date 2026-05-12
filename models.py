from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(50),
        unique=True
    )


class Stats(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    wins = db.Column(
        db.Integer,
        default=0
    )

    losses = db.Column(
        db.Integer,
        default=0
    )

    draws = db.Column(
        db.Integer,
        default=0
    )