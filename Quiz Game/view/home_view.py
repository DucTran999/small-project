from view.view import View
from view.prevent_invalid_input import PreventInvalidInput


class HomeView(View):
    """Manage the presentation of the Home Screen.

    This class is responsible for interacting with the user on the Home screen. 
    The main job is to take user input and display the information owned by Home.
    
    Available method:
    - display_home_screen: show the main menu and get the user option then send 
    it to the Home Controller that handles it.
    - render_menu: the sub-method of home_menu which rendering the home menu.
    - display_guideline.
    - display_bye_message.
    """
    def display_home_screen(self) -> None:
        self.render_banner()
        self.render_menu()
        valid_options = [option for option in range(1, 5)]
        return PreventInvalidInput.user_enter_menu_option(valid_options)
    
    def render_menu(self) -> None:
        name = "home menu"
        options = {
            "1": "New Game",
            "2": "Manage Topic",
            "3": "Guideline",
            "4": "Exit"
            }
        print(f"{name.upper():-^60}")
        for order, option_name in options.items():
            option = f"{order}. {option_name}"
            print(f"{option: ^60}")
    
    def display_guideline(self, guideline: list[str]) -> None:
        if guideline:
            for line in guideline:
               print(line)
        else:
            self.display_announcement("<i> Empty!")
    
    def display_bye_message(self) -> None:
        bye_message = (
            "\t  _____ ____  ____  ____  ____ ___  _ _____ \n"
            "\t /  __//  _ \/  _ \/  _ \/  _ \ \  \///  __/ \n"
            "\t | |  _| / \|| / \|| | \|| | //  \  / |  \   \n"
            "\t | |_//| \_/|| \_/|| |_/|| |_\ \ / /  |  /_  \n"
            "\t \____/\____/\____/\____/\____/ /_/   \____\ \n"
            )
        print(bye_message)