from flask import request

from . import bp

from db import genres



@bp.route('/genres')
def get_genres():
    return {
        'genres' : list(genres.values())
    }


@bp.route('/genres', methods=['POST'])
def create_genre():
    data = request.get_json()
    print(data)
    genres[data['genre']] = data
    return {
        'Genre added successfully' : f"data{['genre']} has been added! NICE!"
    }

@bp.route('/genres', methods=['PUT'])
def update_genre():
    data = request.get_json()
    if data['genre'] in genres:
        genres[data['genre']] = data
        return {
            'Genre updated' : f"data{['genre']} has some new info!"
        }
    return {
        'error' : "No genre found with that name"
    }

@bp.route('/genres', methods=['DELETE'])
def delete_genre():
    data = request.get_json()
    if data['genre'] in genres:
        del genres[data['genre']]
        return {
            'Genre has been deleted' : f"data{['genre']} is no longer around"
        }
    return {
        'ERROR OI ERROR' : "You can't delete something that doesn't exist!"
    }
