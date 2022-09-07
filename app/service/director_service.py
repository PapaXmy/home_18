from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self):
        return self.director_dao.get_all()

    def get_director_one(self, gid):
        return self.director_dao.get_one(gid)

    def create(self, director_data):
        return self.director_dao.create(director_data)

    def update(self, director_data):
        self.director_dao.update(director_data)

    def delete(self, did):
        self.director_dao.delete(did)