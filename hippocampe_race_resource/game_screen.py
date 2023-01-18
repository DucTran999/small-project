class Screen:
    """class Screen responsible for interacting to player.

        Essential screen:
        menu: show menu with arguments were passed.
        banner: only user for first time when player open the game.
    """
    def __init__(self):
        self.screen = self.show_banner()
        
    def show_menu(self, menu_name, option1, option2, option3):
        menu =  f"\t\t---------{menu_name.capitalize()} Menu---------\n"
        menu += f"\t\t     1. {option1.capitalize()}\n"
        menu += f"\t\t     2. {option2.capitalize()}\n"
        menu += f"\t\t     3. {option3.capitalize()}\n"
        print(menu)
          
    def show_banner(self):
        banner =  "    __  ___                                      \n"
        banner += "   / / / (_)___  ____  ____  _________ _____ ___  ____  __  _______\n"
        banner += "  / /_/ / / __ \/ __ \/ __ \/ ___/ __ `/ __ `__ \/ __ \/ / / / ___/\n"
        banner += " / __  / / /_/ / /_/ / /_/ / /__/ /_/ / / / / / / /_/ / /_/ (__  ) \n"
        banner += "/_/ /_/_/ .___/ .___/\____/\___/\__,_/_/ /_/ /_/ .___/\__,_/____/  \n"
        banner += "       /_/   /_/                              /_/               \n"

        banner_2 =  "\t\t    ____                 \n"
        banner_2 += "\t\t   / __ \____ _________  \n"
        banner_2 += "\t\t  / /_/ / __ `/ ___/ _ \ \n"
        banner_2 += "\t\t / _, _/ /_/ / /__/  __/ \n"
        banner_2 += "\t\t/_/ |_|\__,_/\___/\___/  \n"
        print(banner, banner_2)
    
    