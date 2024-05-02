from flask import abort
from flask.views import MethodView
from schemas import GamesSchemas, GamesWithPostsSchemas
from . import bp

from models.games_models import GamesModel


@bp.route('/games')
class GamesList(MethodView):

    @bp.response(200, GamesSchemas(many=True))
    def get(self):
        return GamesModel.query.all()
    
    @bp.response(201, GamesWithPostsSchemas)
    @bp.arguments(GamesSchemas)
    def post(self):
        try:
            games = GamesModel()
            
            games.save_user()
            return games
        except:
            abort(400, message="Game already exists, please try a different one!")

    @bp.response(200, GamesWithPostsSchemas)
    @bp.arguments(GamesSchemas)
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
                
            