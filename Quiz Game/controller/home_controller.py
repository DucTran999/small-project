from view.home_view import HomeView
from model.home_model import HomeModel
from utils.function_helper import FunctionHelper

from view.game_view import GameView
from model.game_model import GameModel
from .game_controller import GameController

from view.management_view import ManagementView
from model.management_model import ManagementModel
from .management_controller import ManagementController


class HomeController:
    """Operating activities at Home Screen.
     
    This class handles user requests by tasks. It also distributes data for Home
    View to display and transport data for Home Model to process.
    """
    
    def __init__(self, home_view: HomeView, home_model: HomeModel) -> None:
        self.home_v = home_view
        self.home_m = home_model

    def run(self):
        """Display the menu and fulfill the user's request."""
        while True:
            user_choice = self.home_v.display_home_screen()
            self.handle_user_choice(user_choice)
    
    def handle_user_choice(self, user_choice: int) -> None:
        if user_choice == 1:
            self.handle_new_game_option()
        elif user_choice == 2:
            self.handle_manage_option()
        elif user_choice == 3:
           self.handle_guideline_option()
        elif user_choice == 4:
            self.handle_exit_option()
    
    def handle_new_game_option(self):
        FunctionHelper.clear_console()
        game_view = GameView()
        game_model = GameModel()
        game_controller = GameController(game_view, game_model)
        game_controller.run()
    
    def handle_manage_option(self):
        FunctionHelper.clear_console()
        management_view = ManagementView()
        management_model = ManagementModel()
        management_controller = ManagementController(management_view,
                                                     management_model)
        management_controller.run()
    
    def handle_guideline_option(self):
        FunctionHelper.clear_console()
        guideline = self.home_m.get_guideline()
        if guideline != None:
            self.home_v.display_guideline(guideline)
    
    def handle_exit_option(self):
        FunctionHelper.clear_console()
        self.home_v.display_bye_message()
        exit()