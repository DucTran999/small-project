from seahorse.seahorse import Seahorse


class Player:
    """This class represent a player in game"""
    def __init__(self, name: str, 
                 seahorses: list[Seahorse],
                 player_type: str,
                 turn_remain: int = 1,
                 turns_total: int = 0
                 ) -> None:
        """Player constructor
        
        Param:
        - name: player name. default: computer
        - seahorses: player's seahorses
        - player_type: default manual. Other type is auto use for creating computer
        - turn_remain: number of dice roll. This attribute will be affected by box
        event.
        - turn_total: total turn players used for moving all seahorses to finish.
        player.
        """
        self.__name = name
        self.__seahorses = seahorses
        self.__player_type = player_type
        self.__turn_remain = turn_remain
        self.__turns_total = turns_total
    
    def __repr__(self) -> str:
        return f"Player: {self.name}"
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def seahorses(self) -> list[Seahorse]:
        return self.__seahorses
    
    @property
    def player_type(self):
        return self.__player_type
    
    @player_type.setter
    def player_type(self, new_type: str):
        self.__player_type = new_type
   
    @property
    def turn_remain(self) -> int:
        return self.__turn_remain
    
    @turn_remain.setter
    def turn_remain(self, new_qty: int) -> None:
        self.__turn_remain = new_qty
    
    @property
    def turns_total(self) -> int:
        return self.__turns_total
    
    @turns_total.setter
    def turns_total(self, turn_qty: int) -> None:
        self.__turns_total = turn_qty
    
    def tracking_turns(self):
        self.__turns_total += 1
    