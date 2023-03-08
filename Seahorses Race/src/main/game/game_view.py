from home.view import ViewBaseClass

from utils.validation import Validation

class GameView(ViewBaseClass):
    """Providing methods for presenting data and get user input at Game Screen"""
    
    def print_menu(self):
        options = {
            1:'Single Player',
            2:'Two Player',
            3: 'Back'
        }
        print(f"{'Chose Game Mode':-^60}")
        for id, content in options.items():
            option = f"{id}. {content}"
            print(f"{option: ^60}")
    
    def get_user_option(self) -> str:
        valid_option = ('1', '2', '3')
        return Validation.get_user_option(valid_option, "=> Enter option: ")
