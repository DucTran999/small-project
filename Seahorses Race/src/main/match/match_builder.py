from match.match import Match

from player.player import Player
from player.player_view import PlayerView
from player.player_builder import PlayerBuilder

from race.race import Race
from race.race_builder import RaceBuilder


class MatchBuilder:
    """Create a Match Objects"""
    def __init__(self) -> None:
        self.player_service = PlayerBuilder()
        self.race_builder = RaceBuilder()
    
    def build_players_single_mode(self) -> tuple[Player]:
        player_1_name = 'computer'
        player_1 = self.player_service.create_player(player_1_name, "auto")
        player_2_name = PlayerView.display_user_input_name_form(2, player_1_name)
        player_2 = self.player_service.create_player(player_2_name)
        return player_1, player_2

    def build_players_multi_mode(self) -> tuple[Player]:
        player_1_name = PlayerView.display_user_input_name_form(1)
        player_1 = self.player_service.create_player(player_1_name)
        player_2_name = PlayerView.display_user_input_name_form(2, player_1_name)
        player_2 = self.player_service.create_player(player_2_name)
        return player_1, player_2
    
    def build_race(self) -> Race:
        return self.race_builder.create_race()

    def get_result(self, match: Match, mode: str) -> Match:
        if mode == 'single':
            match.players = self.build_players_single_mode()
        elif mode == 'multi':
            match.players = self.build_players_multi_mode()
        match.race = self.build_race()
        return match
    