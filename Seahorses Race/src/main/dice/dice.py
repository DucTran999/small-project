class Dice:
    """This class represent a die in game."""
    def __init__(self) -> None:
        """A die always has 6 face"""
        self.__faces = (1, 2, 3, 4, 5, 6)
    
    @property
    def faces(self) -> tuple[int]:
        return self.__faces