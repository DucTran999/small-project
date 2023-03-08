import os
import sys

import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')


from main.utils.file_helper import FileHelper

class TestFileHelper(unittest.TestCase):
    """Test FileHelper's methods both pass and fail case
    
    List of methods tested:
    - read_text_file
    - read_json_file
    """
    def test_0_read_text_file_method(self):
        # Set up data for testing
        exist_filename = 'guideline'
        non_existent_filename = ''
        
        print("\n---Start Test 0:")
        
        print("\nCase 1: Can read file.")
        content_expected = FileHelper.read_text_file(exist_filename)
        self.assertIsNotNone(content_expected)

        print("Case 2: Cannot read file text. File not found exception.")
        content_expected = FileHelper.read_text_file(non_existent_filename)
        self.assertIsNone(content_expected)

        print("Finish Test 0")
    
    def test_1_read_json_file_method(self):
        # Set up date for testing
        exist_filename = 'box_event'
        none_existent_filename = ''
        
        print("\n---Start Test 1:")
        
        print("Case 1: Can read JSON file.")
        content_expected = FileHelper.read_json_file(exist_filename)
        self.assertIsNotNone(content_expected)
        
        print("Case 2: Cannot read JSON file. File not found exception!")
        content_expected = FileHelper.read_text_file(none_existent_filename)
        self.assertIsNone(content_expected)
        
        print("---Finish Test 1")


if __name__ == '__main__':
    unittest.main(verbosity=2)