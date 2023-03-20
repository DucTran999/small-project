import random
import secrets

from race.race import Race

from box.box import Box
from box.box_builder import BoxBuilder


class RaceBuilder:
    """This class responsible for creating a Race
    
    The RaceBuilder class will call BoxBuilder's method while building the race.
    """
    def __init__(self) -> None:
        """RaceBuilder constructor
        
        instance state:
        - box_builder: help race builder creating box.
        """
        self.box_builder = BoxBuilder()
    
    def create_race(self, steps: int=12) -> Race:
        """Creating a Race
        
        Workflow:
        - Choose the random position where the box will placed.
        - For each position create a box with a random event.
        
        Sub-method:
        - generate_box_quantity_randomly.
        - generate_box_positions_randomly.
        - generate_boxes.
        """
        boxes_qty = self.generate_box_quantity_randomly(steps//2)
        boxes_positions = self.generate_box_positions_randomly(boxes_qty, steps)
        boxes = self.generate_boxes(boxes_positions)
        return Race(steps, boxes_positions, boxes)
    
    def generate_box_quantity_randomly(self, maximum: int) -> int:
        # the maximum number of boxes is half of the race's steps
        return secrets.choice(range(1,maximum + 1))

    def generate_box_positions_randomly(self, quantity: int, steps: int) -> list[int]:
        positions = list(range(1, steps + 1))
        boxes_positions = random.sample(positions, quantity)
        return sorted(boxes_positions)
    
    def generate_boxes(self, boxes_positions: list[int]) -> list[Box]:
        boxes = []
        for position in boxes_positions:
            event = self.box_builder.choice_event_for_create_box()
            box = self.box_builder.create_box(position, event)
            boxes.append(box)
        return boxes