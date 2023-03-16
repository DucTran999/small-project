import os
import sys
import unittest
from parameterized import parameterized

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.seahorse.seahorse import Seahorse
from main.seahorse.filter_seahorse_service import FilterSeahorseService 


class FilterSeahorseServiceTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = FilterSeahorseService()
    
    @parameterized.expand([
        ('Warm up', False),
        ('Finish', False),
        ('Cannot race', False),
        ('Ready', True),
        ('Running', True),
    ])
    def test_can_detect_seahorse_can_move_by_state(self, state: str, 
                                                   expected_output: bool
                                                   ):
        # When
        actual_output = self.sut.is_seahorse_can_move(state)
        
        # Then
        self.assertEqual(actual_output, expected_output)
    
    @parameterized.expand([
        ('Warm up', True),
        ('Finish', False),
        ('Cannot race', False),
        ('Ready', False),
        ('Running', False),
    ])
    def test_can_detect_seahorse_is_warm_up_by_state(self, state: str, 
                                                     expected_output: bool
                                                     ):
        # When
        actual_output = self.sut.is_seahorse_warm_up(state)
        
        # Then
        self.assertEqual(actual_output, expected_output)
    
    @parameterized.expand([
        ('Warm up', True),
        ('Finish', False),
        ('Cannot race', False),
        ('Ready', True),
        ('Running', True),
    ])
    def test_can_detect_seahorse_is_available_for_race_by_state(
        self, state: str, expected_output: bool
        ):
        # When
        actual_output = self.sut.is_seahorse_available(state)
        
        # Then
        self.assertEqual(actual_output, expected_output)
    
    def test_filter_seahorse_can_move_id_by_state(self):
        # Given
        seahorse_fake_1 = Seahorse(1, 2, 'Warm up')
        seahorse_fake_2 = Seahorse(2, 2, 'Ready')
        seahorse_fake_3 = Seahorse(3, 2, 'Running')
        seahorse_fake_4 = Seahorse(4, 2, 'Finish')
        seahorse_fake_5 = Seahorse(5, 2, 'Cannot race')
        seahorses = [seahorse_fake_1, seahorse_fake_2, seahorse_fake_3,
                     seahorse_fake_4, seahorse_fake_5]
        expected_output = [2, 3]
        
        # When 
        actual_output = self.sut.get_seahorse_can_move_id_list(seahorses)
        
        # Then
        self.assertListEqual(actual_output, expected_output)
    
    def test_filter_seahorse_warm_up_id_by_state(self):
        # Given
        seahorse_fake_1 = Seahorse(1, 2, 'Warm up')
        seahorse_fake_2 = Seahorse(2, 2, 'Warm up')
        seahorse_fake_3 = Seahorse(3, 2, 'Running')
        seahorse_fake_4 = Seahorse(4, 2, 'Finish')
        seahorse_fake_5 = Seahorse(5, 2, 'Warm up')
        seahorses = [seahorse_fake_1, seahorse_fake_2, seahorse_fake_3,
                     seahorse_fake_4, seahorse_fake_5]
        expected_output = [1, 2, 5]
        
        # When 
        actual_output = self.sut.get_seahorse_warm_up_id_list(seahorses)
        
        # Then
        self.assertListEqual(actual_output, expected_output)
    
    def test_filter_seahorse_available_for_race_id_by_state(self):
        # Given
        seahorse_fake_1 = Seahorse(1, 2, 'Warm up')
        seahorse_fake_2 = Seahorse(2, 2, 'Warm up')
        seahorse_fake_3 = Seahorse(3, 2, 'Running')
        seahorse_fake_4 = Seahorse(4, 2, 'Finish')
        seahorse_fake_5 = Seahorse(5, 2, 'Warm up')
        seahorses = [seahorse_fake_1, seahorse_fake_2, seahorse_fake_3,
                     seahorse_fake_4, seahorse_fake_5]
        expected_output = [1, 2, 3, 5]
     
        # When 
        actual_output = self.sut.get_seahorses_available_id_list(seahorses)
        
        # Then
        self.assertListEqual(actual_output, expected_output)

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.sut


if __name__ == '__main__':
    unittest.main(verbosity=1)
    