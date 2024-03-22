from flask import Flask
from flask_smorest import Blueprint


app = Flask(__name__)

from resources.games import bp as games_bp
app.register_blueprint(games_bp)

from resources.genres import bp as genres_bp
app.register_blueprint(genres_bp)

from resources.user import bp as users_bp
app.register_blueprint(users_bp)


from resources.games import routes
from resources.genres import routes
from resources.user import routes