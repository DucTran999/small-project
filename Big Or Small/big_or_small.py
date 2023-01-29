# -*- coding: utf-8 -*- 

from big_or_small_resource.screens import Screen
from big_or_small_resource.validates import Validate
from big_or_small_resource.games import Game

class BigOrSmall:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        self.screens = Screen()
        self.games = Game(self)

    def run_game(self):
        """ Game control
            1: 'New Game.'
            2: 'View Top 10.'
            3: 'Load Gameplay'
            4: 'Exit/Quit.'
        """

        while True:
            self.screens._main_menu_screen()
            player_choice = Validate().validate_player_choice()
            if player_choice == 1:
                self.games._handle_new_game_option()
            elif player_choice == 2:
                print("Record")
            elif player_choice == 3:
                self.games._handle_gameplay_option()
            else:
                self.games._handle_exit_option()

if __name__ == '__main__':
    # Make a game instance and run the game.
    bos = BigOrSmall()
    bos.run_game()