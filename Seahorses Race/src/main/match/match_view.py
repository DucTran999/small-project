from race.race import Race
from race.race_view import RaceView

from player.player import Player

from utils.validation import Validation

class MatchView:
    """"""
    def get_user_choice(self):
        valid_inp = ('r', 'sur')
        return Validation.get_user_option(valid_inp, "=> Enter [r/sur]: ")
    
    def display_round_info(self, round_count: int, race: Race):
        banner = f" ROUND {round_count} "
        print(f"{banner:#^60}")
        print("-Race:")
        RaceView.display_race(race)
        print("-" * 60)
    
    def display_match_result_surrender_case(self, player_name: str):
        print(f"Player {player_name} surrendered!")
    
    def display_match_result(self, player: Player):
        if player:
            print(f"------------------{player.name} WIN!--------------------")
        else:
            print("----------------------- TIE ---------------------------")
