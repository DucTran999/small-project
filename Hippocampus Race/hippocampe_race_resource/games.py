import json

from . players import Player
from . races import Race
from . dice_side import Dice
from random import choice

class Game:
    
    def __init__(self, hr_game):
        self.hr_game = hr_game
        self.validates = hr_game.validates
        self.game_screen = hr_game.screens
        self.dice = Dice()
        
    def create_new_game(self, game_mode):
        if game_mode == '1 player':
            self.start_single_game(game_mode)
        elif game_mode == '2 players':
            self.start_multi_game(game_mode)

        
    def start_single_game(self, game_mode):
        """ Processing flow:
            1. create player profile
            2. create race
            3. Looping:
                roll dice
                update_hippo_list()
                show round result
        """
        # Create player profile
        players = self.create_player_profile(game_mode)
        p1_name = players[0].get_name()
        p2_name = players[1].get_name()
        print(f"\t\t\t{p1_name} vs {p2_name}")
        
        # Create player races:
        p1_race = Race(p1_name)
        self.game_screen.show_deday_create_race(p1_name)
        self.game_screen.show_player_process(p1_race)
        p2_race = Race(p2_name)
        self.game_screen.show_deday_create_race(p2_name)
        self.game_screen.show_player_process(p2_race)
        boxes_event = self.load_box_event()
        
        game_finished = False
        surrender_flag = 0
        rnd = 1 
        while not game_finished:
            # Player 1's turn

            while players[0].get_dice_roll() > 0:
                # Rolling dice:
                dice_face = self.dice.roll_dice(p1_name)
                if dice_face == "sur":
                    print(f"\t\t{p1_name} SURRENDER!")
                    surrender_flag = 1
                    break
                # Update hippo list
                p1_hpl = players[0].get_hippo_list()
                p1_boxes = p1_race.get_boxes()
                hp1_update = self.hanle_dice_side(dice_face, p1_hpl)
                if hp1_update:
                    players[0].update_hippo_list(hp1_update, p1_boxes,
                                             dice_face, boxes_event)
                players[0].decrease_dice_roll()
            
            # Computer turn
            if surrender_flag == 1:
                ptext = f"FINAL RESULT"
                print(f"#{ptext:-^74}#")    
                print(f"\t\t<_______________ The {p2_name} WIN_________________>")
                print("-" * 78)
                break

            while players[1].get_dice_roll() > 0:
                # Rolling dice:
                dice_face = self.dice.roll_dice(p2_name, 1)
                # Update hippo list
                p2_hpl = players[1].get_hippo_list()
                p2_boxes = p2_race.get_boxes()
                hp2_update = self.hanle_dice_side(dice_face, p2_hpl, 1)
                if hp2_update:
                    players[1].update_hippo_list(hp2_update, p2_boxes,
                                             dice_face, boxes_event)
                players[1].decrease_dice_roll()
            
            #show round result
            self.draw_map(p1_race, p2_race, players[0], players[1], rnd)
            
            # update p1 & p2 turn
            check_p1 = players[0].is_valid_player()
            check_p2 = players[1].is_valid_player()
            if check_p1:
                players[0].increase_dice_roll()
            if check_p2:
                players[1].increase_dice_roll()
            if not check_p1 and not check_p2:
                ptext = f"FINAL RESULT"
                print(f"#{ptext:-^74}#")
                p1_finished = players[0].count_finished_hippo()
                p2_finished = players[1].count_finished_hippo()
                if p1_finished == p2_finished:
                    print("\t\t_____________DRAW GAME______________")
                elif p1_finished > p2_finished:
                    print(f"\t\t<____________ P1: {p1_name} WIN ___________>")
                else:
                    print(f"\t\t<____________ P2: {p2_name} WIN ___________>")
                print("-" * 80)
                game_finished = True
            rnd += 1
    
    
    def start_multi_game(self, game_mode):
        """ Processing flow:
            1. create player profile
            2. create race
            3. Looping:
                roll dice
                update_hippo_list()
                show round result
        """
        
        # Create player profile
        players = self.create_player_profile(game_mode)
        p1_name = players[0].get_name()
        p2_name = players[1].get_name()
        print(f"\t\t\t{p1_name} vs {p2_name}")
        
        # Create player races:
        p1_race = Race(p1_name)
        self.game_screen.show_deday_create_race(p1_name)
        self.game_screen.show_player_process(p1_race)
        p2_race = Race(p2_name)
        self.game_screen.show_deday_create_race(p2_name)
        self.game_screen.show_player_process(p2_race)
        boxes_event = self.load_box_event()
        
        game_finished = False
        surrender_flag = 0
        # surrender_flag: p1: 1, p2 = 2
        rnd = 1 
        while not game_finished:
            # Player 1's turn
            while players[0].get_dice_roll() > 0:
                # Rolling dice:
                dice_face = self.dice.roll_dice(p1_name)
                if dice_face == "sur":
                    print(f"\t\t{p1_name} SURRENDER!")
                    surrender_flag = 1
                    break
                # Update hippo list
                p1_hpl = players[0].get_hippo_list()
                p1_boxes = p1_race.get_boxes()
                hp1_update = self.hanle_dice_side(dice_face, p1_hpl)
                if hp1_update:
                    players[0].update_hippo_list(hp1_update, p1_boxes,
                                             dice_face, boxes_event)
                players[0].decrease_dice_roll()
            
            #Player 2's turn
            if surrender_flag == 1:
                ptext = f"FINAL RESULT"
                print(f"#{ptext:-^74}#")    
                print(f"\t\t<_______________ P2: {p2_name} WIN _________________>")
                print("-" * 78)
                break
            
            while players[1].get_dice_roll() > 0:
                # Rolling dice:
                dice_face = self.dice.roll_dice(p2_name)
                if dice_face == "sur":
                    print(f"\t\t{p2_name} SURRENDER!")
                    surrender_flag = 2
                    break
                # Update hippo list
                p2_hpl = players[1].get_hippo_list()
                p2_boxes = p2_race.get_boxes()
                hp2_update = self.hanle_dice_side(dice_face, p2_hpl)
                if hp2_update:
                    players[1].update_hippo_list(hp2_update, p2_boxes,
                                             dice_face, boxes_event)
                players[1].decrease_dice_roll()
            
            if surrender_flag == 2:
                ptext = f"FINAL RESULT"
                print(f"#{ptext:-^74}#")    
                print(f"\t\t<_______________ P1: {p1_name} WIN _________________>")
                print("-" * 78)
                break
            
            #show round result
            self.draw_map(p1_race, p2_race, players[0], players[1], rnd)
            
            # update p1 & p2 turn
            check_p1 = players[0].is_valid_player()
            check_p2 = players[1].is_valid_player()
            if check_p1:
                players[0].increase_dice_roll()
            if check_p2:
                players[1].increase_dice_roll()
            if not check_p1 and not check_p2:
                self.game_screen.show_deday_result()
                ptext = f"FINAL RESULT"
                print(f"#{ptext:-^74}#")
                p1_finished = players[0].count_finished_hippo()
                p2_finished = players[1].count_finished_hippo()
                if p1_finished == p2_finished:
                    print("\t\t_____________DRAW GAME______________")
                elif p1_finished > p2_finished:
                    print(f"\t\t<____________{p1_name} WIN___________>")
                else:
                    print(f"\t\t<____________{p2_name} WIN___________>")
                print("-" * 80)
                game_finished = True
            rnd += 1

    def load_box_event(self):
        file_path = "hippocampe_race_resource/box_event.json"
        try:
            with open(file_path, 'r') as file_obj:
                contents = json.load(file_obj)
        except Exception as e:
            print("<!> Some problems was occured when loading box_event file")
            print(f"<!> Error_name: {e}")
        else:
            boxes = self.classify_box_event(contents)
            return boxes


    def classify_box_event(self, boxes):
        danger_boxes = []
        mystery_boxes = []
        
        for box in boxes:
            for box_key, box_value in box.items():
                if box_key == "mystery":
                    mystery_boxes.append(box)
                    break
                else:
                    danger_boxes.append(box)
                    break
        return [mystery_boxes, danger_boxes]


    def create_player_profile(self, game_mode):
        if game_mode == '1 player':
            """validate player input and create player profile.""" 
            p1_name = self.validates.validate_player_name()
            p1 = Player(p1_name.title())
            p2 = Player("Computer")
            return [p1, p2]
        elif game_mode == '2 players':
            print("P1", end=' ')
            p1_name = self.validates.validate_player_name()
            print("P2", end=' ')
            p2_name = self.validates.validate_player_name()
            p1 = Player(p1_name.title())
            p2 = Player(p2_name.title())
            return [p1, p2]

    
    def hanle_dice_side(self, dice_side, hpl, computer_flag=0):
        """Determine which hippocampus will be update."""
        if dice_side == 6:
            hippo_chosen = self.get_dice_6_event(hpl, computer_flag)
            return hippo_chosen
        else:
            hippo_chosen = self.get_other_dice_side_event(hpl, dice_side, 
                                                          computer_flag)
            return hippo_chosen

    
    def get_dice_6_event(self, hpl, computer_flag):
        hpl_valid = self.hippo_valid_filter(hpl, 1)
        if computer_flag == 1:
            return choice(hpl_valid)
        else:    
            msg = "<?> Dice 6 allow move 1 hippo to start or move 6 steps!\n"
            msg += "-> Enter hippo order (1, 2, etc.): "
            while True:
                try: 
                    p_choice = int(input(msg))
                    if p_choice in hpl_valid:
                        return p_choice
                    else:
                        print(f"<!> Hippo {p_choice} is not valid!")
                except ValueError:
                    print("<!> Enter number only!")


    def get_other_dice_side_event(self, hpl, dice_side, computer_flag):
        hpl_valid = self.hippo_valid_filter(hpl, 0)
        if computer_flag == 1:
            if len(hpl_valid):
                return choice(hpl_valid)
            else:
                print("I don't have hippo ready for the race!")
                return None
        else:
            if len(hpl_valid):
                msg = f"<?> Hippo can move {dice_side} steps.\n"
                msg += "-> Enter hippo order (1, 2, etc.): " 
                while True:
                    try:
                        p_choice = int(input(msg))
                    except ValueError:
                        print("Enter number only!")
                    else:
                        if p_choice in hpl_valid:
                            return p_choice
                        else:
                            print(f"Hippo {p_choice} is not valid!")
            else:
                print("You don't have hippo ready for the race!")
                return None


    def hippo_valid_filter(self, hpl, event_6_mark):
        """Return list hippo are conditioned
            event_6_mark: is variable I use for separating event 6 and others.
            So this function can call by all event dice.
        """

        hippo_valid = []
        print("<?> Hippo valid:")
        for hp in hpl:
            if event_6_mark == 1:
                if hp.get_state_code() == -1:
                    print(f"\t<i> Hippo {hp.get_order()} is warming up!")
                    hippo_valid.append(hp.get_order())
            if hp.get_state_code() == 0:
                print(f"\t<i> Hippo {hp.get_order()} is ready at the start!")
                hippo_valid.append(hp.get_order())
            elif hp.get_state_code() == 4:
                print(f"\t<i> Hippo {hp.get_order()} is at steps {hp.get_position()}!")
                hippo_valid.append(hp.get_order())
        return hippo_valid

    def draw_map(self, p1_race, p2_race, p1, p2, round):
        text = f"ROUND {round}"
        print(f"#{text:-^74}#")
        self.game_screen.show_player_process(p1_race)
        p1.show_hippo_list()
        print(f".{'_' * 74}.")
        self.game_screen.show_player_process(p2_race)
        p2.show_hippo_list()
        print(f"#{'-' * 74}#")

    