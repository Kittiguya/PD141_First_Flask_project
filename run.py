from flask import Flask, request

app = Flask(__name__)

users = {
    1:{
        'id' : 1,
        'username' : 'Kittiguya',
        'email' : 'Robinwalk31@gmail.com'
    }, 
    2:{
        'id' : 2,
        'username' : 'Goodsoldier1p1_7',
        'email' : 'soldier1p1@gmail.com'
    }
}


games = {
    1: {
        'name' : 'Rust',
        'Studio' : 'Facepunch',
        'Description' : 'Harcore FPS Survival game, Youre not safe even when you are'
    },
    2: {
        'name' : 'Rainbow 6 Siege',
        'Studio' : 'Ubisoft',
        'Description' : 'Search and destroy style 5v5 tactical FPS game'
    },
    3: {
        'name' : 'Counter-Strike 2',
        'Studio' : 'Valve',
        'Description' : 'Defuse the bomb, or rescue the hostage style game modes. 6v6 tactical FPS'
    },
    4: {
        'name' : 'World of Warcraft',
        'Studio' : 'Blizzard/Activision/Microsoft',
        'Description' : 'MMORPG with an emphasis on pure end game content. Or collectible farming. Kind of bad nowadays'
    },
    5: {
        'name' : 'League of Legends',
        'Studio' : 'Riot games',
        'Description' : '5v5 top down view game. Fight over tower objectives and destroy the enemy\'s nexus to win!'
    }
}

@app.route('/')
def land():
    return {
        "Welcome!! These are game genres i play" : "You'll see I offer a little information on these games here"
    }

@app.route('/FPS/')
def create():
    return {
        "So you think you got aim like James Bond?" : "You came to the right place kid!"
    }

@app.route('/MMORPG/')
def read():
    return {
        "You've opted to go on quests in search of treasures and glory," : "Here you will find the most fantastic places to acquire all your wishes!"
    }


@app.route('/SURVIVAL/')
def update():
    return {
        "Living in the real world isn't enough? Still more to desire?" : "Over here, we teach you the basics of all survival games and send you on your way to be a strong survivalist"
    }


@app.route('/MOBA/')
def delete():
    return {
        "So MOBA's intrigue you. You're special 100%." : "Everyone has different tastes, You can dine with the others like yourself."
    }

@app.route('/users')
def get_users():
    return {
        'users' : list(users.values())
    }

@app.route('/games')
def get_games():
    return {
        'games' : list(games.values())
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


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    users[data['id']] = data
    return {
        'User created successfully' : users[data['id']]
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




@app.route('/games', methods=['POST'])
def create_game():
    data = request.get_json()
    print(data)
    games[data['name']] = data
    return {
        'Game added successfully' : games[data['name']]
    }

@app.route('/games', methods=['PUT'])
def update_game():
    data = request.get_json()
    if data['name'] in games:
        games[data['name']] = data 
        return {
            'Game updated' : games[data['name']]
        }
    return {
        'error' : 'No game found with that name'
    }

@app.route('/games', methods=['DELETE'])
def delete_game():
    data = request.get_json()
    if data['name'] in games:
        del games[data['name']]
        return {
            'Game has been deleted' : f"data{['name']} is no longer here."
        }
    return {
        'error' : "can't delete what isn't there!"
    }

app.run()