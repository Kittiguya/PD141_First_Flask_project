from flask_smorest import Blueprint

bp = Blueprint("games", __name__, description="Routes for games")

from . import routes