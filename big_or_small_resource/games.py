from sys import exit

from . utilities import Utilization
from . players import Player
from . validates import Validate

class Game:
    """ The Game class will handle all the game processing.
    Basic features:
        1. Create a new game where the player can enjoy the game. 
        2. Show the gameplay which contains guide play.
        3. Showing the top 10 players with the best record. 
    """
    
    def __init__(self, bos_game) -> None:
        self.bos_game = bos_game

    def _handle_new_game_option(self):
        """Create player profile.
        Start new game.
        Update record when player loses the game.
        """
        player = self.__create_player_profile()
        self.__start_new_game(player)

    def __create_player_profile(self) -> Player:
        """Create a player instance"""
        player_name = Validate().validate_player_name()
        player = Player(player_name)
        return player
    
    def __start_new_game(self, player: Player) -> None:
        """Create a new game and start it."""
        print(player.__repr__())
        
    def _handle_gameplay_option(self) -> None:
        """A small time delay and announcement message before clearing 
            the current console and printing the gameplay contents.
        """
        Utilization().delay(0.5, "Loading Gameplay...")
        Utilization.clear_console_screen()
        Utilization().delay(0.2)
        # Read gameplay line by line and present it in the center of the screen
        file_path = "gameplay/big_or_small.txt"
        try: 
            # Encoding utf-8 to read some special character correctly.
            # Example: the heart sympbol (♥)
            with open(file_path, 'r', encoding='utf-8') as gp_file:
                gameplay_contents = gp_file.readlines() 
                for line in gameplay_contents:
                    print(" " * 5, line.strip())  # Print the text in the center
        except Exception as e:
            err_alert = "<!> Some problems occurred while loading the gameplay."
            err_name = f"Error name: {e}"
            print(err_alert, err_name, sep='\n')
    
    def _handle_exit_option(self) -> None:
        """Show goodbye message and terminate the programme."""
        Utilization().delay(0.2)
        Utilization().clear_console_screen()
        self.bos_game.screens._exit_screen()
        exit()