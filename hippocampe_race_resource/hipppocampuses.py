class Hippocampus:
    
    def __init__(self, order, state_code, position, owner):
        self.order = order
        self.state_code = state_code
        self.position = int(position)
        self.owner = owner
    
    def __str__(self) -> str:
        if self.position < 13:
            info = f"Order: {self.order} - "
            info += f"State: {self.convert_state_to_string(self.state_code)} - "
            info += f"At step: {self.position} "
        else:
            info = f"Order: {self.order} - "
            info += f"State: {self.convert_state_to_string(self.state_code)}"
        return info
    
    def get_order(self):
        return self.order
    
    def get_state_code(self):
        return self.state_code
    
    def get_position(self):
        return self.position
    
    def get_owner(self):
        return self.owner
    
    def set_position(self, steps):
        self.position = steps
    
    def set_state_code(self, new_code):
        self.state_code = new_code
        
    def update_new_pos(self, steps):
        new_pos = self.position + int(steps)
        self.set_position(new_pos)
    
    def update_finished(self):
        if self.get_position() > 12:
            self.set_position(13)
            self.state_code = 1
    
    def check_get_box(self, boxes):
        cur_pos = self.get_position()
        for box in boxes:
            if box.get_pos() == cur_pos:
                hippo_state = self.check_box_type(box)
                self.set_state_code(hippo_state)
                
    def check_box_type(self, box):
        box_type = box.get_type()
        if box_type == 'mystery':
            return 2
        else:
            return 3
        
    def get_string_state(self):
        return self.convert_state_to_string(self.state_code)
    
    def convert_state_to_string(self, state_code):
        if state_code == -1:
            return "Warm up"
        elif state_code == 0:
            return "At START"
        elif state_code == 1:
            return "Finished"
        elif state_code == 2:
            return "Mistery Box"
        elif state_code == 3:
            return "Missing"
        elif state_code == 4:
            return "Racing"