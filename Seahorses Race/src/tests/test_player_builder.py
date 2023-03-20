import unittest
import config_path_for_test

from main.player.player import Player
from main.player.player_builder import PlayerBuilder
from main.seahorse.seahorse import Seahorse


class PlayerBuilderTest(unittest.TestCase):
    def test_create_player_with_name_provided_must_return_player_instance(self):
        # Given
        name = 'Tester'
        seahorses = [Seahorse(seahorse_id) for seahorse_id in range(1, 4)]
        expected_output =  Player(name, seahorses, "manual")
        sut = PlayerBuilder()
        
        # When 
        actual_output = sut.create_player('Tester')

        # Then
        self.assertEqual(actual_output.__class__.__name__, Player.__name__)
        self.assertEqual(actual_output.name, expected_output.name)
        self.assertEqual(actual_output.player_type, expected_output.player_type)

    def test_create_computer_player_with_name_and_type_provided(self):
        # Given
        name = 'computer'
        seahorses = [Seahorse(seahorse_id) for seahorse_id in range(1, 4)]
        expected_output =  Player(name, seahorses, "auto")
        sut = PlayerBuilder()
        
        # When 
        actual_output = sut.create_player(name, "auto")

        # Then
        self.assertEqual(actual_output.__class__.__name__, Player.__name__)
        self.assertEqual(actual_output.name, expected_output.name) 
        self.assertEqual(actual_output.player_type, expected_output.player_type)

if __name__ == '__main__':
    unittest.main(verbosity=2)