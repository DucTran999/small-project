class Setting:
    """ class Settings responsible for all settings for the game:
        
    Features list:
        Load gameplay
        Change game mode: 1 player vs computer and 2 players.
        Get and Set game mode. (default game mode is single player.)
    Additional infomation: 'hp' is stand for hippocampus.
    """
    
    def __init__(self, mode='1 player'):
        self.mode = mode
    
    def set_game_mode(self, mode):
        self.mode = mode
    
    def get_game_mode(self):
        return self.mode
    
    def load_gameplay(self):
        """Load the gameplay from file in folder gameplay"""
        
        try:
            hp_gameplay_path = 'gameplay/hippocampe_gameplay.txt'
            with open(hp_gameplay_path) as file_obj:
                hp_gameplay = file_obj.read()
                print(hp_gameplay)
        except Exception as e:
            print("Some promblem has been occured while loading gameplay!")
            print(f"Error name: {e}")
    
    def change_game_mode(self, player_choice):
        """Change game mode"""
        
        mode_1, mode_2 = "1 player", "2 players"
        if player_choice == 1:
            self.set_game_mode(mode_1)
            print(f"Game mode is set to {mode_1}!")
        elif player_choice == 2:
            self.set_game_mode(mode_2)
            print(f"Game mode is set to {mode_2}!")
