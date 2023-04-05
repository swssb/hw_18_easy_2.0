from flask_restx import Namespace, Resource

from models import Genre, GenreSchema
from setup_db import db

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = db.session.query(Genre).all()
        print(genres)
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = Genre.query.get(id)
        return genre_schema.dump(genre), 200
