from flask import Flask, abort, jsonify, request
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies
from schemas import UserSchema, UserWithPostsSchemas
from . import bp

from app import app
from models.users_models import UserModel





@bp.route('/users')
class UserList(MethodView):

    @bp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    # @jwt_required
    @bp.arguments(UserSchema)
    @bp.response(201, UserWithPostsSchemas)
    def post(self, data):
        print(data)
        try:
            user = UserModel()
            user.from_dict(data)
            user.save_user()
            return user
        except:
            abort(400, message="username or email already taken, please try a different one!")
   

@bp.route('/user/<int:id>')
class User(MethodView):

    
    @bp.response(200, UserWithPostsSchemas)
    def get(self, id):
        user = UserModel.query.get(id)
        if user:
            return user
        else: 
            abort(400, message="not a valid user")

    @jwt_required
    @bp.arguments(UserSchema)
    @bp.response(200, UserWithPostsSchemas)
    def put(self, data, id):
        user = UserModel.query.get(id)
        if user:
            user.from_dict(data)
            user.save_user() 
            return {"message" : "user updated"}, 201
        else:
            abort(400, message="not a valid user")

    
    def delete_user():
        user = UserModel.query.get(id)
        if user:
            user.del_user()
            
            return {"message" : "user has been deleted"}, 200
        abort(400, message="not a valid user")
        



@bp.post('/login')
def login():
    login_data=request.get_json()
    username = login_data['username']

    user = UserModel.query.filter_by(username = username).first()
    if user and user.check_password(login_data['password']):
        access_token = create_access_token(identity=user.id)
        return {'access_token' : access_token}
    abort(400, message="invalid user data")


@bp.post('/logout')
def logout():
    response = jsonify({"message" : "logout successful"})
    unset_jwt_cookies(response)
    return response