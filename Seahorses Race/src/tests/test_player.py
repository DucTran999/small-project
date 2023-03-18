import unittest
import config_path_for_test

from parameterized import parameterized
from main.player.player import Player


class TestPlayer(unittest.TestCase):
    
    @parameterized.expand([
        (Player('Player1', [], "manual", 1, 1), 2),
        (Player('Player2', [], "manual", 1, 5), 6)
    ])
    def test_track_player_total_turn_each_turn_passed(self, player: Player,
                                                      expected_turns_total: int):
        # When
        player.tracking_turns()
        
        # Then
        self.assertEqual(player.turns_total, expected_turns_total)


if __name__ == '__main__':
    unittest.main()
    