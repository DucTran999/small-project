import os
import sys
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.player.player import Player
from main.player.player_view import PlayerView

from main.seahorse.seahorse import Seahorse

from main.race.race import Race

from main.box.box import Box

from main.match.match_service import MatchService
from main.match.match_controller import MatchController


class TestMatch(unittest.TestCase):
    
    @unittest.SkipTest
    def test_0_create_player_list(self):
        # set up data for testing
        match_s = MatchService()
        
        print("\n---Start Test 0:")
        
        print("Case 1: Single player mode.")
        players = match_s.create_players_list_single_game()
        for player in players:
            PlayerView.display_player_info(player)
        
        print("Case 2: Two players mode.")
        players = match_s.create_players_list()
        for player in players:
            PlayerView.display_player_info(player)
        print("---Finish Test 0")
    
    @unittest.SkipTest
    def test_1_ask_player_for_rolling_die_method(self):
        match_c = MatchController()
        match_c.start_two_player_match()
    
    @unittest.SkipTest
    def test_2_finished_seahorse_qty_not_equal_case_method(self):
        # Set up data for testing
        player1 = Player('Tom',[], 0, 30)
        player2 = Player('Jerry',[], 0, 30)
        match_s = MatchService()
        
        print("\n---Start Test 2: ")
        
        print("Case 1: Draw game case.")
        winner = match_s.finished_seahorse_qty_not_equal_case(player1, player2)
        self.assertIsNone(winner)
        
        print("Case 2: player 1 win!")
        player1.turns_total = 25
        winner = match_s.finished_seahorse_qty_not_equal_case(player1, player2)
        self.assertEqual(winner.name, "Tom")
        
        print("Case 3: player 2 win!")
        player1.turns_total = 35
        winner = match_s.finished_seahorse_qty_not_equal_case(player1, player2)
        self.assertEqual(winner.name, "Jerry")
        
        print("---Finish Test 2")
    
    @unittest.SkipTest
    def test_3_judge_match_result(self):
        # Set up data for testing
        sh1, sh2 = Seahorse(1, 13, 'Finish'), Seahorse(1, 0, 'Cannot race')
        player1 = Player('Tom',[sh1], 0, 25)
        player2 = Player('Jerry',[sh2], 0, 25)
        match_s = MatchService()
        
        print("\n---Start Test 3: ")
        
        print("Case 1: player 1 win!")
        winner = match_s.judge_match_result(player1, player2)
        self.assertEqual(winner.name, "Tom")
        
        print("---Finish Test 3")

    def test_4_handle_face_6_event(self):
        #Set up data for testing
        box_1 = Box(7, 'mystery', 'abc', 'more roll', 1)
        box_2 = Box(8, 'danger', 'xyz', 'lost turn', -1)
        box_3 = Box(1, 'mystery', 'aaa','move faster', 3)
        box_4 = Box(5, 'mystery', 'sth', 'move to finish', 'Finish')
        box_5 = Box(9, 'danger', 'sth', 'get trouble', 'Cannot race')
        sh1 = Seahorse(1, 1, 'Running')
        sh2 = Seahorse(2, 2, 'Running')
        sh3 = Seahorse(3, 0, 'Warm up')
        sh4 = Seahorse(4, 5, 'Running')
        p1 = Player('Tom', [sh1, sh2, sh3, sh4], 1, 10)
        race = Race(12, [box_3, box_4, box_1, box_2, box_5])
        match_c = MatchController()
        
        print("\n---Start Test 4: ")
        
        # input id 1
        print("Case 1: Event name: more roll")
        match_c.handle_face_6_event(p1, race, 6)
        self.assertEqual(p1.turn_remain, 2)

        # input id 2
        print("Case 2: Event name: lost turn.")
        match_c.handle_face_6_event(p1, race, 6)
        self.assertEqual(p1.turn_remain, 1)
        
        # input id 3
        print("Case 3: Move seahorse to start.")
        match_c.handle_face_6_event(p1, race, 6)
        self.assertEqual(p1.seahorses[2].state, 'Ready')
        
        # input id 3
        print("Case 4: Seahorse get event move faster.")
        match_c.handle_other_face_event(p1, race, 1)
        self.assertEqual(p1.seahorses[2].position, 4)
        
        # input id 3
        print("Case 5: Seahorse get event go to finish")
        match_c.handle_other_face_event(p1, race, 1)
        self.assertEqual(p1.seahorses[2].state, 'Finish')
        self.assertEqual(p1.seahorses[2].position, 13)
        
        #input id 4
        print("Case 6: Seahorse get event 'get trouble'")
        match_c.handle_other_face_event(p1, race, 4)
        self.assertEqual(p1.seahorses[3].state, 'Cannot race')
        self.assertEqual(p1.seahorses[3].position, 0)
        print("---Finish Test 4")
    
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
              