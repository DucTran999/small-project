import os
import sys

import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.box.box import Box
from main.box.box_builder import BoxBuilder

class BoxTests(unittest.TestCase):
    
    def test_box_builder_with_position_and_event_must_return_a_box_instance(self):
        # Given
        position = 3
        event = {
            "event_type": "mystery",
            "description": "saw a magic gate that let him move direct to the Finish Flag.",
            "event_name": "update_state",
            "event_value": 1
        }
        expected_output = Box(position, 
                           event.get('event_type'),
                           event.get('description'),
                           event.get('event_name'),
                           event.get('event_value')
                           )
        sut = BoxBuilder()
        
        # When
        actual_output = sut.create_box(position, event) 
        
        # Then
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main(verbosity=2)