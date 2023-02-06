class View:
    
    def render_banner(self) -> None:
        banner = (
                "\t ____  _     _  ____  _____ ____  _      _____ \n"
                "\t/  _ \/ \ /\/ \/_   \/  __//  _ \/ \__/|/  __/ \n"
                "\t| / \|| | ||| | /   /| |  _| / \|| |\/|||  \   \n"
                "\t| \_\|| \_/|| |/   /_| |_//| |-||| |  |||  /_  \n"
                "\t\____/\____/\_/\____/\____/\_/ \|\_/  \|\____\ \n"
                )
        print(banner)
    
    def render_menu(self):
        pass
    
    def display_announcement(self, announcement: str) -> None:
        print(announcement)
    
    def display_error(self, error_message: str) -> None:
        print(error_message)
