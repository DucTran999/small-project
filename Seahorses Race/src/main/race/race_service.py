import random
import secrets

from race.race import Race

from box.box import Box
from box.box_service import BoxService


class RaceService:
    """This class provides methods to create a race.
    
    The RaceService class will call Box's methods while building the race.
    
    Create race workflow:
    - Choose the random position where the box will appear.
    - For each position create a box with a random event.
    """    
    @classmethod
    def create_race(cls):
        race_length = 12
        boxes = cls.generate_boxes(race_length)
        return Race(race_length, boxes)
    
    @classmethod
    def attract_box_position(cls, boxes: list[Box]) -> list[int]:
        list_pos = list()
        for box in boxes:
            list_pos.append(box.position)
        return list_pos
    
    @classmethod
    def get_box_by_pos(cls, box_pos: int, boxes: list[Box]) -> Box:
        for box in boxes:
            if box_pos == box.position:
                return box
        
    @classmethod
    def generate_boxes(cls, race_length: int) -> list[Box]:
        box_qty = secrets.randbelow(8) # maximum 7 box
        boxes_pos = cls.random_box_position(box_qty, race_length)
        box_events = BoxService.load_box_event()
        boxes = list()
        for pos in boxes_pos:
            boxes.append(BoxService.create_box(pos, box_events))
        return boxes
        
    @classmethod
    def random_box_position(cls, box_qty: int, race_length: int) -> list[int]:
        positions = [*range(1, race_length + 1)]
        box_pos = random.sample(positions, box_qty)
        return sorted(box_pos)
