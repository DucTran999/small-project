import os
import sys
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.player.player import Player
from main.player.player_view import PlayerView
from main.player.player_service import PlayerService

from main.seahorse.seahorse import Seahorse


class TestPlayer(unittest.TestCase):
    """Test methods in player package
    
    Methods list:
    - create_player.
    - is_box_event_apply_to_player.
    - handle_player_get_box_event.
    """
    def test_0_display_player_info_method(self):
        #set up data for test
        player: Player = PlayerService.create_player('Tester')
        
        print("\n---Start Test 0:")
        PlayerView.display_player_info(player)
        print("---Finish Test 0")

    def test_1_is_box_event_apply_to_player_method(self):
        #set up data for test
        event_1, event_2, event_3 = 'lost turn', 'more roll', 'get trouble'
        
        print("\n---Start Test 1:")
        
        print("Case 1: Check event applies to player object.")
        self.assertTrue(PlayerService.is_box_event_apply_to_player(event_1))
        self.assertTrue(PlayerService.is_box_event_apply_to_player(event_2))
        
        print("Case 2: Check event does not apply to player object.")
        self.assertFalse(PlayerService.is_box_event_apply_to_player(event_3))
        
        print("---Finish Test 1")
    
    def test_2_player_get_box_event(self):
        # set up data for test
        player = PlayerService.create_player('William')
        
        print("\n---Start Test 2:")
        
        print("Case 1: User lost turn.")
        PlayerService.handle_player_get_box_event(player, 'lost turn', -1)
        self.assertEqual(player.turn_remain, 0)
        PlayerService.handle_player_get_box_event(player, 'lost turn', -1)
        self.assertEqual(player.turn_remain, -1)
        
        print("Case 2: User get more roll.")
        PlayerService.handle_player_get_box_event(player, 'more roll', 1)
        self.assertEqual(player.turn_remain, 0)
        PlayerService.handle_player_get_box_event(player, 'more roll', 2)
        self.assertEqual(player.turn_remain, 2)
        
        print("---Finish Test 2")       
    
    def test_3_tracking_player_total_turn_method(self):
        #set up data for testing
        player = Player('John', [])
        
        print("\n---Start Test 3:")
        player.tracking_turns()
        self.assertEqual(player.turns_total, 1)
        print("---Finish Test 3")
    
    def test_4_is_player_has_seahorse_available_for_race(self):
        #set up data for test
        sh1, sh2, sh3 = Seahorse(1), Seahorse(2, 0, 'Ready'), Seahorse(3, 0, 'Finish')
        two_seahorses_available = [sh1, sh2]
        no_seahorse_available = [sh3]
        
        print("\n---Start test 4: ")
        print("Case 1: Two seahorse available for race.")
        self.assertTrue(PlayerService.is_seahorses_available_for_race(two_seahorses_available))
        
        print("Case 2: No seahorse available for race.")
        self.assertFalse(PlayerService.is_seahorses_available_for_race(no_seahorse_available))
        print("\n---Finish Test 4")
    
    def test_5_get_seahorse_id_for_action(self):
        # Set up daa for testing
        valid_id = [1, 2]
        print("\n---Start test 5:")
        PlayerView.get_seahorse_id_for_action(valid_id)
        print("\n---Finish test 5:")
     
     
if __name__ == '__main__':
    unittest.main(verbosity=2)