import sys

from home.home_view import HomeView
from home.home_service import HomeService

from game.game_controller import GameController

from utils.function_helper import FunctionHelper

class HomeController:
    """Interacting with user by HomeView and fulfill their request."""
    def __init__(self) -> None:
        """The HomeController constructor
        
        Instance attribute
        - home_v: The HomeView instance used for presenting data
        - home_s: The HomeService instance used for manipulating data
        """
        self.home_v = HomeView()
        self.home_s = HomeService()
    
    def run(self):
        """Operating activities of HomeController
        
        Workflow:
        - Display home screen.
        - Get user request
        - Handle request.
        
        Sub-method:
        - handle_user_option: fulfill user request.
        """
        while True:
            self.home_v.display_screen()
            user_option = self.home_v.get_user_option()
            self.handle_user_option(user_option)
    
    def handle_user_option(self, user_option: int):
        FunctionHelper.clear_screen()
        if user_option == '1':
            self.handle_new_game_option()
        elif user_option == '2':
            self.handle_guideline_option()
        else:
            self.handle_exit_option()
    
    def handle_new_game_option(self):
        game_c = GameController()
        game_c.run()
    
    def handle_guideline_option(self):
        guideline = self.home_s.get_guideline()
        if guideline:
            self.home_v.display_guideline(guideline)
            FunctionHelper.clear_screen() 
    
    def handle_exit_option(self):
        self.home_v.display_bye_message()
        sys.exit()