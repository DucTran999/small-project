from player.player import Player
from seahorse.seahorse import Seahorse

class MatchJudgeResultHandler:
    """In charge of judging the match result"""
    def judge_match_result_has_player_surrender(
            self, player1: Player, player2: Player, player_surrender: Player):
        return player2 if player1.name == player_surrender else player1

    def judge_match_result_no_surrender_player(self, player_1: Player, player_2: Player):
        """Find the winner if no one surrender.
        
        2 main case need to be consider:
        - numbers of seahorse finished the race NOT EQUAL: The player with the 
        most seahorses completing the race wins the match.
        - player seahorses' finished EQUAL case: Total turn should be consider.
        """
        p1_seahorses_finished = self.count_finished_seahorse(player_1.seahorses)
        p2_seahorses_finished =  self.count_finished_seahorse(player_2.seahorses)
        if p1_seahorses_finished > p2_seahorses_finished:
            return player_1
        elif p1_seahorses_finished < p2_seahorses_finished:
            return player_2
        else:
            return self.find_winner_seahorse_qty_equal_case(player_1, player_2)
    
    def count_finished_seahorse(self, seahorses: list[Seahorse]) -> int:
        count = 0
        for seahorse in seahorses:
            if seahorse.state == 'Finish':
                count += 1
        return count
    
    def find_winner_seahorse_qty_equal_case(self, player1: Player, player2: Player):
        if player1.turns_total == player2.turns_total:
            return None
        elif player1.turns_total < player2.turns_total:
            return player1
        else:
            return player2
    