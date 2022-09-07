from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.movies_views import movie_ns
from app.views.genres_views import genre_ns
from app.views.director_views import director_ns

# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)

app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(port=4776)

