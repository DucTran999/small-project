import unittest
import config_path_for_test

from parameterized import parameterized

from main.seahorse.seahorse import Seahorse
from main.seahorse.handle_seahorse_event_service import HandleSeahorseEventService

class HandleSeahorseEventServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = HandleSeahorseEventService()
    
    @parameterized.expand([
        ('move to finish', True),
        ('move faster', True),
        ('get trouble', True),
        ('more roll', False),
    ])
    def test_can_detect_box_is_apply_for_seahorse_by_event_name(
            self, event_name: str, expected_output: bool):
        # When
        actual_output = self.sut.is_box_event_apply_to_seahorse(event_name)
        
        # Then
        self.assertEqual(actual_output, expected_output)
    
    @parameterized.expand([
        (Seahorse(1), 'move to finish', 'Finish', 13, 'Finish'),
        (Seahorse(2, 2, 'Running'), 'move faster', 3, 5, 'Running'),
        (Seahorse(3, 5, 'Running'), 'get trouble', 'Cannot race', 0, 'Cannot race')
    ])
    def test_update_seahorse_info_when_get_box(
            self, seahorse: Seahorse, event_name: str, event_value: str | int,
            expected_position: int, expected_state: str):
        # When
        self.sut.update_seahorse_info_get_box_event(
            seahorse, event_name, event_value)
        
        # Then
        self.assertEqual(seahorse.position, expected_position)
        self.assertEqual(seahorse.state, expected_state)
    
    @parameterized.expand([
        (Seahorse(1, 0, 'Warm up'), 6, 0, 'Ready'),
        (Seahorse(2, 0, 'Ready'), 6, 6, 'Running'),
        (Seahorse(3, 8, 'Running'), 6, 13, 'Finish')
    ])
    def test_update_seahorse_info_when_get_dice_face_6_event(
            self, seahorse: Seahorse, dice_face: int, expected_position: int,
            expected_state: str ):
        # When 
        self.sut.update_seahorse_info_get_face_6_event(seahorse, dice_face)
    
        # Then
        self.assertEqual(seahorse.position, expected_position)
        self.assertEqual(seahorse.state, expected_state)
    
    @parameterized.expand([
        ([4, 5, 7], 6, False),
        ([4, 5, 8], 8, True)
    ])
    def test_can_detect_seahorse_get_box_by_position(
            self, boxes_positions: list[int], seahorse_position: int, 
            expected_output: bool) -> None:
        # When
        actual_output = self.sut.is_seahorse_get_box(seahorse_position,
                                                     boxes_positions)
        
        # Then
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=1)