from view.view import View
from view.topic_view import TopicView
from view.prevent_invalid_input import PreventInvalidInput

class EditTopicView(View, TopicView):
    """Managing presentation of information at Edit Topic Screen."""
    def display_edit_screen(self, topic_name: str) -> int:
        self.render_banner()
        self.render_menu(topic_name)
        options_valid = [option for option in range(1, 6)]
        return PreventInvalidInput.user_enter_menu_option(options_valid)
        
    def render_menu(self, topic_name: str) -> None:
        name = f"EDIT TOPIC: {topic_name}"
        options = {
            "1": "Rename Topic",
            "2": "Add Quiz",
            "3": "Edit Quiz",
            "4": "Delete Quiz",
            "5": "Go Back"
            }
        print(f"{name.upper():-^60}")
        for order, option_name in options.items():
            option = f"{order}. {option_name}"
            print(f"{option: ^60}")
   
    def input_form_new_topic_name(self, topics: list[str]):
        return PreventInvalidInput.user_enter_new_topic_name(topics)
    
    def input_form_quiz_id(self, quiz_qty: str) -> str:
        return PreventInvalidInput.user_enter_quiz_id(quiz_qty)
    