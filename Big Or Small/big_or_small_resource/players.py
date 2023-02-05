class Player:
    """A class to manage the player infomation"""

    def __init__(self, name: str) -> None:
        """Initialize the players and set their relevant information."""
        self.__name = name
        self.__heart = 3
        # The closest round that the player won.
        self.__round_passed = 0
        # The time that the player loses the game.
        self.__end_time = ''

    def __repr__(self) -> str:
        """Formating the player's inforamtion to a string."""
        player_info = (f"Player: {self.__name}, "
                       f"Rounds: {self.__round_passed}, "
                       f"Finished: {self.__end_time}")
        return player_info
    
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.name = name 
    
    def get_heart(self) -> None:
        return self.__heart

    def set_rounds_passed(self, rounds: int) -> None:
        self.__round_passed = rounds
    
    def set_end_time(self, end_time: str) -> None:
        self.__end_time = end_time
    
    def lose_heart(self) -> None:
        """Lose 1 heart when player guess wrong""" 
        self.__heart -= 1