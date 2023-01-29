import sys

from hippocampe_race_resource.game_screen import Screen
from hippocampe_race_resource.validates import Validate
from hippocampe_race_resource.settings import Setting
from hippocampe_race_resource.games import Game

class HippocampusRace:
    
    def __init__(self):
        self.screens = Screen()
        self.validates = Validate()
        self.settings = Setting()
        self.games = Game(self)

    def run_game(self):
        while True:
            game_mode = self.settings.get_game_mode()
            print(f"\t\t-------> {game_mode} <-------")
            self.screens.show_menu("game", "Let's play!", "Settings", "Exit")
            self.hanle_player_choice_main_menu(game_mode)

    def hanle_player_choice_main_menu(self, game_mode):
        player_choice = self.validates.validate_player_choice()
        if player_choice == 1:
            # Start a new game depend on the game mode.
            self.games.create_new_game(game_mode)
        elif player_choice == 2:
            # Move to setting mennu
            self.handle_player_choice_setting_menu()
        else:
            print("Goodbye!")
            sys.exit()
    
    def handle_player_choice_setting_menu(self):
        while True:
            # the while loop to keep showing the setting menu
            self.screens.show_menu("settings",
                                   "load gameplay",
                                   "game mode",
                                   "back")
            player_choice = self.validates.validate_player_choice()
            if player_choice == 1:
                self.settings.load_gameplay()
            elif player_choice == 2:
                self.handle_player_choice_game_mode_menu()
            else:
                break
        
    def handle_player_choice_game_mode_menu(self):
        while True:
            self.screens.show_menu("game mode", 
                                   "1 player", 
                                   "2 players",
                                   "back")
            player_choice = self.validates.validate_player_choice()
            if player_choice == 1:
                self.settings.change_game_mode(1)
            elif player_choice == 2:
                self.settings.change_game_mode(2)
            else:
                break
            
if __name__ == '__main__':
    """Make a game instance and run the game."""
    hp = HippocampusRace()
    hp.run_game()