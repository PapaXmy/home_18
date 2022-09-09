from app.dao.model.director_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_data):
        director = Director(**director_data)
        self.session.add(director)
        self.session.commit()

        return director

    def update(self, director_id):
        director = self.get_one(director_id.get("id"))
        director.name = director_id.get("name")

        self.session.add(director)
        self.session.commit()

    def delete(self, director_id):
        director = self.get_one(director_id)
        self.session.delete(director)
        self.session.commit()
