import os
import sys

import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.box.box import Box

from main.race.race_view import Race
from main.race.race_service import RaceService
from main.race.race_view import RaceView


class TestRace(unittest.TestCase):
    """Test methods in race package
    
    Methods list:
    - random_box_position:
    - display race
    """
    def test_0_random_box_position_method(self):
        box_qty = 4
        race_length = 12
        boxes_pos = RaceService.random_box_position(box_qty, race_length)
        self.assertIsNotNone(boxes_pos)
        self.assertGreater(boxes_pos[1], boxes_pos[0])

    def test_1_display_race_method(self):
        race_length = 12
        box_1 = Box(1, 'mystery', 'event1', 'action1', 1)
        box_2 = Box(5, 'mystery', 'event2', 'action2', 1)
        box_3 = Box(6, 'danger', 'event1', 'action1', 1)
        box_4 = Box(9, 'danger', 'event1', 'action1', 1)
        boxes = [box_1, box_2, box_3, box_4]
        race = Race(race_length, boxes)
        print("\nDisplay race")
        RaceView.display_race(race)

if __name__ == '__main__':
    unittest.main(verbosity=2)