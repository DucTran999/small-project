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
    
    def draw_map(self,
                 p1_name, p1_hippo_has, p1_hippo_finished, p1_box,
                 p2_name, p2_hippo_has, p2_hippo_finished, p2_box):
        print("#-------------------------------Match-------------------------------#")
        self.show_player_process(p1_name, p1_hippo_has, p1_box, p1_hippo_finished)
        print(".___________________________________________________________________.")
        self.show_player_process(p2_name, p2_hippo_has, p2_box, p2_hippo_finished)
        print("#-------------------------------------------------------------------#")
    
    def show_player_process(self, name, hippo_has, box, hippo_finished):
        print(f"Player: {name}", end='\n')
        print(f"Has: {hippo_has}")
        self.draw_race(box)
        print(f"{name}'s hippo finished race: {hippo_finished}")
        
    def draw_race(self, box_classified):
        special_gift = box_classified[0]
        danger_box = box_classified[1]
        for i in range(1, 13):
            if i in special_gift:
                print("_?_", end='  ')
            elif i in danger_box:
                print("_!_", end='  ')
            else:
                print("___", end='  ')
        print("FINISH\n")