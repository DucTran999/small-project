from player.player import Player

from dice.dice_shaker import DiceShaker

from race.race import Race

class Match:
    """This class represent a match in game"""  

    def __init__(self) -> None:
        self.__players: tuple[Player] = None
        self.__dice_shaker = DiceShaker()
        self.__race: Race = None
        self.__state = "not finish"
    
    @property
    def players(self):
        return self.__players
    
    @players.setter
    def players(self, new_players: list[Player]):
        self.__players = new_players
    
    @property
    def dice_shaker(self):
        return self.__dice_shaker
    
    @dice_shaker.setter
    def dice_shaker(self, new_dice_shaker: DiceShaker):
        self.__dice_shaker = new_dice_shaker
        
    @property
    def race(self) -> Race:
        return self.__race

    @race.setter
    def race(self, new_race):
        self.__race = new_race
        
    @property
    def state(self) -> str:
        return self.__state
    
    @state.setter
    def state(self, new_state: str):
        self.__state = new_state
    