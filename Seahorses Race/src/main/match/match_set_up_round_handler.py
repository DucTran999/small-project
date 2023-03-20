from player.player import Player
from seahorse.filter_seahorse_service import FilterSeahorseService

class MatchSetupRoundHandler:
    """Help Match Operator in setting up players turn for next round."""
    def __init__(self) -> None:
        self.seahorse_filter = FilterSeahorseService()
        
    def setup_player_turn_for_next_round(self, player1: Player, player2: Player):
        if player1.state == player2.state == "not done":
            self.add_new_turn_for_player(player1)
            self.add_new_turn_for_player(player2)
        elif player1.state == "done" and player2.state == "not done":
            self.add_new_turn_for_player(player2)
        else:
            self.add_new_turn_for_player(player1)
            
    def add_new_turn_for_player(self, player: Player):
        if self.is_player_has_seahorse_available(player.seahorses):
            player.turn_remain += 1
        else:
            player.state = "done"
    
    def is_player_has_seahorse_available(self, seahorses_list):
        return self.seahorse_filter.get_seahorses_available_id_list(seahorses_list)
    