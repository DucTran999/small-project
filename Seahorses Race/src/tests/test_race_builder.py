import unittest
import config_path_for_test

from main.box.box import Box

from main.race.race import Race
from main.race.race_builder import RaceBuilder


class RaceBuilderTests(unittest.TestCase):
    """Test methods in race package"""
    def setUp(self) -> None:
        self.sut = RaceBuilder()
    
    def test_generates_box_quantity_with_maximum_are_provided_and_expected_the_result_from_1_to_maximum(self):
        # Given
        maximum_qty = 4
        expected_output_range = list(range(1, maximum_qty+1))

        # When 
        actual_output = self.sut.generate_box_quantity_randomly(maximum_qty)
        
        # Then   
        self.assertTrue(actual_output in expected_output_range)
    
    def test_generates_boxes_positions_with_quantity_is_provided_and_expected_the_result_is_subset_of_positions_set(self):
        # Given
        steps = 12
        quantity = 3
        positions_set = set(range(1, steps + 1))
        
        # When
        actual_result = set(self.sut.generate_box_positions_randomly(quantity, steps))
        
        # Then
        self.assertTrue(actual_result.issubset(positions_set))
    
    def test_generates_boxes_with_positions_provided_and_the_expected_result_is_list_of_box_objects(self):
        # Given
        boxes_positions = [1, 7]
        box_dummy_1 = Box(1, 'mystery', 'something', 'event', 1)
        box_dummy_2 = Box(7, 'danger', 'something', 'bad_event', -1)
        expected_output = [box_dummy_1, box_dummy_2]
        
        # When
        actual_output = self.sut.generate_boxes(boxes_positions)
        
        # Then
        self.assertEqual(len(expected_output), len(actual_output))
        self.assertEqual(actual_output[0].position, expected_output[0].position)
        self.assertEqual(actual_output[1].position, expected_output[1].position)
    
    def test_create_race_with_length_and_boxes_must_return_a_race_instance(self):
        # Given
        steps = 8
        expected_box_qty = list(range(1, steps//2))
        
        # When
        actual_output = self.sut.create_race(steps) 
        
        # Then
        self.assertEqual(actual_output.__class__.__name__, Race.__name__)
        self.assertEqual(actual_output.steps, steps)
        self.assertTrue(len(actual_output.boxes_positions), expected_box_qty)

    def tearDown(self) -> None:
        del self.sut
    
    
if __name__ == '__main__':
    unittest.main(verbosity=2)