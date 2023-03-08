import os
import sys

import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from main.utils.validation import Validation

class TestValidation(unittest.TestCase):
    """Test validation class's methods 
    
    List of methods tested:
    - user_option_validation.
    - user_name_validation
    """
    def test_0_can_get_user_option_if_input_valid(self):
        # set up data for test
        valid_options = ('1', '2', '3')
        user_inp = '1'
        int_inp, empty_inp , str_inp = 1, '', 'a'
        
        print("\n---Start Test 0")
        
        print("Case 1: user enter valid option.")
        expected = Validation.user_option_validation(user_inp, valid_options)        
        self.assertEqual(user_inp, expected)
        
        print("Case 2: user enter invalid option.")
        with self.assertRaises(ValueError) as cm:
            Validation.user_option_validation(int_inp, valid_options)
        self.assertEqual(str(cm.exception), 'Invalid option!')
        
        with self.assertRaises(ValueError) as cm:
            Validation.user_option_validation(empty_inp, valid_options)
        self.assertEqual(str(cm.exception), 'Invalid option!')

        with self.assertRaises(ValueError) as cm:
            Validation.user_option_validation(str_inp, valid_options)
        self.assertEqual(str(cm.exception), 'Invalid option!')

        print("---Finish Test 0")
        
    def test_1_user_name_validation(self):
        # prepare data for test
        valid_name = "Peter Parker"
        empty_name = ''
        name_over_30_chars = 'My name is A B C D E F G H I J K L M N O P'
        
        print("\n---Start Test 1:")
        
        print("Case 1: Test valid name.")
        expected = Validation.user_name_validation(valid_name)
        self.assertEqual(expected, valid_name)
        
        print("Case 2: Test invalid name.")
        empty_name_err_msg = "<!> Empty name not excepted!"
        with self.assertRaises(ValueError) as cm:
            Validation.user_name_validation(empty_name)
        self.assertEqual(str(cm.exception), empty_name_err_msg)

        lengthy_name_err_msg = "<!> Name cannot over 30 chars"
        with self.assertRaises(ValueError) as cm:
            Validation.user_name_validation(name_over_30_chars)
        self.assertEqual(str(cm.exception), lengthy_name_err_msg)
        
        print("---Finish Test 1")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)