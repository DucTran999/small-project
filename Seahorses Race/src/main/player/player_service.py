from main.player.player import Player
from main.seahorse.filter_seahorse_service import FilterSeahorseService


class PlayerService:
    
    def __init__(self) -> None:
        self.filter_service = FilterSeahorseService()
    
    def is_player_has_seahorse_available_for_race(self, seahorses) -> list[int]:
        seahorses_id = self.filter_service.get_seahorses_available_id_list(seahorses)
    def is_player_has_seahorse_available_for_race(self, seahorses) -> list[int]:
        seahorses_id = self.filter_service.get_seahorses_available_id_list(seahorses)
        return True if seahorses_id else False
    
    def is_box_event_apply_to_player(self, box_event: str) -> bool:
    def is_box_event_apply_to_player(self, box_event: str) -> bool:
        events = ('more roll', 'lost turn')
        return True if box_event in events else False
    
    def handle_player_get_box_event(self, player: Player, event_name: str,
                                    event_value: int) -> None:
    def handle_player_get_box_event(self, player: Player, event_name: str,
                                    event_value: int) -> None:
        if event_name == 'lost turn' or event_name == 'more roll':
            player.turn_remain += event_value
