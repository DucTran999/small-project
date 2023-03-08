from player.player import Player

from die.die_controller import DieController

from race.race import Race

class Match:
    """This class represent a match in game"""  
    def __init__(self, players: list[Player], die_c: DieController, race: Race) -> None:
        self.players = players
        self.die_c = die_c
        self.race = race
    