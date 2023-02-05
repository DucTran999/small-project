class Screen:
    """Class Screen:
    This class manage all screens that interact with the player.
    Essential screens:
        Welcome screen: Show the greeting when player open the game.
        Exit screen: bye player when they chose exit option.
        The main menu screen gives players options to control the game. 
    """
    
    def __init__(self):
        self._welcome_screen()

    def _welcome_screen(self):
        banner = """
                ____  _                        _____                 ____
               / __ )(_)___ _   ____  _____   / ___/____ ___  ____ _/ / /
              / __  / / __ `/  / __ \/ ___/   \__ \/ __ `__ \/ __ `/ / / 
             / /_/ / / /_/ /  / /_/ / /      ___/ / / / / / / /_/ / / /  
            /_____/_/\__, /   \____/_/      /____/_/ /_/ /_/\__,_/_/_/   
                    /____/                                               
        """
        print(banner)
    
    def _exit_screen(self):
        banner = """
                ______                ____             
              / ____/___  ____  ____/ / /_  __  _____ 
             / / __/ __ \/ __ \/ __  / __ \/ / / / _ \\
            / /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/
            \____/\____/\____/\__,_/_.___/\__, /\___/ 
                                         /____/        
        """
        print(banner)

    def _main_menu_screen(self):
        menu_options = {
            1: 'New Game.',
            2: 'View Top 10.',
            3: 'Load Gameplay.',
            4: 'Exit/Quit.'
        }
        # Print Main Menu banner and 4 options follow it.
        text = f"Main Menu"
        print(f"\t  {text:-^60}")
        tabs = '\t' * 4
        for option_num, value in menu_options.items():
            print(f"{tabs}{option_num}. {value}")