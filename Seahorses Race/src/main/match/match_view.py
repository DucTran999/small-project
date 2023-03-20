from race.race import Race
from race.race_view import RaceView

from player.player import Player

from utils.validation import Validation

class MatchView:
    """Present data and get player request at MatchView"""
    def get_user_choice(self, player: Player):
        print(">>>>>>>>> PLAYER", player.name)
        valid_inp = ('r', 'sur')
        return Validation.get_user_option(valid_inp, "=> Enter [r/sur]: ")
    
    def display_round_info(self, round_order: int, race: Race):
        banner = f" ROUND {round_order} "
        print(f"{banner:#^60}")
        print("-Race:")
        RaceView.display_race(race)
        print("-" * 60)
    
    def display_match_result_has_surrender(self, winner: Player, player_name: str):
        print("----------------------- MATCH END-----------------------------")
        print(f"Player {player_name} surrendered!")
        print(f"{winner.name} win the game")
        
    def display_match_result(self, winner: Player):
        if winner:
            print(f"------------------{winner.name} WIN!--------------------")
        else:
            print("----------------------- TIE ---------------------------")
