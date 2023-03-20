import unittest
import config_path_for_test

from parameterized import parameterized

from main.seahorse.seahorse import Seahorse
from main.player.player import Player
from main.match.match_judge_result_handler import MatchJudgeResultHandler

class MatchJudgeResultHandlerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = MatchJudgeResultHandler()
    
    @parameterized.expand([
        ([Seahorse(1), Seahorse(2, 13, 'Finish'), Seahorse(3, 6, 'Ready')], 1),
        ([Seahorse(1), Seahorse(2, 13, 'Finish'), Seahorse(3, 13, 'Finish')], 2),
        ([Seahorse(1), Seahorse(2), Seahorse(3, 6, 'Cannot Race')], 0)
    ])
    def test_count_seahorse_finished_the_race(self, seahorses: list[Seahorse],
                                              expected_quantity: int):
        # When
        actual_quantity = self.sut.count_finished_seahorse(seahorses)
        
        # Then
        self.assertEqual(actual_quantity, expected_quantity)
    
    def test_find_winner_when_finished_seahorses_quantity_are_equal(self):
        # Given
        p1 = Player('P1', [], "manual", 0, 10)
        p2 = Player('P2', [], "manual", 0, 12)
        expected_output = p1
        
        # When
        actual_output = self.sut.find_winner_seahorse_qty_equal_case(p1, p2)
        
        # Then  
        self.assertEqual(actual_output, expected_output)
    
    def test_find_winner_when_finished_seahorses_quantity_not_equal(self):
        # Given
        p1 = Player('P1', [Seahorse(1)],"manual", 0, 10)
        p2 = Player('P2', [Seahorse(1, 13, 'Finish')], "manual", 0, 12)
        expected_output = p2
        
        # When
        actual_output = self.sut.judge_match_result_no_surrender_player(p1, p2)
        
        # Then  
        self.assertEqual(actual_output, expected_output)
    
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.sut
    
        
if __name__ == '__main__':
    unittest.main(verbosity=2)