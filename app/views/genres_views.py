from app.container import genre_service
from app.dao.model.genre_model import GenreSchema
from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_genres = genre_service.get_genres()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:genre_id>')
class MovieView(Resource):
    def get(self, genre_id):
        genre = genre_service.get_genre_one(genre_id)
        return genre_schema.dump(genre)