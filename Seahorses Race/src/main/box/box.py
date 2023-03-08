from dataclasses import dataclass

@dataclass
class Box:
    """This class describe a box"""
    position: int
    box_type: str
    description: str
    event_name: str
    event_value: int
    
    def __repr__(self) -> str:
        return f"Event: {self.description}\n"
