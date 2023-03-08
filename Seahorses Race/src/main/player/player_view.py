from player.player import Player

from utils.validation import Validation


class PlayerView:
    
    @classmethod
    def display_player_info(cls, player: Player) -> None:
        print(player)
        print('Seahorses: ')
        for seahorse in player.seahorses:
            print('\t', seahorse)
    
    @classmethod
    def display_user_input_name(cls, order: int, avoid_name: str='') -> str:
        print(f"Player {order}: ")
        return Validation.get_player_name(avoid_name)
    
    @classmethod
    def get_seahorse_id_for_action(cls, valid_seahorse_id: list[str]) -> int:
        return Validation.get_seahorse_id(valid_seahorse_id, "=> Enter seahorse id: ")