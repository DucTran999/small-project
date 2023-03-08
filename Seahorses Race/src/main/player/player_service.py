from player.player import Player
from seahorse.seahorse import Seahorse
from seahorse.seahorse_service import SeahorseService


class PlayerService:
    """"""
    @staticmethod
    def create_player(name: str) -> Player:
        seahorses = list()
        for id in range(1, 4):
            seahorses.append(Seahorse(id))
        return Player(name, seahorses)
    
    @staticmethod
    def is_seahorses_available_for_race(seahorses: list[Seahorse]) -> bool:
        seahorses_id = SeahorseService.get_seahorses_available_for_race(seahorses)
        return True if seahorses_id else False
    
    @staticmethod
    def is_box_event_apply_to_player(box_event: str) -> bool:
        events = ('more roll', 'lost turn')
        return True if box_event in events else False
    
    @staticmethod
    def handle_player_get_box_event(player: Player, event_name: str, event_value: int):
        if event_name == 'lost turn' or event_name == 'more roll':
            player.turn_remain += event_value
