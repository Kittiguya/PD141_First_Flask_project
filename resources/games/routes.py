from flask import request


from . import bp
from db import games




@bp.route('/games')
def get_games():
    return {
        'games' : list(games.values())
    }


@bp.route('/games', methods=['POST'])
def create_game():
    data = request.get_json()
    print(data)
    games['name'] = data
    return {
        'Game added successfully' : games['name']
    }

@bp.route('/games', methods=['PUT'])
def update_game():
    data = request.get_json()
    if data['name'] in games:
        games['name'] = data 
        return {
            'Game updated' : games['name']
        }
    return {
        'error' : 'No game found with that name'
    }

@bp.route('/games', methods=['DELETE'])
def delete_game():
    data = request.get_json()
    if 'name' in games:
        del games['name']
        return {
            'Game has been deleted' : f"Game {data}."
        }
    return {
        'error' : "can't delete what isn't there!"
    }
