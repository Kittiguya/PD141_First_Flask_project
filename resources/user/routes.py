from flask import request

from . import bp

from db import users



@bp.route('/users')
def get_users():
    return {
        'users' : list(users.values())
    }

@bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    users[data['id']] = data
    return {
        'User created successfully' : users[data['id']]
    }


@bp.route('/user/<int:id>')
def get_ind_user(id):
    if id in users:
        return {
            'user' : users[id]
        }
    return {
        'RUH ROH RAGGY' : 'SOMETHING WENT WRONG, WRONG USER ID'
    }


@bp.route('/user', methods=['PUT'])
def update_user():
    data = request.get_json()
    if data['id'] in users:
        users[data['id']] = data 
        return {
            'user updated' : users[data['id']]
        }

@bp.route('/user', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    if data['id'] in users:
        del users[data['id']]
        return {
            'User has been deleted' : f"data{['id']} is no longer here."
        }
    return {
        'error' : "can't delete what isn't there!"
    }
