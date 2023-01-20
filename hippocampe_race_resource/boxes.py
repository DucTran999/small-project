class Box:

    def __init__(self, position, type):
        self.position = position
        self.type = type
    
    def __str__(self) -> str:
        return f"pos: {self.position}, type: {self.type}"
    
    def convert_type_to_signal(self, type_string):
        if type_string == 'mystery':
            return '?'
        elif type_string == 'danger':
            return '!'