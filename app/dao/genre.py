from app.dao.model.genre_model import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_data):
        genre = Genre(**genre_data)
        self.session.add(genre)
        self.session.commit()

        return genre

    def update(self, genre_id):
        genre = self.get_one(genre_id.get("id"))
        genre.name = genre_id.get("name")

        self.session.add(genre)
        self.session.commit()

    def delete(self, genre_id):
        genre = self.get_one(genre_id)
        self.session.delete(genre)
        self.session.commit()