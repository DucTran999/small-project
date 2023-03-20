from dataclasses import dataclass

@dataclass
class Box:
    """This class describe a box"""
    position: int
    event_type: str
    description: str
    event_name: str
    event_value: int    
    
    def display_box(self):
        box_art = {
            'mystery': ("┌───────────┐",
                        "│───────────│",
                        "│  Mystery  │",
                        "│  ? ? ? ?  │",
                        "└───────────┘"
                        ),
            'danger':  ("┌───────────┐",
                        "│───────────│",
                        "│   Danger  │",
                        "│   ! ! !   │",
                        "└───────────┘"
                        )
        }
        for art_line in box_art.get(self.event_type):
            print(f'\t\t{art_line}')
        print(f"Event: {self.description}")