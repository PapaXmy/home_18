from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self):
        return self.genre_dao.get_all()

    def get_genre_one(self, gid):
        return self.genre_dao.get_one(gid)

    def create(self, genre_data):
        return self.genre_dao.create(genre_data)

    def update(self, genre_data):
        self.genre_dao.update(genre_data)

    def delete(self, did):
        self.genre_dao.delete(did)