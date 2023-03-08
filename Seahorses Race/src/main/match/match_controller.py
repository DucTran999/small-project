import secrets

from match.match import Match
from match.match_service import MatchService
from match.match_view import MatchView

from player.player import Player
from player.player_service import PlayerService
from player.player_view import PlayerView

from seahorse.seahorse_service import SeahorseService

from race.race import Race
from race.race_service import RaceService

from box.box import Box
from box.box_view import BoxView

from utils.function_helper import FunctionHelper


class MatchController:
    """Operating a match
    
    Class attributes:
    - match_processing: type bool. This class attribute help maintaining the match.
    - surrender_flag: type bool. End the match and print the result immediately.
    """
    match_processing = True
    surrender_flag = False
    
    def __init__(self) -> None:
        """MatchController constructor."""
        self.match_s = MatchService()
        self.match_v = MatchView()
    
    def start_single_player_match(self):
        match = self.match_s.setup_match(1)
        FunctionHelper.delay_with_announcement("Creating match", 2)
        FunctionHelper.clear_screen()
        self.process_match_single_player(match)
    
    def start_two_player_match(self):
        """Start two player session.
        
        Unit of work:
        - setup_match: create a match object
        - process_match: operating the match
        """
        match = self.match_s.setup_match()
        FunctionHelper.delay_with_announcement("Creating match", 2)
        FunctionHelper.clear_screen()
        self.process_match(match)

    def process_match_single_player(self, match):
        round_count = 0
        while self.match_processing:
            round_count += 1
            self.match_v.display_round_info(round_count, match.race)
            
            player_1: Player = match.players[0]
            while player_1.turn_remain > 0:
                self.computer_processing(match, player_1)
            
            player_2: Player = match.players[1]
            while player_2.turn_remain > 0:
                self.player_processing(match, player_2)
            
            if self.surrender_flag == False:
                self.setup_after_round(match, player_1, player_2, round_count)
    
    def process_match(self, match: Match):
        """Operating the match
        
        Workflow:
        - player 1 turn.
        - player 2 turn.
        - check surrender flag: if one player enter 'sur' end the game. Otherwise
        setup data for new round.
        """
        round_count = 0
        while self.match_processing:
            round_count += 1
            self.match_v.display_round_info(round_count, match.race)
            
            player_1: Player = match.players[0]
            while player_1.turn_remain:
                self.player_processing(match, player_1)
            
            player_2: Player = match.players[1]
            while player_2.turn_remain:
                self.player_processing(match, player_2)
            
            if self.surrender_flag == False:
                self.setup_after_round(match, player_1, player_2, round_count)
    
    def setup_after_round(self, match: Match, player_1: Player,
                          player_2: Player, round_count: int) -> None:
        """Set up data for next round.
        
        Check player's seahorse is available for race. If they have some. Adding
        1 more turn for them.
        Suppose both of them don't have any seahorses available. It means the 
        match is going to end. So that we don't need to set up for the next round.
        Call process_match_result to find the winner and end it.
        """
        FunctionHelper.delay_with_announcement(
            f"<i> Set up round {round_count + 1}", 3)
        FunctionHelper.clear_screen()
        self.process_match_has_player_lost_turn(player_1, player_2)
        if PlayerService.is_seahorses_available_for_race(player_1.seahorses):
            player_1.turn_remain += 1
        if PlayerService.is_seahorses_available_for_race(player_2.seahorses):
            player_2.turn_remain += 1
        
        if player_2.turn_remain == player_1.turn_remain == 0:
            self.process_match_result(match)
    
    def process_match_has_player_lost_turn(self, player_1: Player, player_2):
        """"""
        if player_1.turn_remain == player_2.turn_remain == -1:
               player_1.turn_remain = 0
               player_2.turn_remain = 0
        elif player_1.turn_remain == 0 and player_2.turn_remain == -1:
            player_2.turn_remain = 0
        elif player_2.turn_remain == 0 and player_1.turn_remain == -1:
            player_1.turn_remain = 0
    
    
    def process_match_result(self, 
                             match: Match,
                             player_name: str = '',
                             command: str = 'judge'
                             ) -> None:
        """Process the match result.
        
        Param:
        - command: has two values are 'sur' and 'judge'. The 'judge' is default.
        
        According to the command param, this method will find the winner of the 
        match.
        """
        if command == 'sur':
            self.match_processing = False
            self.surrender_flag = True
            self.match_v.display_match_result_surrender_case(player_name)
        else:
            self.match_processing = False
            winner = self.match_s.judge_match_result(match.players[0],
                                                     match.players[1])
            self.match_v.display_match_result(winner)
    
    def computer_processing(self, match: Match, player: Player):
        if PlayerService.is_seahorses_available_for_race(player.seahorses):
            player.tracking_turns()
            die_face = match.die_c.handle_player_roll_die()
            self.processing_die_face_event_computer(die_face, player, match.race)
            player.turn_remain -= 1
    
    def player_processing(self, match: Match, player: Player):
        """Processing 1 player turn
        
        Tasks:
        - tracking player turn. Use tracking turns method.
        - let player roll a die.
        - handle the event corresponded to the die face.
        - Subtract the player's turn by 1.
        """
        if PlayerService.is_seahorses_available_for_race(player.seahorses):
            player.tracking_turns()
            die_face = self.ask_player_for_die_roll(match, player)
            if die_face:
                self.processing_die_face_event(die_face, player, match.race)
            player.turn_remain -= 1
    
    def ask_player_for_die_roll(self, match: Match, player: Player):
        print(">>>>>>>>> PLAYER", player.name)
        user_choice = self.match_v.get_user_choice()
        if user_choice == 'r':
            return match.die_c.handle_player_roll_die()
        elif user_choice == 'sur':  
            self.process_match_result(match, player.name, 'sur')

    def processing_die_face_event_computer(self, die_face: int, player: Player, race: Race):
        """Handle die face event.
        
        The 2 main case below has their sub-method to solve them.
        - face 6: 
        - other faces.
        """
        PlayerView.display_player_info(player)
        if die_face == 6:
            self.handle_face_6_event_computer(player, race, die_face)
        else:
            self.handle_other_face_event_computer(player, race, die_face)
    
    def processing_die_face_event(self, die_face: int, player: Player, race: Race):
        """Handle die face event.
        
        The 2 main case below has their sub-method to solve them.
        - face 6: 
        - other faces.
        """
        PlayerView.display_player_info(player)
        if die_face == 6:
            self.handle_face_6_event(player, race, die_face)
        else:
            self.handle_other_face_event(player, race, die_face)
    
    def handle_face_6_event_computer(self, player: Player, race: Race, die_face: int):
        """Handle die face 6."""
        
        # using module secrets get seahorse id will be move randomly
        list_id = SeahorseService.get_seahorses_available_for_race(player.seahorses)
        seahorse_id = secrets.choice(list_id)
        # Update seahorse new position.
        seahorse = player.seahorses[seahorse_id-1]
        SeahorseService.handle_seahorse_get_6_face_event(seahorse, die_face)
        
        # Update seahorse if it get box.
        self.update_seahorse_if_get_box(seahorse, player, race)
    
    def handle_face_6_event(self, player: Player, race: Race, die_face: int, ):
        """Handle die face 6.
        
        Tasks:
        - Get all the player's seahorses that satisfy the condition.
        - Chose seahorse will be moved.
        - Update seahorses new position.
        - Check if it gets a box.
        - Handle box event.
        """
        
        # get seahorse id will be move
        list_id = SeahorseService.get_seahorses_available_for_race(player.seahorses)
        seahorse_id = PlayerView.get_seahorse_id_for_action(list_id)
        
        # Update seahorse new position.
        seahorse = player.seahorses[seahorse_id-1]
        SeahorseService.handle_seahorse_get_6_face_event(seahorse, die_face)
        
        # Update seahorse if it get box.
        self.update_seahorse_if_get_box(seahorse, player, race)

    def handle_other_face_event_computer(self, player: Player, race: Race, die_face: int):
        # get seahorse id will be move
        list_id = SeahorseService.get_seahorse_can_move_id_list(player.seahorses)
        if list_id:
            seahorse_id = secrets.choice(list_id)
            
            # Update seahorse new position.
            seahorse = player.seahorses[seahorse_id-1]
            SeahorseService.handle_seahorse_get_not_6_face_event(seahorse, die_face)

            # Update seahorse if it get box.
            self.update_seahorse_if_get_box(seahorse, player, race)
        else:
            print("<i> No seahorse ready!")
            
    def handle_other_face_event(self, player: Player, race: Race, die_face: int):
        # get seahorse id will be move
        list_id = SeahorseService.get_seahorse_can_move_id_list(player.seahorses)
        if list_id:
            seahorse_id = PlayerView.get_seahorse_id_for_action(list_id)
        
            # Update seahorse new position.
            seahorse = player.seahorses[seahorse_id-1]
            SeahorseService.handle_seahorse_get_not_6_face_event(seahorse, die_face)

            # Update seahorse if it get box.
            self.update_seahorse_if_get_box(seahorse, player, race)
        else:
            print("<i> No seahorse ready!")
    
    def update_seahorse_if_get_box(self, seahorse, player: Player, race: Race):
        boxes_pos = RaceService.attract_box_position(race.boxes)
        if SeahorseService.is_seahorse_get_box(seahorse.position, boxes_pos):
            box = RaceService.get_box_by_pos(seahorse.position, race.boxes)
            BoxView.display_box(box)
            if SeahorseService.is_box_event_apply_to_seahorse(box.event_name):
                SeahorseService.handle_seahorse_get_box_event(seahorse, 
                                                              box.event_name,
                                                              box.event_value
                                                              )
            elif PlayerService.is_box_event_apply_to_player(box.event_name):
                PlayerService.handle_player_get_box_event(player, 
                                                          box.event_name, 
                                                          box.event_value
                                                          )
                