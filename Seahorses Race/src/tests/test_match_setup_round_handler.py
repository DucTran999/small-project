import config_path_for_test
import unittest

from parameterized import parameterized

from main.player.player import Player
from main.seahorse.seahorse import Seahorse
from main.match.match_set_up_round_handler import MatchSetupRoundHandler


class TestMatchSetupRoundHandler(unittest.TestCase):
    """"""
    @parameterized.expand([
        (   # case 1: Both players state are "not done"
            Player("Mary", [Seahorse(1)], "manual", 0), 
            Player("Peter", [Seahorse(1)], "manual", 0), 
            1, 1
        ),
        (   # case 2: Player 1 done, player 2 'not done'
            Player("Mary", [], "manual", 0, 1, "done"), 
            Player("Peter", [Seahorse(1)], 0, 0, 1, "not done"),
            0, 1
        ),
        (   # case 3: Player 1 done, player 2 not done and freezed.
            Player("Mary", [], "manual", 0, 1, "done"),
            Player("Harry", [Seahorse(1)], "manual", -1, 1, "not done"),
            0, 0  
        ),
        (   # case 4: Both players are freezed.
            Player("Mary", [Seahorse(1)], "manual", -1, 1, "not done"),
            Player("Harry", [Seahorse(1)], "manual", -1, 1, "not done"),
            0, 0  
        )
    ])
    def test_setup_player_turn_next_round(
            self, player_1: Player, player_2: Player, 
            p1_expected_turn_remain: int, p2_expected_turn_remain: int):
        sut = MatchSetupRoundHandler()
        
        # When
        sut.setup_player_turn_for_next_round(player_1, player_2)
        
        # Then
        self.assertEqual(player_1.turn_remain, p1_expected_turn_remain)
        self.assertEqual(player_2.turn_remain, p2_expected_turn_remain)
        


if __name__ == '__main__':
    unittest.main()