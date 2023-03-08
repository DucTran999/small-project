import secrets

from box.box import Box

from utils.file_helper import FileHelper


class BoxService:
    """Manipulate box data"""
    @classmethod
    def load_box_event(cls) -> list[dict]:
        return FileHelper.read_json_file('box_event')    
    
    @classmethod
    def create_box(cls, pos: int, box_events: list[dict]) -> tuple:
        box_event = secrets.choice(box_events)
        box_type = box_event.get('box_type')
        description = box_event.get('description')
        event_name = box_event.get('event_name')
        event_value = box_event.get('event_value')
        return Box(pos, box_type, description, event_name, event_value)
    