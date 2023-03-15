import secrets

from main.box.box import Box

from main.utils.file_helper import FileHelper


class BoxBuilder:
    """This box responsible for creating a box"""
    def __init__(self) -> None:
        self.file_helper = FileHelper()
        self.events = self.load_box_event()
    
    def load_box_event(self) -> list[dict]:
        """Load all events describe from file."""
        return self.file_helper.read_json_file('box_event') 
    
    def choice_event_for_create_box(self) -> dict:
        return secrets.choice(self.events)

    def create_box(self, pos: int, event: dict) -> tuple:
        box_type = event.get('event_type')
        description = event.get('description')
        event_name = event.get('event_name')
        event_value = event.get('event_value')
        return Box(pos, box_type, description, event_name, event_value)
