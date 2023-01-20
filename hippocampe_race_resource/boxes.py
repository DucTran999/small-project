class Box:

    def __init__(self, position, type):
        self.position = position
        self.type = type
    
    def __str__(self) -> str:
        return f"pos: {self.position}, type: {self.type}"
    
    def get_pos(self):
        return self.position
    
    def get_type(self):
        return self.type
    
    def convert_type_to_signal(self, type_string):
        if type_string == 'mystery':
            return '_?_'
        elif type_string == 'danger':
            return '_!_'