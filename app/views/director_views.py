from flask_restx import Resource, Namespace
from app.container import director_sevice
from app.dao.model.director_model import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_directors = director_sevice.get_directors()

        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:director_id>')
class MovieView(Resource):
    def get(self, director_id):
        director = director_sevice.get_director_one(director_id)

        return director_schema.dump(director)