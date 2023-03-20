import abc

class ViewBaseClass(metaclass=abc.ABCMeta):
    """Providing basic methods of View
    
    Its Sub-class like HomeView and GameView have to override all methods that 
    have decorator @abc.abstractmethod
    """
    def display_screen(self):
        self.print_banner()
        self.print_menu()
    
    def print_banner(self):
        first_line = (
            "     _____            _                               \n"
            "    / ____|          | |                              \n"
            "   | (___   ___  __ _| |__   ___  _ __ ___  ___  ___  \n"
            "    \___ \ / _ \/ _` | '_ \ / _ \| '__/ __|/ _ \/ __| \n"
            "    ____) |  __/ (_| | | | | (_) | |  \__ \  __/\__ \ \n"
            "   |_____/ \___|\__,_|_| |_|\___/|_|  |___/\___||___/ \n"
        )

        second_line = (
            "\t\t    ____                 \n"
            "\t\t   / __ \____ _________  \n"
            "\t\t  / /_/ / __ `/ ___/ _ \ \n"
            "\t\t / _, _/ /_/ / /__/  __/ \n"
            "\t\t/_/ |_|\__,_/\___/\___/  \n"
        )
        print(first_line, second_line)
    
    @abc.abstractclassmethod
    def print_menu(self):
        pass
    
    @abc.abstractclassmethod
    def get_user_option(self):
        pass