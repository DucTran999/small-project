from box.box import Box

class Race:
    """This class describe a race"""
    def __init__(self, length: int, boxes: list[Box]):
        """Race constructor
        
        param:
        - length: race length
        - boxes: list box will be distributed on the race lane.
        """
        self.__length = length
        self.__boxes = boxes
    
    @property
    def length(self) -> int:
        return self.__length

    @property
    def boxes(self) -> list[Box]:
        return self.__boxes