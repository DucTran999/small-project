from time import sleep

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


    def show_player_process(self, p_race):
        p_name = p_race.get_owner()
        print(f"Player: {p_name}", end='\n')
        self.draw_race(p_race)
        self.show_steps_mark()

    
    def show_deday_create_race(self, p_name):
        print(f"\tCreating race for {p_name}", end='')
        for i in range(0, 5):
            if i < 4:
                print('.', end='')
                sleep(0.6)
            else:
                print()

    def show_deday_result(self):
        print(f"\tWaiting for last result", end='')
        for i in range(0, 5):
            if i < 4:
                print('.', end='')
                sleep(0.6)
            else:
                print()

    def draw_race(self, p_race):
        race = ['___'] * 14
        race[0] = 'START:'
        race[13] = 'FINISH'
        for box in p_race.get_boxes():
            box_pos = box.get_pos()
            box_type = box.convert_type_to_signal(box.get_type())
            race[box_pos] = box_type
        for step in race:
            print(step, end='  ')
        print()


    def show_steps_mark(self):
        print("Steps: ", end='  ')
        for step in range(1, 9):
            print(step, end='    ')
        for step in range(9, 13):
            print(step, end='   ')
        print()

    
    def show_hpl(self, hpl):
        for hp in hpl:
            print(str(hp))