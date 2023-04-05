from flask import request
from flask_restx import Namespace, Resource

from models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id_arg = request.args.get('director_id')
        genre_id_arg = request.args.get('genre_id')
        year_arg = request.args.get('year')
        if director_id_arg:
            movies = Movie.query.filter(Movie.director_id == director_id_arg).all()
        elif genre_id_arg:
            movies = Movie.query.filter(Movie.genre_id == genre_id_arg).all()
        elif year_arg:
            movies = Movie.query.filter(Movie.year == year_arg).all()
        else:
            movies = Movie.query.all()

        return movies_schema.dump(movies), 200

    def post(self):
        req = request.get_json()
        new_movie = Movie(**req)
        db.session.add(new_movie)
        db.session.commit()
        return "", 201


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = Movie.query.get(id)
        if movie:
            return movie_schema.dump(movie), 200
        else:
            return 'invalid id', 404

    def put(self, id):
        req = request.get_json()
        movie = Movie.query.get(id)
        if not movie:
            return 'invalid id', 404
        movie.name = req.get('name')
        movie.title = req.get('title')
        movie.description = req.get('description')
        movie.trailer = req.get('trailer')
        movie.year = req.get('year')
        movie.rating = req.get('rating')
        movie.genre_id = req.get('genre_id')
        movie.director_id = req.get('director_id')
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, id):
        movie = Movie.query.get(id)
        db.session.delete(movie)
        db.session.commit()
        return '', 204
