from flask import Flask
from flask_smorest import Blueprint, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models.users_models import UserModel
from models.genres_models import GenresModel
from models.games_models import GamesModel

from resources.games import bp as games_bp
app.register_blueprint(games_bp)

from resources.genres import bp as genres_bp
app.register_blueprint(genres_bp)

from resources.user import bp as users_bp
app.register_blueprint(users_bp)


from resources.games import routes
from resources.genres import routes
from resources.user import routes