from match.match import Match
from match.match_operator import MatchOperator
from match.match_builder import MatchBuilder
from utils.function_helper import FunctionHelper


class MatchController:
    """Navigate to the corresponding match operator requested by the user.""" 
    def __init__(self) -> None:
        """MatchController constructor."""
        self.match_builder = MatchBuilder()
        self.match_operator = MatchOperator()
    
    def start_single_mode_match(self):
        match = Match()
        match = self.match_builder.get_result(match, "single")
        FunctionHelper.delay_with_announcement("Creating match", 2)
        FunctionHelper.clear_screen()
        self.match_operator.operate_match(match)
    
    def start_multi_mode_match(self):
        match = self.match_builder.get_result(match,"multi")
        FunctionHelper.delay_with_announcement("Creating match", 2)
        FunctionHelper.clear_screen()
        self.match_operator.operate_match(match)
    