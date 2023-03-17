from main.player.player import Player
from main.seahorse.seahorse import Seahorse
from main.seahorse.filter_seahorse_service import FilterSeahorseService


class PlayerService:
    
    def __init__(self) -> None:
        self.filter_service = FilterSeahorseService()
    
    def create_player(self, name: str) -> Player:
        seahorses = [Seahorse(seahorse_id) for seahorse_id in range(1, 4)]
        return Player(name, seahorses)
    
    def is_player_has_seahorse_available_for_race(self, seahorses) -> list[int]:
        seahorses_id = self.filter_service.get_seahorses_available_id_list(seahorses)
        return True if seahorses_id else False
    
    def is_box_event_apply_to_player(self, box_event: str) -> bool:
        events = ('more roll', 'lost turn')
        return True if box_event in events else False
    
    def handle_player_get_box_event(self, player: Player, event_name: str,
                                    event_value: int) -> None:
        if event_name == 'lost turn' or event_name == 'more roll':
            player.turn_remain += event_value
