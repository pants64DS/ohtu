import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def read():
        response = requests.get(self.url).json()

        return [Player(player_dict) for player_dict in response]
