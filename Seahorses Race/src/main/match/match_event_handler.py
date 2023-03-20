import secrets

from player.player import Player
from player.player_view import PlayerView
from player.player_service import PlayerService
from race.race import Race
from box.box import Box
from seahorse.seahorse import Seahorse
from seahorse.filter_seahorse_service import FilterSeahorseService
from seahorse.handle_seahorse_event_service import HandleSeahorseEventService

class MatchEventHandler:
    """Responsible for handling match events affecting data of players and their
    seahorse.
    """
    def __init__(self) -> None:
        self.seahorse_filter = FilterSeahorseService()
        self.seahorse_event = HandleSeahorseEventService()
        self.player_event = PlayerService()
        self.player_view = PlayerView()
    
    def handle_dice_event(self, die_face: int, player: Player, race: Race):
        """Handle two main cases of dice events."""
        self.player_view.display_player_info(player)
        if die_face == 6:
            self.handle_face_6_event(player, race, die_face)
        else:
            self.handle_other_face_event(player, race, die_face)
      
    def handle_face_6_event(self, player: Player, race: Race, dice_face: int):
        """Handle die face 6.
        
        Filter the seahorse id that matches the event. Then let the player choose
        one and update it info.
        """
        # get list id of seahorses available (state: Warmup, Ready, Running)
        list_id = self.seahorse_filter.get_seahorses_available_id_list(
            player.seahorses)
        if list_id:
            seahorse_id = self.get_seahorse_id_selected(player, list_id)
            self.update_player_info_depend_on_event(
                player, race, seahorse_id, dice_face)
        else:
            print("<i> No seahorse available!")
    
    def handle_other_face_event(self, player: Player, race: Race, dice_face: int):
        # get list id of seahorses can move (state: Ready, Running )
        list_id = self.seahorse_filter.get_seahorse_can_move_id_list(
            player.seahorses)
        if list_id:
            seahorse_id = self.get_seahorse_id_selected(list_id)
            self.update_player_info_depend_on_event(
                player, race, seahorse_id, dice_face)
        else:
            print("<i> No seahorse ready!")
    
    def get_seahorse_id_selected(self, player: Player, list_id: list[int]):
        """ and let player select."""
        if player.player_type == "auto":
            # using module secrets get seahorse id will be move.
            return secrets.choice(list_id)
        elif player.player_type == "manual":
            # player enter seahorse id
            return PlayerView.enter_seahorse_id_for_action(list_id)
    
    def update_player_info_depend_on_event(self, player: Player, race: Race,
                                             seahorse_id: int, dice_face: int):
        # Update seahorse new position.
        seahorse = player.seahorses[seahorse_id - 1]
        if dice_face == 6:
            self.seahorse_event.update_seahorse_info_get_face_6_event(
                seahorse,dice_face)
        else:
            self.seahorse_event.update_seahorse_info_get_not_face_6_event(
                seahorse, dice_face)
        # After moving to new position, seahorse may get box.
        self.update_player_info_if_get_box(seahorse, player, race)
    
    def update_player_info_if_get_box(self, seahorse: Seahorse, player: Player,
                                      race: Race) -> None:
        if self.seahorse_event.is_seahorse_get_box(seahorse.position,
                                                   race.boxes_positions):
            box = self.get_box_by_position(seahorse.position, race.boxes)
            box.display_box()
            self.apply_box_event(seahorse, player, box)
    
    def get_box_by_position(self, box_position: int, boxes: list[Box]) -> Box:
        for box in boxes:
            if box_position == box.position:
                return box
    
    def apply_box_event(self, seahorse: Seahorse, player: Player, box: Box):
        if self.seahorse_event.is_box_event_apply_to_seahorse(box.event_name):
            self.seahorse_event.update_seahorse_info_get_box_event(
                seahorse, box.event_name, box.event_value)
        elif self.player_event.is_box_event_apply_to_player(box.event_name):
            self.player_event.update_player_info_get_box_event(
                player, box.event_name, box.event_value)
    