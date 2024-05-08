from fastapi import FastAPI
from pydantic import BaseModel

api = FastAPI()

players = {
    1: {
        "name": "Rony",
        "age": 29,
        "team": "Palmeiras"
    },
    2: {
        "name": "Gustavo Gomez",
        "age": 31,
        "team": "Palmeiras"
    },
    3: {
        "name": "Diego Costa",
        "age": 35,
        "team": "Gremio"
    }
}

class Player(BaseModel):
    name: str
    age: int
    team: str

@api.get("/")
def index():
    return players


@api.get("/players/{id}")
def get_player(id:int):
    return players[id]


@api.get('/players')
def get_teams(team:str):
    return [player for player in players.values() if player['team'] == team]


@api.post('/players')
def create_player(player: Player):
    player_id = len(players) + 1
    players[player_id] = player
    return players[player_id]


@api.delete('/players/{id}')
def delete_player(id:int):
    del players[id]
    return players


@api.put('/players/{id}')
def update_player(id:int, player: Player):
    players[id] = player
    return players