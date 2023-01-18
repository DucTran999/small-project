from time import sleep

class Game:
    
    def __init__(self, hr_game):
        self.hr_game = hr_game
        self.validates = hr_game.validates
        self.player1 = hr_game.player1
        self.player2 = hr_game.player2
        
    def create_new_game(self, game_mode):
        if game_mode == '1 player':
            self.start_single_game()
        elif game_mode == '2 players':
            self.start_multi_game()
        
    def start_single_game(self):
        """validate player input and create player profile."""
        
        player_name = self.validates.validate_player_name()
        self.player1.set_name(player_name)
        self.player2.set_name("Computer")
        print(f"\t\t\t{self.player1.get_name()} vs {self.player2.get_name()}")
        
        self.load_map()
        
        
    def start_multi_game(self):
        player_name1 = self.validates.validate_player_name()
        player_name2 = self.validates.validate_player_name()
        self.player1.set_name(player_name1)
        self.player2.set_name(player_name2)
        print(f"\t\t\t{self.player1.get_name()} vs {self.player2.get_name()}")
        
    def load_map(self):
        print("\tLoading map", end='')
        for i in range(0, 5):
            if i < 4:
                print('.', end='')
                sleep(0.6)
            else:
                print()
    