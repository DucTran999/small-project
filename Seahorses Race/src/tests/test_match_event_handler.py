import unittest
import config_path_for_test

from unittest.mock import patch, MagicMock
from main.match.match_event_handler import MatchEventHandler

from main.box.box import Box
from main.player.player import Player
from main.seahorse.seahorse import Seahorse
from main.race.race import Race


class TestMatchEventHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = MatchEventHandler()
    
    def test_get_box_info_by_it_position(self):
        # Given
        box1 = Box(1, 'mystery', 'description', 'event_name_1', 1)
        box2 = Box(4, 'danger', 'description', 'event_name_2', -1)
        box3 = Box(5, 'danger', 'description', 'event_name_1', 1)
        boxes = [box1, box2, box3]
        test_position = [1, 4, 5] 
        
        # When
        for idx, position in enumerate(test_position):
            expected_box = boxes[idx]
            actual_box = self.sut.get_box_by_position(position, boxes)

            #Then
            self.assertEqual(actual_box, expected_box)
    
    def test_apply_box_event_must_change_player_info(self):
        # Given
        player = Player("Willie", [Seahorse(1, 2, 'Running')], 'manual')
        box_effect_player = Box(2, 'mystery', 'abc', 'more roll', 1)
        box_effect_seahorse = Box(2, 'mystery', 'xyz', 'move to finish', 'Finish')
        expected_player_turn_remain = 2
        expected_seahorse_state = "Finish"
        
        # When 
        self.sut.apply_box_event(
            player.seahorses[0], player, box_effect_player)
        self.sut.apply_box_event(
            player.seahorses[0], player, box_effect_seahorse)
        
        # Then
        self.assertEqual(player.turn_remain, expected_player_turn_remain)
        self.assertEqual(player.seahorses[0].state, expected_seahorse_state)
        
    
    def test_update_player_info_if_get_face_6_event_without_event_box(self):
        # Given
        dice_face = 6
        player = Player("Daniel", [Seahorse(1)], "manual")
        race = Race(12, [1], [Box(1,'dummy','dummy','dummy','dummy')]) 
        seahorse_id = 1
        expected_seahorse_state = "Ready"
        
        # When
        self.sut.update_player_info_depend_on_event(
            player, race, seahorse_id, dice_face)

        # Then         
        self.assertEqual(player.seahorses[0].state, expected_seahorse_state)
    
    def test_update_player_info_if_not_get_face_6_event_without_event_box(self):
        # Given
        player = Player("Daniel", [Seahorse(1, 0, "Ready")], "manual")
        race = Race(12, [1], [Box(1,'dummy','dummy','dummy','dummy')]) 
        seahorse_id = 1
        dice_face = 5
        expected_seahorse_state = "Running"
        expected_seahorse_position = 5
        
        # When
        self.sut.update_player_info_depend_on_event(player, race, 
                                                    seahorse_id, dice_face)

        # Then         
        self.assertEqual(player.seahorses[0].state, expected_seahorse_state)
        self.assertEqual(player.seahorses[0].position, expected_seahorse_position)
        
    def test_computer_auto_select_seahorse_by_id(self):
        # Given
        player = Player("computer", [Seahorse(1), Seahorse(2), Seahorse(3)], "auto")
        seahorse_list = [1, 2, 3]
        
        # When
        actual_output = self.sut.get_seahorse_id_selected(player, seahorse_list)
         
        # Then
        self.assertTrue(actual_output in seahorse_list)
    
    @patch("builtins.input", create=True)
    def test_manual_player_select_seahorse_id(self, mock_input: MagicMock):
        # Given
        player = Player("Daniel", [Seahorse(1), Seahorse(2), Seahorse(3)], "manual")
        expected_id = 1
        list_id = [1, 2 , 3]
        mock_input.side_effect = ['4','', '1']
        
        # When
        actual_output = self.sut.get_seahorse_id_selected(player, list_id)
        
        # Then
        self.assertEqual(actual_output, expected_id)
        
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.sut
    

if __name__     == '__main__':
    unittest.main()