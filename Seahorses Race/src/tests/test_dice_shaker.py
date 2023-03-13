import os
import sys
import unittest
from unittest.mock import patch

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from main.dice.dice_shaker import DiceShaker


class DieShakerTests(unittest.TestCase):
    """Testing dice shaker"""
    @patch('time.sleep', return_value=None)
    def test_shake_dice_return_result_from_one_to_six_is_valid(self, patched):
        dice_shaker = DiceShaker()
        
        result = dice_shaker.shake_dice()

        self.assertTrue(1 <= result <= 6)


if __name__ == '__main__':
    unittest.main(verbosity=2)