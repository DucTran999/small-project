import os
import sys
import unittest

from parameterized import parameterized

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.player.player import Player

from main.seahorse.seahorse import Seahorse

class TestPlayer(unittest.TestCase):
    
    @parameterized.expand([
        (Player('Player1', [], 1, 1), 2),
        (Player('Player2', [], 1, 5), 6)
    ])
    def test_track_player_total_turn_each_turn_passed(self, player: Player,
                                                      expected_turns_total: int):
        # When
        player.tracking_turns()
        
        # Then
        self.assertEqual(player.turns_total, expected_turns_total)


if __name__ == '__main__':
    unittest.main()