from time import time
from random import randint, seed

from . boxes import Box

class Race:
    
    def __init__(self, owner):
        self.owner = owner
        self.boxes = self.create_boxes()

    def get_owner(self):
        return self.owner
    
    def get_boxes(self):
        return self.boxes

    def set_boxes(self, boxes):
        self.boxes = boxes
    
    def show_boxes(self):
        for box in self.boxes:
            print(str(box))
    
    def create_boxes(self, salt='1999'):
        """Diffusion variable is used for pseudo random more likely random,
            then we will have random number of box and their position and type.
            salt is a string-number which use to create diffusion variable. 
        """
        quantity = self.generate_box_quantity(salt)
        boxes = self.generate_boxes(quantity, salt)
        return boxes
    
    def generate_box_quantity(self, salt):
        # generate number of boxes.
        diffusion_var = int(time()) + len(salt)
        seed(diffusion_var + int(time()) + int(salt))
        quantity = randint(1, 4)
        return quantity

    def generate_boxes(self, quantity, salt):
        # list of box position:
        boxes_pos = self.distribute_boxes(quantity, salt)
        boxes_classified = self.box_classify(boxes_pos)        
        return boxes_classified


    def distribute_boxes(self, quantity, salt):
        diffusion_var = int(time()) + len(salt)
        seed(diffusion_var + int(time()) + int(salt))
        posistions = []
        count_box = 0
        while count_box < quantity:
            box_pos = randint(1, 12)
            # if state prevent duplicate box.
            if box_pos not in posistions:
                posistions.append(box_pos)
                count_box += 1 
        return posistions
    
    def box_classify(self, boxes_pos):
        """Type of boxes are depend on their index:
                odd: danger box
                even: mystery box
            Ex:  1  2  3  4
            pos [3, 9, 4, 1] -> 9 and 1 are mystery box, 3 and 4 are danger box 
        """
        boxes_classified = []
        for index, box_pos in enumerate(boxes_pos):
            if index % 2 == 0:
                box_tmp = Box(box_pos, 'mystery')
                boxes_classified.append(box_tmp)
            else:
               box_tmp = Box(box_pos, 'danger')
               boxes_classified.append(box_tmp) 
        return boxes_classified
