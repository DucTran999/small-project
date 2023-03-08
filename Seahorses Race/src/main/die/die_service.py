import secrets

from die.die import Die

class DieService:
    
    @classmethod
    def roll_dice(cls, dice: Die):
        return secrets.choice(dice.faces)