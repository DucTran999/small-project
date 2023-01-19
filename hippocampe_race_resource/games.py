from time import sleep, time
from random import randint, seed

class Game:
    
    def __init__(self, hr_game):
        self.hr_game = hr_game
        self.validates = hr_game.validates
        self.player1 = hr_game.player1
        self.player2 = hr_game.player2
        self.game_screen = hr_game.screens
        
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
        
        self.create_map()
        
    def start_multi_game(self):
        player_name1 = self.validates.validate_player_name()
        player_name2 = self.validates.validate_player_name()
        self.player1.set_name(player_name1)
        self.player2.set_name(player_name2)
        print(f"\t\t\t{self.player1.get_name()} vs {self.player2.get_name()}")
        

    def create_map(self):
        # delay between p1_box_pos and p2_box_pos to ensure they are diff.
        p1_box_pos = self.create_box_in_race(self.player1.get_name())
        self.load_map()
        p2_box_pos = self.create_box_in_race(self.player2.get_name())
        #classify box
        p1_box_type = self.box_classify(p1_box_pos)
        p2_box_type = self.box_classify(p2_box_pos)
                
        # Draw map
        self.game_screen.draw_map(self.player1.get_name(),
                                   self.player1.get_hippo(),
                                   self.player2.get_name(),
                                   self.player2.get_hippo(),
                                   p1_box_type,
                                   p2_box_type)
        
    def load_map(self):
        print("\tLoading map", end='')
        for i in range(0, 5):
            if i < 4:
                print('.', end='')
                sleep(0.6)
            else:
                print()
                
    def create_box_in_race(self, player_name):
        """diffusion var use for pseudo random more likely random,
            then we will have random number of box and their position and type.
            type of box depend on the index oven for sp_gift and odd for danger.
            Ex:  1  2  3  4
            pos [3, 9, 4, 1] -> 9 and 1 are special gift, 3 and 4 are danger box 
        """
        
        diffusion_var = int(time()) + len(player_name)
        seed(diffusion_var + int(time()) + 1999)
        number_of_box = randint(1, 4)

        i = 1
        box_position = []
        seed(int(time()) + 2003)
        while i <= number_of_box:
            new_pos = randint(1, 12)
            if new_pos not in box_position:
                box_position.append(new_pos)
                i += 1
                
        return box_position
    
    def box_classify(self, box_pos):
        special_gift = []
        danger_box = []
        for i, value in enumerate(box_pos):
            if i % 2 == 0:
                special_gift.append(value)
            else:
                danger_box.append(value)
        return [special_gift, danger_box]
        
    