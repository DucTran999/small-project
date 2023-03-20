class Dice:
    """This class represent a die in game."""
    def __init__(self) -> None:
        """A die always has 6 face"""
        self.__faces = (6,)
    
    @property
    def faces(self) -> tuple[int]:
        return self.__faces