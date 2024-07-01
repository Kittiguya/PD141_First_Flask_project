from flask import abort
from flask.views import MethodView
from schemas import GenreSchemas, GenreWithPostsSchemas
from . import bp

from models.genres_models import GenresModel


@bp.route('/genres')
class GenresList(MethodView):

    @bp.response(200, GenreSchemas(many=True))
    def get(self):
        return GenresModel.query.all()


    @bp.arguments(GenreWithPostsSchemas)
    @bp.response(201, GenreSchemas)
    def post(self, data):
        try:
            genre = GenresModel()
            
            genre.save_genre()
            return genre
        except:
            abort(400, message="genre already exists")
        

    @bp.arguments(GenreSchemas)
    @bp.response(201, GenreWithPostsSchemas)
    def update_genres(self, data, id):
        genre = GenresModel.query.get(id)
        if genre:
            genre.from_dict(data)
            genre.save_genre()
            return {'message' : "genre updated"}, 201
        else:
            abort(300, message="not a valid genre")


    def delete_genre(self, id):
        genre = GenresModel.query.get(id)
        if genre:
            genre.del_user()
            return {"message" : "user has been deleted"}, 200
        abort(400, message="not a valid genre")