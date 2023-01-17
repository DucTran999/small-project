""" Dice class handles all player dice operations. """

from random import seed, choice, shuffle
from time import time

class Dice:
    
    def __init__(self):
        """ Dice always have 6 sides """
        self.sides = [1, 2, 3, 4, 5, 6]

    def roll_dice(self):
        """The dice are random according to how the player rolls it.
        
        Keyword argument: 
        power -- determine how fast or slow the player rolls the dice.
        power in range 1 to 100 and use it as a seed for random.
        """
        while True:
            try:
                print("Fast or slow rolling? ")
                player_input = int(input("Enter power from 1 to 100: "))
                if player_input < 1:
                    print("Roll please!")
                elif player_input > 100:
                    print("You use to much power. The dice was broken.")
                else:
                    roll_result = self.pseudo_random_dice_roll(player_input)
                    return roll_result
            except ValueError:
                print("Enter number only.")

    def pseudo_random_dice_roll(self, power):
        """A formula to get the most random number possible.
            
            1. create a seed by time() and power
            2. shuffle the list of dice's side
            3. choice
        """
        a_seed = int(time()) + power
        seed(a_seed)
        shuffle(self.sides)
        roll_result = choice(self.sides)
        
        return roll_result
    
    def print_dice_side(self, side):
        side_1 =  " ------- \n"
        side_1 += "|       |\n"
        side_1 += "|   o   |\n"
        side_1 += "|       |\n"
        side_1 += " ------- \n"

        side_2 =  " ------- \n"
        side_2 += "| o     |\n"
        side_2 += "|       |\n"
        side_2 += "|     o |\n"
        side_2 += " ------- \n"

        side_3 =  " ------- \n"
        side_3 += "| o     |\n"
        side_3 += "|   o   |\n"
        side_3 += "|     o |\n"
        side_3 += " ------- \n"

        side_4 =  " ------- \n"
        side_4 += "| o   o |\n"
        side_4 += "|       |\n"
        side_4 += "| o   o |\n"
        side_4 += " ------- \n"

        side_5 =  " ------- \n"
        side_5 += "| o   o |\n"
        side_5 += "|   o   |\n"
        side_5 += "| o   o |\n"
        side_5 += " ------- \n"

        side_6 =  " ------- \n"
        side_6 += "| o   o |\n"
        side_6 += "| o   o |\n"
        side_6 += "| o   o |\n"
        side_6 += " ------- \n"
        
        if side == 1:
            print(side_1)
        elif side == 2:
            print(side_2)
        elif side == 3:
            print(side_3)
        elif side == 4:
            print(side_4)
        elif side == 5:
            print(side_5)
        else:
            print(side_6)
        