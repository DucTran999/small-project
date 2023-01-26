from . hipppocampuses import Hippocampus
from random import choice

class Player:
    
    def __init__(self, name):
        self.name = name
        self.hippo_list = self.init_hippo_list()
        self.dice_roll = 1

    
    def set_name(self, name):
        self.name = name

    
    def get_dice_roll(self):
        return self.dice_roll

    
    def increase_dice_roll(self):
        self.dice_roll += 1


    def decrease_dice_roll(self):
        self.dice_roll -= 1


    def roll_dice_event(self, dice):
        self.dice_roll += dice


    def get_name(self):
        return self. name


    def get_hippo_list(self):
        return self.hippo_list


    def show_hippo_list(self):
        print("<i> Hippocampus list:")
        for hippo in self.hippo_list:
            print(str(hippo))


    def init_hippo_list(self):
        hippo_list = []
        for i in range(1, 4):
            hippo_i = Hippocampus(i, -1, 0, self.name)
            hippo_list.append(hippo_i)
        return hippo_list


    def is_valid_player(self):
        """This function check player have hippo can race or racing.
            so we can give player dice roll turn.
        """

        for hp in self.hippo_list:
            hp_state = hp.get_state_code()
            if hp_state == -1 or hp_state == 4 or  hp_state == 0:
                return True
        return False        

    def count_finished_hippo(self):
        count = 0
        for hp in self.hippo_list:
            if hp.get_state_code() == 1:
                count += 1
        return count   
    
    def update_hippo_list(self, hp_need_upd,
                          p_box,steps, box_event):
        # get hippocampus info
        hp_ind = hp_need_upd - 1 
        hp_state_code = self.hippo_list[hp_ind].get_state_code()
        #Handle the event they got. (It's depend on their state)
        if hp_state_code == -1: 
            self.hippo_list[hp_ind].set_state_code(0)
        elif hp_state_code  == 0:
            self.hippo_list[hp_ind].set_state_code(4)
            self.hippo_list[hp_ind].update_new_pos(steps)
            box_type = self.hippo_list[hp_ind].check_get_box(p_box)
            self.handle_event(box_event, box_type,hp_ind)
        elif hp_state_code  == 4:
            self.hippo_list[hp_ind].update_new_pos(steps)
            box_type = self.hippo_list[hp_ind].check_get_box(p_box)
            self.hippo_list[hp_ind].update_finished()
            self.handle_event(box_event, box_type, hp_ind)
        print(str(self.hippo_list[hp_ind]))


    def handle_event(self, box_event, box_type, hp_ind):
        """Choose event randomly by box type
            event structure:{
                type : event_smg
                action : value
            }
            action: increase or descrease dice roll turn or change hippo state 
        """
        
        if box_type == "mystery":
            rand_event = choice(box_event[0])
            rand_event_key = list(rand_event.keys())
            event_msg = rand_event.get(rand_event_key[0])
            print(event_msg)
            if rand_event_key[1] == "state_set":
                state_code = rand_event.get(rand_event_key[1])
                self.hippo_list[hp_ind].set_state_code(state_code)
            elif rand_event_key[1] ==  "dice_roll":
                dice_roll = rand_event.get(rand_event_key[1])
                self.roll_dice_event(dice_roll)
            elif rand_event_key[1] =="more_step":
                steps = rand_event.get(rand_event_key[1])
                self.hippo_list[hp_ind].update_new_pos(steps)
        elif box_type == "danger":
            rand_event = choice(box_event[1])
            rand_event_key = list(rand_event.keys())
            event_msg = rand_event.get(rand_event_key[0])
            print(event_msg)
            if rand_event_key[1] == "state_set":
                state_code = rand_event.get(rand_event_key[1])
                self.hippo_list[hp_ind].set_state_code(state_code)
            elif rand_event_key[1] ==  "dice_roll":
                dice_roll = rand_event.get(rand_event_key[1])
                self.roll_dice_event(dice_roll)