from match.match import Match

from race.race_service import RaceService

from player.player import Player
from player.player_view import PlayerView
from player.player_service import PlayerService

from seahorse.seahorse import Seahorse

from die.die_controller import DieController

class MatchService:
    
    def setup_match(self, player_qty: int = 2) -> Match:
        if player_qty == 2:
            players = self.create_players_list()
        else:
            players = self.create_players_list_single_game()
        die = DieController()
        race = RaceService.create_race()
        return Match(players, die, race)
    
    def create_players_list(self) -> tuple[Player]:
        player_1_name = PlayerView.display_user_input_name(1)
        player_1 = PlayerService.create_player(player_1_name)
        player_2_name = PlayerView.display_user_input_name(2, player_1_name)
        player_2 = PlayerService.create_player(player_2_name)
        return player_1, player_2
    
    def create_players_list_single_game(self):
        player_1_name = 'computer'
        player_1 = PlayerService.create_player(player_1_name)
        player_2_name = PlayerView.display_user_input_name(2, player_1_name)
        player_2 = PlayerService.create_player(player_2_name)
        return player_1, player_2
    
    def judge_match_result(self, player_1: Player, player_2: Player): 
        p1_seahorses_finished = self.count_finished_seahorse(player_1.seahorses)
        p2_seahorses_finished =  self.count_finished_seahorse(player_2.seahorses)
        if p1_seahorses_finished > p2_seahorses_finished:
            return player_1
        elif p1_seahorses_finished < p2_seahorses_finished:
            return player_2
        else:
            return self.finished_seahorse_qty_not_equal_case(player_1, player_2)
    
    def count_finished_seahorse(self, seahorses: list[Seahorse]):
        count = 0
        for seahorse in seahorses:
            if seahorse.state == 'Finish':
                count += 1
        return count
    
    def finished_seahorse_qty_not_equal_case(self, player1: Player,
                                             player2: Player
                                             ) -> Player:
        if player1.turns_total == player2.turns_total:
            return None
        elif player1.turns_total < player2.turns_total:
            return player1
        else:
            return player2
    