import os
import sys
import unittest

from parameterized import parameterized

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.player.player import Player
from main.player.player_service import PlayerService

from main.seahorse.seahorse import Seahorse


class PlayerServiceTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = PlayerService()

    @parameterized.expand([
        ([Seahorse(1), Seahorse(2, 0, 'Ready'), Seahorse(3, 2, 'Running')], True),
        ([Seahorse(1, 0, 'Cannot race'), Seahorse(2, 0, 'Finish')], False),
    ])
    def test_can_detect_player_has_seahorse_for_race(self, seahorses: list,
                                                     expected_output: bool):
        # When
        actual = self.sut.is_player_has_seahorse_available_for_race(seahorses)
        
        # Then
        self.assertEqual(actual, expected_output)
        
    @parameterized.expand([
        ('lost turn', True),
        ('more roll', True),
        ('get trouble', False)
    ])
    def test_can_detect_event_apply_for_player_by_event_name(self, 
                                                             event_name: str,
                                                             expected_out: bool
                                                             ):
        # When
        actual_out = self.sut.is_box_event_apply_to_player(event_name)
        # Then
        self.assertEqual(actual_out, expected_out)
    
    @parameterized.expand([
        (Player('William', [], 1, 0), 'more roll', 1, 2),
        (Player('William', [], 1, 0), 'lost turn', -1, 0)
    ])
    def test_update_player_info_when_get_box_event(self, fake_player: Player,
                                                   event_name: str,
                                                   event_value: int or str,
                                                   expected_turn_remain: int):
        # When
        self.sut.handle_player_get_box_event(fake_player, event_name, event_value)
        
        # Then
        self.assertEqual(fake_player.turn_remain, expected_turn_remain)
    
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.sut
     
     
if __name__ == '__main__':
    unittest.main()