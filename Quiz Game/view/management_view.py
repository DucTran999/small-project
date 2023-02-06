from view.view import View
from view.topic_view import TopicView
from view.prevent_invalid_input import PreventInvalidInput


class ManagementView(View, TopicView):
    """Managing presentation of information at Topic Management Screen."""
    
    def display_management_screen(self, special_case: bool = False) -> int:
        """Showing management menu in different case.
        
        Sub-methods: 
        - render_menu_special_case: in case topic list is empty.
        - render_menu: used for all other cases.
        """
        self.render_banner()
        if special_case:
            self.render_menu_special_case()
            options_valid = [option for option in range(1, 3)]
        else:
            self.render_menu()
            options_valid = [option for option in range(1, 6)]
        return PreventInvalidInput.user_enter_menu_option(options_valid)
    
    def render_menu_special_case(self) -> None:
        name = "MANAGEMENT MENU"
        options = {
            "1": "Add Topic",
            "2": "Go Back"
            }
        print(f"{name.upper():-^60}")
        for order, option_name in options.items():
            option = f"{order}. {option_name}"
            print(f"{option: ^60}")
        
    def render_menu(self) -> None:
        name = "MANAGEMENT MENU"
        options = {
            "1": "Search Topic By Name",
            "2": "Add Topic",
            "3": "Edit Topic",
            "4": "Delete Topic",
            "5": "Go Back"
            }
        print(f"{name.upper():-^60}")
        for order, option_name in options.items():
            option = f"{order}. {option_name}"
            print(f"{option: ^60}")
    
    def input_form_search_topic_by_name(self) -> str:
        return PreventInvalidInput.user_enter_topic_name()
    
    def input_form_get_topic_by_id(self, topics) -> int:
        return PreventInvalidInput.user_enter_topic_id(topics)
    
