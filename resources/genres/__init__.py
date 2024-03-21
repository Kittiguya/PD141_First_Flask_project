from flask_smorest import Blueprint

bp = Blueprint("genres", __name__, description="Routes for genres")

from . import routes