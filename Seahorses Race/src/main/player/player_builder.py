from main.player.player import Player
from main.seahorse.seahorse import Seahorse


class PlayerBuilder:
    
    def create_player(self, name: str, player_type: str = "manual") -> Player:
        seahorses = [Seahorse(seahorse_id) for seahorse_id in range(1, 4)]
        return Player(name, seahorses, player_type)