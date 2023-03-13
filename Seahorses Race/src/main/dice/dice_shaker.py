import secrets

from main.dice.dice import Dice
from main.utils.function_helper import FunctionHelper

class DiceShaker:
    """This class represent a dice shaker in a match."""
    def __init__(self) -> None:
        self.dice = Dice()
    
    def shake_dice(self) -> int:
        """Get dice face and display it.
        
        To get truly random dice, it is better to use the secret module than the
        random one. 
        See more at: https://docs.python.org/3/library/secrets.html
        """
        FunctionHelper.delay_with_announcement("Shaking dice...", 3)
        face = secrets.choice(self.dice.faces)
        self.display_result(face)
        return face

    def display_result(self, face: int):
        if face == 1:
            print("\t\t┌─────────┐\n",
                  "\t\t│         │\n",
                  "\t\t│    ●    │\n",
                  "\t\t│         │\n",
                  "\t\t└─────────┘\n")
        elif face == 2:
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●      │\n"
                  "\t\t│         │\n"
                  "\t\t│      ●  │\n"
                  "\t\t└─────────┘\n")
        elif face == 3: 
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●      │\n"
                  "\t\t│    ●    │\n"
                  "\t\t│      ●  │\n"
                  "\t\t└─────────┘\n")
        elif face == 4: 
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t│         │\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t└─────────┘\n")
        elif face == 5: 
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t│    ●    │\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t└─────────┘\n")
        elif face == 6: 
            print("\t\t┌─────────┐\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t│  ●   ●  │\n"
                  "\t\t└─────────┘\n")

