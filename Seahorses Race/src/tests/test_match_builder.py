import unittest
import config_path_for_test

from unittest.mock import patch, MagicMock

from main.match.match import Match
from main.match.match_builder import MatchBuilder 

from main.player.player import Player


class MatchBuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = MatchBuilder()
    
    @patch('builtins.input', lambda _: 'Daniel', create=True)
    def test_task_build_players_single_mode(self):
        # Given
        fake_player_1 = Player('computer', [1, 2, 3], "auto")
        fake_player_2 = Player('Daniel', [1, 2, 3], "manual")
        expected_output = [fake_player_1, fake_player_2]
        
        # When
        actual_output = self.sut.build_players_single_mode()
        
        # Then
        self.assertEqual(actual_output[0].name, expected_output[0].name)
        self.assertEqual(actual_output[1].name, expected_output[1].name)
        self.assertEqual(actual_output[0].player_type, 
                         expected_output[0].player_type)
        self.assertEqual(actual_output[1].player_type, 
                         expected_output[1].player_type)
    
    @patch('builtins.input')
    def test_task_build_players_multi_mode(self, mock_input: MagicMock):
        # Given
        fake_player_1 = Player('Willie', [1, 2, 3], "manual")
        fake_player_2 = Player('Daniel', [1, 2, 3], "manual")
        expected_output = [fake_player_1, fake_player_2]
        mock_input.side_effect = ['Willie', 'Daniel']
        
        # When
        actual_output = self.sut.build_players_multi_mode()
        
        # Then
        self.assertEqual(actual_output[0].name, expected_output[0].name)
        self.assertEqual(actual_output[1].name, expected_output[1].name)
        self.assertEqual(actual_output[0].player_type, 
                         expected_output[0].player_type)
        self.assertEqual(actual_output[1].player_type, 
                         expected_output[1].player_type)
    
    @patch('builtins.input', create=True)
    def test_get_match_result_single_mode(self, mock_input: MagicMock):
        # Given
        match = Match()
        mock_input.side_effect = ['Daniel']
        
        # When
        match = self.sut.get_result(match, 'single')
    
        # Then
        self.assertIsInstance(match, Match)
        self.assertIsNotNone(match.dice_shaker)
        self.assertEqual(match.players[0].name, 'computer')
        self.assertEqual(match.players[1].name, 'Daniel')
        self.assertIsNotNone(match.race)
        self.assertEqual(match.state, "not finish")
    
    @patch('builtins.input', create=True)
    def test_get_match_result_multi_mode(self, mock_input: MagicMock):
        # Given
        match = Match()
        mock_input.side_effect = ['Willie', 'Daniel']
                                  
        # When
        match = self.sut.get_result(match, 'multi')
    
        # Then
        self.assertIsInstance(match, Match)
        self.assertIsNotNone(match.dice_shaker)
        self.assertEqual(match.players[0].name, 'Willie')
        self.assertEqual(match.players[1].name, 'Daniel')
        self.assertIsNotNone(match.race)
        self.assertEqual(match.state, "not finish")
    
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.sut
       
    
if __name__ == '__main__':
    unittest.main(verbosity=2)