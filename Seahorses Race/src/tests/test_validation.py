import os
import sys
import unittest
from parameterized import parameterized

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from main.utils.validation import Validation

class ValidationTests(unittest.TestCase):
    
    @parameterized.expand([
        (('1', '2', '3'), '1', '1'),
        (('1', '2', 'sur'), 'sur', 'sur')
    ])
    def test_get_player_input_if_it_is_a_valid_option(self, valid_options: list,
                                                      user_inp: str,
                                                      expected_output: str):
        # When
        actual_output = Validation.user_option_validation(valid_options, user_inp)
        
        # Then
        self.assertEqual(actual_output, expected_output)
    
    @parameterized.expand([
        (('1', '2', '3'), 1),
        (('1', '2', '3'), ''),
        (('1', '2', '3'), 'a'),
        (('1', '2', '3'), ' '),
    ])
    def test_cannot_get_player_input_if_it_is_a_invalid_option(self, 
                                                               valid_options: list,
                                                               user_inp: str):
        with self.assertRaises(ValueError):
            Validation.user_option_validation(valid_options, user_inp)


    def test_can_get_player_name_entered_if_it_is_valid(self):
        # Given
        valid_name = "Peter Parker"
        avoid_name = 'computer'
        expected_output = valid_name
        
        # When
        actual_output = Validation.user_name_validation(valid_name, avoid_name)
        
        # Then
        self.assertEqual(actual_output, expected_output)
    
    @parameterized.expand([
        ('computer', 'computer'),                       # case 1: exist name
        ('computer', ''),                               # case 2: empty name
        ('computer', '123123321321321313211321313123')  # case 3: lengthy name
    ])
    def test_cannot_get_player_name_if_it_is_a_invalid_name(self,
                                                            avoid_name: str,
                                                            player_input: str):
        with self.assertRaises(ValueError):
            Validation.user_name_validation(player_input, avoid_name)
    
    def test_can_get_seahorse_id_if_it_valid(self):
        # Given
        input_id = 1
        valid_inp = (1, 3, 4)
        expected_output = input_id
        
        # When
        actual_output =Validation.seahorse_id_valid(input_id, valid_inp)
        
        # Then
        self.assertEqual(actual_output, expected_output)
        
    @parameterized.expand([
        ((1, 2, 3), 'a'),   # case 1: character input
        ((1, 2 ,3), 4)      # case 2: id not exist 
    ])
    def test_cannot_get_seahorse_id_if_it_invalid(self, valid_id: tuple[int],
                                                  player_input: str or int):
        with self.assertRaises(ValueError):
            Validation.seahorse_id_valid(player_input, valid_id)
        
         
    
if __name__ == '__main__':
    unittest.main()