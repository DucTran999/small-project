from player.player import Player
from match.match import Match
from match.match_view import MatchView
from match.match_event_handler import MatchEventHandler
from match.match_judge_result_handler import MatchJudgeResultHandler
from match.match_set_up_round_handler import MatchSetupRoundHandler
from utils.function_helper import FunctionHelper


class MatchOperator:
    def __init__(self) -> None:
        self.match_v = MatchView()
        self.match_event_handler = MatchEventHandler()
        self.match_judger = MatchJudgeResultHandler()
        self.setup_round_handler = MatchSetupRoundHandler()
    
    def operate_match(self, match: Match):
        """Operating the match
        
        A match can have many innings. The match ends when either player surrenders
        or both sides have no more seahorses.
        """
        round_order = 0
        while match.state == "not finish":
            round_order += 1
            self.match_v.display_round_info(round_order, match.race)
            
            self.operate_round(match)
            
            self.handle_round_result(match, round_order)
    
    def operate_round(self, match: Match):
        """Handling activities of players in a round."""
        player_1: Player = match.players[0]
        while player_1.turn_remain > 0:
            self.handle_player_activity(match, player_1)
        
        player_2: Player = match.players[1]
        while player_2.turn_remain > 0:
            self.handle_player_activity(match, player_2)
                
    def handle_player_activity(self, match: Match, player: Player):
        """Handling player request.
        
        If the player type is auto: then roll the dice automatically. 
        If a player is manual, let them roll the dice or surrender.
        """
        player.tracking_turns()
        if player.player_type == "auto":
            dice_face = self.player_roll_dice(match)
        else:
            dice_face = self.ask_player_for_dice_roll(match, player)

        if dice_face:
            self.match_event_handler.handle_dice_event(
                dice_face, player, match.race)
        player.turn_remain -= 1
    
    def ask_player_for_dice_roll(self, match: Match, player: Player):
        user_choice = self.match_v.get_user_choice(player)
        if user_choice == 'r':
            return self.player_roll_dice(match)
        elif user_choice == 'sur':
            winner = self.find_the_match_winner(match, 'sur', player.name)
            self.match_v.display_match_result_has_surrender(winner, player.name)
    
    def player_roll_dice(self, match: Match) -> int:
        return match.dice_shaker.shake_dice()
    
    def handle_round_result(self, match: Match, round_order: int):
        """After each round, depending on players' states consider ending the 
        match or setting up for the next round.
        """
        player1, player2  = match.players[0], match.players[1]
        
        if player1.state == player2.state == "done":  
            winner = self.find_the_match_winner(match)
            self.match_v.display_match_result(winner)
        elif match.state != "finished":   
            setup_announcement = f"<i> Set up round {round_order + 1}"
            FunctionHelper.delay_with_announcement(setup_announcement, 3)
            FunctionHelper.clear_screen()
            self.setup_round_handler.setup_player_turn_for_next_round(
                player1, player2)
    
    def find_the_match_winner(self, match: Match, command: str = 'judge',
                              player_surrender_name: str = ''):
        """Find the winner of the match
        
        Importance parameter:
        - command: has two values are 'sur' and 'judge'. The 'judge' is default.
        The 'sur' command is in case the match has one player surrender otherwise
        is the 'judge' command.
        """
        if command == 'sur':
            match.state = "finished"
            return self.match_judger.judge_match_result_has_player_surrender(
                match.players[0], match.players[1], player_surrender_name)
        else:
            match.state = "finished"
            return self.match_judger.judge_match_result_no_surrender_player(
                match.players[0], match.players[1])
    