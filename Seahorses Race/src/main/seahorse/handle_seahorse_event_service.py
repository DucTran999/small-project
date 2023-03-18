from main.seahorse.i_handle_seahorse_event_service import IHandleSeahorseEventService
from main.seahorse.seahorse import Seahorse


class HandleSeahorseEventService(IHandleSeahorseEventService):
    """Manipulate seahorse objects info when they get event"""
    def is_seahorse_get_box(self, seahorse_pos: int,
                            boxes_positions: tuple[int]) -> bool:
        return True if seahorse_pos in boxes_positions else False
    
    def is_box_event_apply_to_seahorse(self, box_event_name: str) -> bool:
        events = ('move to finish', 'move faster', 'get trouble')
        return True if box_event_name in events else False
   
    def update_seahorse_info_get_box_event(self, seahorse: Seahorse, 
                                      event_name: str, 
                                      event_value: int):
        if event_name == 'get trouble':
            seahorse.state = event_value
            seahorse.position = 0
        elif event_name == 'move faster':
            seahorse.move(event_value)
        elif event_name == 'move to finish':
            seahorse.state = event_value
            seahorse.position = 13
    
    def update_seahorse_info_get_face_6_event(self, seahorse: Seahorse,
                                         die_face: int) -> None:
        if seahorse.state == 'Warm up':
            seahorse.move_to_start()
        else:
            seahorse.move(die_face)

    def update_seahorse_info_get_not_face_6_event(self, seahorse: Seahorse,
                                             die_face: int) -> None:
        seahorse.move(die_face)