import os
import sys
import unittest
from parameterized import parameterized

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.seahorse.seahorse import Seahorse

class SeahorseTests(unittest.TestCase):
    @parameterized.expand([
        (Seahorse(1, 0, 'Ready'), 6, 6, 'Running'),
        (Seahorse(2, 2, 'Running'), 4, 6, 'Running'),
        (Seahorse(3, 8, 'Running'), 6, 13, 'Finish')
    ])
    def test_move_seahorse_by_steps_then_new_position_and_state_are_updated(
        self, seahorse_fake: Seahorse, move_steps: int,
        expected_position: int, expected_state: str):
        # Act
        seahorse_fake.move(move_steps)
        
        # Assert
        self.assertEqual(seahorse_fake.position, expected_position)
        self.assertEqual(seahorse_fake.state, expected_state)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)