from main.seahorse.i_filter_seahorse_service import IFilterSeahorseService
from main.seahorse.seahorse import Seahorse


class FilterSeahorseService(IFilterSeahorseService):
    """Filter seahorses id by specific condition"""
    def is_seahorse_available(self, seahorse_state: str) -> bool:
        return True if seahorse_state != 'Finish' \
                        and seahorse_state != 'Cannot race' \
                    else False
    
    def is_seahorse_can_move(self, seahorse_state: str) -> bool:
        return True if seahorse_state == 'Ready' \
                        or seahorse_state == 'Running' \
                    else False
    
    def is_seahorse_warm_up(self, seahorse_state: str) -> bool:
        return True if seahorse_state == 'Warm up' else False
    
    def get_seahorses_available_id_list(self, 
                                        seahorses: list[Seahorse]) -> list[int]:
        return [seahorse.seahorse_id 
                for seahorse in seahorses 
                if self.is_seahorse_available(seahorse.state)]
    
    def get_seahorse_can_move_id_list(self, 
                                      seahorses: list[Seahorse]) -> list[int]:
        return [seahorse.seahorse_id 
                for seahorse in seahorses
                if self.is_seahorse_can_move(seahorse.state)]
    
    def get_seahorse_warm_up_id_list(self, 
                                     seahorses: list[Seahorse]) -> list[int]:
        return [seahorse.seahorse_id 
                for seahorse in seahorses 
                if self.is_seahorse_warm_up(seahorse.state)]
    