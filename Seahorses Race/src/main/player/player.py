from seahorse.seahorse import Seahorse


class Player:
    """This class represent a player in game"""
    def __init__(self, name: str, 
                 seahorses: list[Seahorse],
                 turn_remain: int = 1,
                 turns_total: int = 0
                 ) -> None:
        """Player constructor
        
        Param:
        - name: player name
        - seahorses: player's seahorses
        - turn_remain: number of dice roll. This attribute will be affected by box
        event.
        - turn_total: total turn players used for moving all seahorses to finish.
        """
        self.__name = name
        self.__seahorses = seahorses
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