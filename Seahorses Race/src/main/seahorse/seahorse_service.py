from seahorse.seahorse import Seahorse

from box.box import Box

class SeahorseService:
    """Manipulate data of seahorse objects.
    
    This class provides methods to manipulate data of seahorse objects. These 
    methods will be called by the MatchService Class to fulfill some tasks.
    """
    @staticmethod
    def is_seahorse_can_move(seahorse_state: str) -> bool:
        if seahorse_state == 'Ready' or seahorse_state == 'Running':
            return True
        return False
    
    @staticmethod
    def is_seahorse_warm_up(seahorse_state: str) -> bool:
        return True if seahorse_state == 'Warm up' else False
    
    @staticmethod
    def is_seahorse_available_for_race(seahorse_state: str) -> bool:
        if seahorse_state != 'Finish' and seahorse_state != 'Cannot race':
            return True
        return False
    
    @staticmethod
    def get_seahorse_can_move_id_list(seahorses: list[Seahorse])-> list[int]:
        seahorses_valid = list()
        for seahorse in seahorses:
            if SeahorseService.is_seahorse_can_move(seahorse.state):
                seahorses_valid.append(seahorse.seahorse_id)
        return seahorses_valid
    
    @staticmethod
    def get_seahorse_warm_up_id_list(seahorses: list[Seahorse]) -> list[int]:
        seahorse_valid = list()
        for seahorse in seahorses:
            if SeahorseService.is_seahorse_warm_up(seahorse.state):
                seahorse_valid.append(seahorse.seahorse_id)
        return seahorse_valid
    
    @staticmethod
    def get_seahorses_available_for_race(seahorses: list[Seahorse]) -> list[int]:
        seahorse_valid = list()
        for seahorse in seahorses:
            if SeahorseService.is_seahorse_available_for_race(seahorse.state):
                seahorse_valid.append(seahorse.seahorse_id)
        return seahorse_valid
    
    @staticmethod
    def is_seahorse_get_box(seahorse_pos: int, box_positions: list[int]) -> bool:
        return True if seahorse_pos in box_positions else False
    
    @staticmethod
    def is_box_event_apply_to_seahorse(box_event_name: str) -> bool:
        events = ('move to finish', 'move faster', 'get trouble')
        return True if box_event_name in events else False
   
    @staticmethod
    def handle_seahorse_get_box_event(seahorse: Seahorse, 
                                      event_name: str, 
                                      event_value: int
                                      ):
        if event_name == 'get trouble':
            seahorse.state = event_value
            seahorse.position = 0
        elif event_name == 'move faster':
            seahorse.move(event_value)
        elif event_name == 'move to finish':
            seahorse.state = event_value
            seahorse.position = 13
    
    @staticmethod
    def handle_seahorse_get_6_face_event(seahorse: Seahorse, die_face: int):
        if seahorse.state == 'Warm up':
            seahorse.move_to_start()
        else:
            seahorse.move(die_face)

    @staticmethod
    def handle_seahorse_get_not_6_face_event(seahorse: Seahorse, die_face: int):
        seahorse.move(die_face)