from flask import abort
from flask.views import MethodView
from schemas import GamesSchema, GamesWithPostsSchemas
from . import bp

from app import app
from models.games_models import GamesModel


@bp.route('/games')
class GamesList(MethodView):

    @bp.response(200, GamesSchema(many=True))
    def get(self):
        return GamesModel.query.all()
    
    @bp.arguments(GamesSchema)
    @bp.response(201, GamesWithPostsSchemas)
    def post(self, data):
        try:
            user = GamesModel()
            user.from_dict(data)
            user.save_user()
            return user
        except:
            abort(400, message="Game already exists, please try a different one!")

    @bp.response(200, GamesWithPostsSchemas)
    @bp.arguments(GamesSchema)
    def put(self, data, id):
        games = GamesModel.query.get(id)
        if games:
            games.from_dict(data)
            games.save_game()
            return {"message" : "game updated"}, 201
        else:
            abort(400, message="not a valid user")
    
    def delete_game(self, id):
        games = GamesModel.query.get(id)
        if games:
            games.del_game()

            return {"Game has been deleted" : "Game has been deleted"}, 200
        abort(400, message="not a valid user")
                
            