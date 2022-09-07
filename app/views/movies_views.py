from flask import request

from app.container import movie_service
from app.dao.model.movie_model import MovieSchema, Movie
from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')

        filters = {
            "director_id": director,
            "genre": genre,
            "year": year
        }

        all_movies = movie_service.get_movies_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        movies_json = request.json
        movie = movie_service.create(movies_json)
        return "Фильм добавлен", 201, {"location": f"/movies/{movie.id}"}

@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        movie = movie_service.get_movies_one(movie_id)
        return movie_schema.dump(movie)

    def put(self, movie_id):
        movie_json = request.json
        movie_json["id"] = movie_id
        movie_service.update(movie_json)

        return "Данные фильма обновлены"

    def patch(self, movie_id):
        movie_json = request.json
        movie_json["id"] = movie_id
        movie_service.update_partial(movie_json)

        return "Данные фильма обновлены"

    def delete(self, movie_id):
        movie_service.delete(movie_id)

        return "Фильм удален", 204
