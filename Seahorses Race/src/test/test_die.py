import os
import sys

import unittest
import dataclasses

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from main.die.die import Die
from main.die.die_view import DieView

class TestDie(unittest.TestCase):
    
    def test_0_faces_attribute_is_immutable(self):
        die = Die()
        with self.assertRaises(dataclasses.FrozenInstanceError) as cm:
            die.faces = (1, 2, 3, 4, 5)   
        self.assertEqual(str(cm.exception), "cannot assign to field 'faces'")
    
    def test_1_display_die_face_method(self):
        print("\n6 face: ")
        DieView.print_dice_face(6)
        print("\n5 face: ")
        DieView.print_dice_face(5)
        print("\n4 face: ")
        DieView.print_dice_face(4)
        print("\n3 face: ")
        DieView.print_dice_face(3)
        print("\n2 face: ")
        DieView.print_dice_face(2)
        print("\n1 face: ")
        DieView.print_dice_face(1)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)