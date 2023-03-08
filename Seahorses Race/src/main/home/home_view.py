from home.view import ViewBaseClass

from utils.validation import Validation


class HomeView(ViewBaseClass):
    """Providing methods for presenting data and get user input at Home Screen""" 
    def print_menu(self) -> None:
        options = {
            1:'New Game',
            2:'Guideline',
            3: 'Exit'
        }
        print(f"{'Home Menu':-^60}")
        for id, content in options.items():
            option = f"{id}. {content}"
            print(f"{option: ^60}")
    
    def get_user_option(self) -> str:
        valid_option = ('1', '2', '3')
        return Validation.get_user_option(valid_option, "=> Enter option: ")

    def display_guideline(self, guideline: str) -> None:
        print(guideline)
        input("Press enter to quit guideline...")
    
    def display_bye_message(self) -> None:
        bye_message = (
            "\t  _____ ____  ____  ____  ____ ___  _ _____ \n"
            "\t /  __//  _ \/  _ \/  _ \/  _ \ \  \///  __/ \n"
            "\t | |  _| / \|| / \|| | \|| | //  \  / |  \   \n"
            "\t | |_//| \_/|| \_/|| |_/|| |_\ \ / /  |  /_  \n"
            "\t \____/\____/\____/\____/\____/ /_/   \____\ \n"
            )
        print(bye_message)