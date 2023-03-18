from box.box import Box

class Race:
    """This class describe a race"""
    def __init__(self, steps: int, boxes_positions: list[int],  boxes: list[Box]):
        """Race constructor
        
        Params:
        - steps: The length of the race is measured in steps.
        - boxes_positions: List of locations where boxes will be placed. It is 
        more convenient to check whether the seahorse has a box.
        - boxes: list box will be distributed on the race lane.
        """
        self.__steps = steps
        self.__boxes_positions = boxes_positions
        self.__boxes = boxes
    
    @property
    def steps(self) -> int:
        return self.__steps

    @property
    def boxes_positions(self) -> list[int]:
        return self.__boxes_positions
    
    @property
    def boxes(self) -> list[Box]:
        return self.__boxes