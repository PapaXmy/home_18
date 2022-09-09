from app.dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies_all(self, filters):
        if filters.get("director_id") is not None:
            movie = self.movie_dao.get_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movie = self.movie_dao.get_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movie = self.movie_dao.get_year(filters.get("year"))
        else:
            movie = self.movie_dao.get_all()

        return movie

    def get_movies_one(self, mid):
        return self.movie_dao.get_one(mid)

    def create(self, movie_data):
        return self.movie_dao.create(movie_data)

    def update(self, movie_data):
        mid = movie_data.get("id")
        movie = self.get_movies_one(mid)

        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")

        self.movie_dao.update(movie)

    def update_partial(self, movie_data):
        mid = movie_data.get("id")
        movie = self.get_movies_one(mid)

        if "title" in movie_data:
            movie.title = movie_data.get("title")
        if "description" in movie_data:
            movie.description = movie_data.get("description")
        if "trailer" in movie_data:
            movie.trailer = movie_data.get("trailer")
        if "year" in movie_data:
            movie.year = movie_data.get("year")
        if "rating" in movie_data:
            movie.rating = movie_data.get("rating")

        self.movie_dao.update(movie)

    def delete(self, mid):
        self.movie_dao.delete(mid)
