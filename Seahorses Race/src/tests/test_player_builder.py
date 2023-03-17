import os
import sys
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.player.player import Player
from main.player.player_builder import PlayerBuilder
from main.seahorse.seahorse import Seahorse


class PlayerBuilderTest(unittest.TestCase):
    def test_create_player_with_name_provided_must_return_player_instance(self):
        # Given
        name = 'Tester'
        seahorses = [Seahorse(seahorse_id) for seahorse_id in range(1, 4)]
        expected_output =  Player(name, seahorses)
        sut = PlayerBuilder()
        
        # When 
        actual_output = sut.create_player('Tester')

        # Then
        self.assertIsInstance(actual_output, Player)
        self.assertEqual(actual_output.name, expected_output.name)


if __name__ == '__main__':
    unittest.main(verbosity=2)