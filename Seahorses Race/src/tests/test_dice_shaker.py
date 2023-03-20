import unittest
from unittest.mock import patch, MagicMock
import config_path_for_test

from main.dice.dice_shaker import DiceShaker


class DieShakerTests(unittest.TestCase):
    """Testing dice shaker"""
    @patch("builtins.print")
    @patch("time.sleep")
    def test_shake_dice_return_result_from_one_to_six_is_valid(
            self, patched_time_sleep: MagicMock, patched_print: MagicMock):
        # Given
        patched_time_sleep.return_value = patched_print.return_value = None
        expected_output_range = [1, 2, 3, 4, 5, 6] 
        sut = DiceShaker()
        
        # When
        actual_output = sut.shake_dice()

        # Then
        self.assertTrue(actual_output in expected_output_range)


if __name__ == '__main__':
    unittest.main()