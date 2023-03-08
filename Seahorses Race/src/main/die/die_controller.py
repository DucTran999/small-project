from die.die import Die
from die.die_view import DieView
from die.die_service import DieService

from utils.function_helper import FunctionHelper


class DieController:
    
    def __init__(self) -> None:
        self.die = Die()
    
    def handle_player_roll_die(self):
        die_face = DieService.roll_dice(self.die)
        FunctionHelper.delay_with_announcement("Die rolling", 2)
        DieView.print_dice_face(die_face)
        return die_face