import os
import sys

import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.box.box import Box
from main.box.box_view import BoxView
from main.box.box_service import BoxService

class TestBox(unittest.TestCase):

    box_pos = 1
    box_type = 'mystery'
    box_description = 'some event occurred!'
    event_name = 'update_state'
    event_value = 1
    box = Box(box_pos, box_type, box_description, event_name, event_value)
        
    def test_0_box_override_str_method(self):
        print(str(self.box))
        self.assertEqual(str(self.box), 'Event: some event occurred!\n')
    
    def test_1_display_box_icon_method(self):
        print()
        BoxView.display_box(self.box)
        self.box.box_type = 'danger'
        BoxView.display_box(self.box)
    
    def test_2_create_box_method(self):
        box_events = [
            {
            "box_type": "mystery",
            "description": "saw a magic gate which brought him to the Finish Flag. (finished)",
            "event_name": "update_state",
            "event_value": 1 
            }
        ]
        box = BoxService.create_box(1, box_events)
        self.assertEqual(type(box).__name__, 'Box')
        self.assertEqual(box.box_type, 'mystery')
        

if __name__ == '__main__':
    unittest.main(verbosity=2)