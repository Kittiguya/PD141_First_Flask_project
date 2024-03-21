from flask import Flask



app = Flask(__name__)


from resources.games import routes
from resources.genres import routes
from resources.user import routes