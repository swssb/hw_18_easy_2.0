from flask_restx import Namespace, Resource

from models import Director, DirectorSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        directors = Director.query.all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id):
        director = Director.query.get(id)
        return director_schema.dump(director), 200
