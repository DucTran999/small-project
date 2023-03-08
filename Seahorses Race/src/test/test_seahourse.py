import os
import sys
import time
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append(parent + '/main')

from main.seahorse.seahorse import Seahorse
from main.seahorse.seahorse_service import SeahorseService 

class TestSeahorse(unittest.TestCase):
    
    def test_0_override_represent_seahorse_method(self):
        # Create seahorse for test
        seahorse = Seahorse(1, 2, 0)    
        
        print("\n--- Start Test 0:")
        print("Seahorse: ", seahorse)
        print("---Finish Test 0.")
    
    def test_1_move_method(self):
        # Create seahorse for test
        seahorse = Seahorse(1, 2, 'Warm up')
        
        print("\n---Start Test 1:")
        print("Case 1: seahorse's running on the race")
        step = 6
        seahorse.move(step)
        self.assertEqual(8, seahorse.position)
        
        print("Case 2: seahorse run to finish")
        seahorse.move(step)
        self.assertEqual(14, seahorse.position)
        self.assertEqual('Finish', seahorse.state)
        
        print("---Finish Test 1:")

    def test_3_seahorse_can_move_method(self):
        # Stet up data for test
        invalid_state= ('Warm up', 'Finish', 'Cannot race')
        valid_state = ('Ready', 'Running')
        
        print("\n---Start Test 3:")
        print("Case 1: Suppose to move seahorse's state is invalid.")
        for state in invalid_state:
            self.assertFalse(SeahorseService.is_seahorse_can_move(state))
        
        print("Case 2: Suppose to move seahorse's state is valid.")
        for state in valid_state:
            self.assertTrue(SeahorseService.is_seahorse_can_move(state))
        print("---Finish Test 3:")
    
    def test_4_get_seahorse_can_move_list(self):
        # Set up data for test
        sh1 = Seahorse(1, 2, 'Warm up')
        sh2 = Seahorse(2, 2, 'Ready')
        sh3 = Seahorse(3, 2, 'Running')
        sh4 = Seahorse(4, 2, 'Finish')
        sh5 = Seahorse(5, 2, 'Cannot race')
        seahorses = [sh1, sh2, sh3, sh4, sh5]
        
        print("\n---Start Test 4:")
        
        print("Case 1: classifying seahorse can move.")
        id_classified = SeahorseService.get_seahorse_can_move_id_list(seahorses)
        self.assertListEqual([2, 3], id_classified)
        print("---Finish Test 4:")
    
    def test_5_get_seahorses_warm_up(self):
        # Set up data for test
        sh1 = Seahorse(1, 2, 'Warm up')
        sh2 = Seahorse(2, 2, 'Ready')
        sh3 = Seahorse(3, 2, 'Running')
        sh4 = Seahorse(4, 2, 'Finish')
        sh5 = Seahorse(5, 2, 'Cannot race')
        seahorses = [sh1, sh2, sh3, sh4, sh5]
        
        print("\n---Start Test 5:")
        
        print("Case 1: classifying seahorse is warming up.")
        id_classified = SeahorseService.get_seahorse_warm_up_id_list(seahorses)
        self.assertListEqual([1], id_classified)
        print("---Finish Test 5:")
        
    def test_6_is_seahorse_get_box_method(self):
        # Set up data for test
        boxes_pos = [4, 5, 7]
        sh1_pos = 4
        sh2_pos = 12
        
        print("\n---Start test 6:")
        
        print("Case 1: Seahorse gets box")
        self.assertTrue(SeahorseService.is_seahorse_get_box(sh1_pos, boxes_pos))

        print("Case 2: Seahorse does not get box")
        self.assertFalse(SeahorseService.is_seahorse_get_box(sh2_pos, boxes_pos))

        print("--Finish Test 6.")

    def test_7_is_box_event_apply_to_seahorses_method(self):
        # Set up data for test
        event1 = 'move to finish'
        event2 = 'move faster'
        event3 = 'get trouble'
        event4 = 'more roll'
        
        print("\n---Start test 7:")
        
        print("Case 1: Event box applies to seahorses")
        self.assertTrue(SeahorseService.is_box_event_apply_to_seahorse(event1))
        self.assertTrue(SeahorseService.is_box_event_apply_to_seahorse(event2))
        self.assertTrue(SeahorseService.is_box_event_apply_to_seahorse(event3))
        
        print("Case 2: Event box applies to seahorses")
        self.assertFalse(SeahorseService.is_box_event_apply_to_seahorse(event4))
        
        print("---Finish Test 7")
    
    def test_8_handle_seahorse_get_box_event_method(self):
        # Set up data for test
        sh1, sh2, sh3 = Seahorse(1), Seahorse(2), Seahorse(3, 6)
        event_name1, event_val1 = 'move to finish', 'Finish'
        event_name2, event_val2 = 'move faster', 3
        event_name3, event_val3 = 'get trouble', 'Cannot race'
        
        print("\n---Start test 8:")
        
        print("Case 1: Seahorse get event 'move to finish'.")
        SeahorseService.handle_seahorse_get_box_event(sh1, event_name1, event_val1)
        self.assertEqual(sh1.state, 'Finish')
        self.assertEqual(sh1.position, 13)
        
        print("Case 2: Seahorse get event 'move faster'")
        SeahorseService.handle_seahorse_get_box_event(sh2, event_name2, event_val2)
        self.assertEqual(sh2.position, 3)
        
        print("Case 3: Seahorse get event 'get trouble'.")
        SeahorseService.handle_seahorse_get_box_event(sh3, event_name3, event_val3)
        self.assertEqual(sh3.state, 'Cannot race')
        self.assertEqual(sh3.position, 0)
        
        print("---Finish Test 8")      
    
    def test_9_seahorse_move_to_start_method(self):
        # Set up data for testing.
        sh = Seahorse(1)
        
        print("\n---Start test 9:")
        sh.move_to_start()
        self.assertEqual(sh.position, 0)
        self.assertEqual(sh.state, 'Ready')
        print("Finish test 9")
        
    
if __name__ == '__main__':
    unittest.main(verbosity=2)