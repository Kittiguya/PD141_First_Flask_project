from flask import request

from app import app
from db import users



@app.route('/users')
def get_users():
    return {
        'users' : list(users.values())
    }

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    users[data['id']] = data
    return {
        'User created successfully' : users[data['id']]
    }


@app.route('/user/<int:id>')
def get_ind_user(id):
    if id in users:
        return {
            'user' : users[id]
        }
    return {
        'RUH ROH RAGGY' : 'SOMETHING WENT WRONG, WRONG USER ID'
    }


@app.route('/user', methods=['PUT'])
def update_user():
    data = request.get_json()
    if data['id'] in users:
        users[data['id']] = data 
        return {
            'user updated' : users[data['id']]
        }

@app.route('/user', methods=['DELETE'])
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
