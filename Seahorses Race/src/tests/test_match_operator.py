import config_path_for_test
import unittest
from unittest.mock import patch, MagicMock

from parameterized import parameterized
from main.player.player import Player
from main.match.match import Match
from main.match.match_operator import MatchOperator


class TestClassOperator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.match = Match()
        cls.sut = MatchOperator()
    
    def test_find_the_winner_in_surrender_case(self):
        # Given
        p1, p2 = Player("Willie", [], "manual"), Player("Mike", [], "manual")        
        self.match.players = [p1, p2]
        expected_winner = p1
        
        # When
        actual_winner = self.sut.find_the_match_winner(self.match, 'sur', "Mike")
        
        # Then
        self.assertEqual(self.match.state, "finished")
        self.assertEqual(actual_winner, expected_winner)

    def test_find_the_winner_when_no_player_surrender(self):
        # Given
        p1 = Player("Willie", [], "manual", 0, 6)
        p2 = Player("Mike", [], "manual", 0, 5)
        self.match.players = [p1, p2]
        expected_winner = p2
        
        # When
        actual_winner = self.sut.find_the_match_winner(self.match)
        
        # Then
        self.assertEqual(self.match.state, "finished")
        self.assertEqual(actual_winner, expected_winner)
   
    @patch('time.sleep', create=True)
    @patch("builtins.print", create=True)
    @patch("builtins.input", create=True)
    def test_fullfil_player_roll_dice_request_to_get_valid_dice_face(
            self, mock_player_input: MagicMock, patched_time_sleep: MagicMock,
            patched_print: MagicMock):
        # Given
        p1 = Player("Willie", [], "manual", 0, 6)
        p2 = Player("Mike", [], "manual", 0, 5)
        self.match.players = [p1, p2]
        patched_time_sleep.return_value = patched_print.return_value = None
        mock_player_input.side_effect = ['a', '', 'r']
        
        expected_dice_faces = list(range(1, 7))
        
        # When 
        dice_face = self.sut.ask_player_for_dice_roll(self.match, p1)
        
        # Then
        self.assertTrue(dice_face in expected_dice_faces)
    
    @patch("builtins.print")
    @patch("time.sleep")
    def test_give_player_turn_without_execute_dice_event(
            self, patched_time_sleep: MagicMock, patched_print: MagicMock):
        # Given
        p1 = Player("Willie", [], "auto", 2, 6)
        p2 = Player("Mike", [], "manual", 0, 5)
        self.match.players = [p1, p2]
        patched_time_sleep.return_value = patched_print.return_value = None
        expected_turn_remain = 0
        # When 
        self.sut.operate_round(self.match)
        
        # Then
        self.assertEqual(p1.turn_remain, expected_turn_remain)
        

    
if __name__ == '__main__':
    unittest.main()