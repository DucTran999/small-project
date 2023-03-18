# -*- coding: utf-8 -*-
import unittest
import os
import json
import config_path_for_test

from main.utils.file_helper import FileHelper

class FileHelperTests(unittest.TestCase):
    """Test FileHelper's method"""
    text_file = "Seahorses Race/src/main/db/text_test.txt"
    json_file = "Seahorses Race/src/main/db/json_test.json"
    
    @classmethod
    def write_text_file_for_testing(cls):
        with open(cls.text_file, mode='w', encoding='utf-8') as file_obj:
            file_obj.write("test-data")
    
    @classmethod
    def write_json_file_for_testing(cls):
        with open(cls.json_file, mode='w', encoding='utf-8') as f:
            json_sample: list[dict] = [{"key" : 'value'}]
            json.dump(json_sample, f, ensure_ascii=False, indent=4)
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = FileHelper()
        cls.write_text_file_for_testing()
        cls.write_json_file_for_testing()
    
    def test_cannot_read_text_file_if_file_not_exist(self):
        # Given
        filename = 'anything'
        
        # When
        actual_output = self.sut.read_text_file(filename)
        
        # Then
        self.assertIsNone(actual_output)
    
    def test_can_read_text_file_if_file_exist(self):
        # Given
        file_name = 'text_test'
        expected_output = 'test-data'
        
        # When
        actual_output = self.sut.read_text_file(file_name)
        
        #Then
        self.assertEqual(actual_output, expected_output)
    
    def test_cannot_read_json_file_if_file_not_exist(self):
        # Given
        filename = 'anything'
        
        # When
        actual_output = self.sut.read_json_file(filename)
        
        # Then
        self.assertIsNone(actual_output)
    
    def test_can_read_json_file_if_file_exist(self):
        # Given
        filename = 'json_test'
        expected_output = [{'key': 'value'}]
        
        # When
        actual_output = self.sut.read_json_file(filename)
        
        # Then
        self.assertListEqual(actual_output, expected_output)
    
    @classmethod
    def tearDownClass(cls) -> None:
        os.remove(cls.text_file)
        os.remove(cls.json_file)


if __name__ == '__main__':
    unittest.main(verbosity=2)