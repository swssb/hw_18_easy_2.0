# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)

# Пример
from marshmallow import Schema, fields
from setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(100))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer)
    director_id = db.Column(db.Integer)

class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Integer()
    genre_id = fields.Integer()
    director_id = fields.Integer()

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()

class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()

