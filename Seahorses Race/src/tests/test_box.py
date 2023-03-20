import unittest
import config_path_for_test

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
                           event.get('event_type'), event.get('description'),
                           event.get('event_name'), event.get('event_value'))
        sut = BoxBuilder()
        
        # When
        actual_output: Box = sut.create_box(position, event) 
        
        # Then
        self.assertEqual(actual_output.position, expected_output.position)
        self.assertEqual(actual_output.description, expected_output.description)
        self.assertEqual(actual_output.event_name, expected_output.event_name)
        self.assertEqual(actual_output.event_type, expected_output.event_type)
        self.assertEqual(actual_output.event_value, expected_output.event_value)
         
         
if __name__ == '__main__':
    unittest.main()