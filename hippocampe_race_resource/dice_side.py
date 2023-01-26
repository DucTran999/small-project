""" Dice class handles all player dice operations. """

from random import seed, choice, shuffle, randint
from time import time, sleep

class Dice:
    
    def __init__(self):
        """ Dice always have 6 sides """
        self.sides = [1, 2, 3, 4, 5, 6]

    def roll_dice(self, name, computer_flag=0):
        """The dice are random according to how the player rolls it.
        
        Keyword argument: 
        power -- determine how fast or slow the player rolls the dice.
        power in range 1 to 100 and use it as a seed for random.
        computer_flag: automation handle event for computer.
        """
        
        if computer_flag == 1:
            sleep(1)
            print("<*> Computer turn: ")
            power = randint(1, 100)
            roll_result = self.pseudo_random_dice_roll(power)
            self.show_deday_roll_dice(name)
            self.print_dice_side(roll_result)
            return roll_result
        else:
            sleep(1)
            print(f"<*> {name} turn: ")
            while True:
                try:
                    print(f"<?> Fast or slow rolling, {name}?")
                    direction_msg = "-> Enter power from 1 to 100"
                    direction_msg += " (enter sur to surrender):"
                    player_input = input(direction_msg)
                    if player_input.lower() == "sur":
                        return player_input
                    else:    
                        player_input = int(player_input)
                        if player_input < 1:
                            print("Roll please!")
                        elif player_input > 100:
                            print("You use to much power. The dice was broken.")
                        else:
                            roll_result = self.pseudo_random_dice_roll(player_input)
                            self.show_deday_roll_dice(name)
                            self.print_dice_side(roll_result)
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

    def show_deday_roll_dice(self, p_name):
        print(f"\t{p_name} rolling", end='')
        for i in range(0, 4):
            if i < 3:
                print('.', end='')
                sleep(0.4)
            else:
                print()

    def print_dice_side(self, side):
        side_1 =  "\t --------- \n"
        side_1 += "\t|         |\n"
        side_1 += "\t|    o    |\n"
        side_1 += "\t|         |\n"
        side_1 += "\t --------- \n"

        side_2 =  "\t --------- \n"
        side_2 += "\t|  o      |\n"
        side_2 += "\t|         |\n"
        side_2 += "\t|      o  |\n"
        side_2 += "\t --------- \n"

        side_3 =  "\t --------- \n"
        side_3 += "\t| o       |\n"
        side_3 += "\t|    o    |\n"
        side_3 += "\t|       o |\n"
        side_3 += "\t --------- \n"

        side_4 =  "\t --------- \n"
        side_4 += "\t|  o   o  |\n"
        side_4 += "\t|         |\n"
        side_4 += "\t|  o   o  |\n"
        side_4 += "\t --------- \n"

        side_5 =  "\t --------- \n"
        side_5 += "\t| o     o |\n"
        side_5 += "\t|    o    |\n"
        side_5 += "\t| o     o |\n"
        side_5 += "\t --------- \n"

        side_6 =  "\t --------- \n"
        side_6 += "\t|  o   o  |\n"
        side_6 += "\t|  o   o  |\n"
        side_6 += "\t|  o   o  |\n"
        side_6 += "\t --------- \n"

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
        