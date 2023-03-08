from game.game_view import GameView

from match.match_controller import MatchController

from utils.function_helper import FunctionHelper

class GameController:
    """Interacting with user by GameView and fulfill their request."""
    is_running = True
    
    def __init__(self) -> None:
        """The GameController constructor
        
        Instance attribute
        - home_v: The GameView instance used for presenting data
        - home_s: The GameService instance used for manipulating data
        """
        self.game_v = GameView()
        self.match_c = MatchController()
    
    def run(self):
        """Operating activities of GameController
        
        Workflow:
        - Display game screen
        - Get user request
        - Handle request.
        
        Sub-method:
        - handle_user_option: fulfill user request.
        """
        while self.is_running:
            self.game_v.display_screen()
            user_option = self.game_v.get_user_option()
            self.handle_user_option(user_option)
    
    def handle_user_option(self, user_option: str) -> None:
        FunctionHelper.clear_screen()
        if user_option == '1':
            self.handle_single_player_option()
        elif user_option == '2':
            self.handle_two_player_option()
        else:
            self.handle_back_option()

    def handle_single_player_option(self):
        self.match_c.start_single_player_match()
    
    def handle_two_player_option(self):
        self.match_c.start_two_player_match()
    
    def handle_back_option(self) -> None:
        self.is_running = False
            