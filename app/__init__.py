from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask_cors import CORS
                               
from Config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
api = Api(app)
app.config["JWT_SECRET_KEY"] = "SECRET_KEY"
jwt = JWTManager(app)


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from resources.games import bp as games_bp
app.register_blueprint(games_bp)
from resources.genres import bp as genres_bp
app.register_blueprint(genres_bp)
from resources.user import bp as users_bp
app.register_blueprint(users_bp)