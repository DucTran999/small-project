from view.management_view import ManagementView
from view.edit_topic_view import EditTopicView

from model.management_model import ManagementModel
from model.edit_topic_model import EditTopicModel

from controller.edit_topic_controller import EditTopicController

from utils.function_helper import FunctionHelper


class ManagementController:
    """Operating activities at Management Screen."""
    
    is_running = True
    
    def __init__(self, management_v: ManagementView, management_m: ManagementModel) -> None:
       self.management_v = management_v
       self.management_m = management_m
    
    def run(self):
        while self.is_running:
            """The brain of Management Controller

            This class always loads the topic list first. This keeps it up to date. 
            Besides, if some error occurs while loading, all features provided at 
            Management Screen will not be available. Besides, if topic list is 
            empty, some features will be disable.

            Sub-method:
            - give_user_option.
            """     
            topics = self.management_m.get_topic_list()
            if topics != None:
                self.give_user_options(topics)
            else: 
                self.management_v.display_error("<!> 'Topic Management' can't start.")
                break
    
    def give_user_options(self, topics: list[str]) -> None:
        """Give users suitable options.
        
        Consider the options that should be offered to the user. If the topics 
        list is empty, only the options add topic and back will be available. 
        If not, enable all options.
        
        Sub-method:
        - handle_user_choice.
        """
        if len(topics) == 0:
            user_choice = self.management_v.display_management_screen(True)
            self.handle_user_choice(user_choice, topics, True)
        else:
            user_choice = self.management_v.display_management_screen()
            self.handle_user_choice(user_choice, topics)
    
    def handle_user_choice(self, user_choice: int,
                           topics: list, special_case: bool = False
                           ):
        if special_case:
            self.management_v.display_announcement("No topics are available.")
            if user_choice == 1:
                FunctionHelper.clear_console()
                self.handle_add_topic_option(topics)
            else:
                FunctionHelper.clear_console()
                self.is_running = False
        else:     
            if user_choice == 1:
                FunctionHelper.clear_console()
                self.handle_search_topic_option(topics)
            elif user_choice == 2:
                FunctionHelper.clear_console()
                self.handle_add_topic_option(topics)
            elif user_choice == 3:
                FunctionHelper.clear_console()
                self.handle_edit_topic_option(topics)
            elif user_choice == 4:
                FunctionHelper.clear_console()
                self.handle_delete_topic_option(topics)
            elif user_choice == 5:
                FunctionHelper.clear_console()
                self.is_running = False
    
    def handle_search_topic_option(self, topics: list) -> None:
        topic_name = self.management_v.input_form_search_topic_by_name()
        topic_id = self.management_m.find_topic_by_name(topic_name, topics)
        self.management_v.display_topic_brief_info(topic_id, topic_name)
    
    def handle_add_topic_option(self, topics: list) -> None:
        """Allow user add new topic.
        
        Check if the topic exists or not. If it is new, suggest users add quizzes.
        If they don't want to do that, just add a topic with an empty list test.
        
        Sub-method:
        create_topic.
        """
        topic_name = self.management_v.input_form_search_topic_by_name()
        topic_id = self.management_m.find_topic_by_name(topic_name, topics)
        if topic_id == -1:
            self.create_topic(topic_name)
        else:
            self.management_v.display_announcement("Topic is exist!")
    
    def create_topic(self, topic_name: str):
        topic = self.management_v.input_form_create_topic(topic_name)
        self.management_m.add_new_topic(topic)
        self.management_v.display_announcement("New topic added!")
    
    def handle_edit_topic_option(self, topics: list):
        self.management_v.display_topic_list_in_table(topics)
        topic_id = self.management_v.input_form_get_topic_by_id(topics)
        if topic_id != 'q':
            FunctionHelper.clear_console()
            topic_name = topics[int(topic_id)]
            edit_topic_v = EditTopicView()
            edit_topic_m = EditTopicModel()
            edit_topic_c = EditTopicController(edit_topic_v, edit_topic_m)
            edit_topic_c.run(topic_name, topics)

    def handle_delete_topic_option(self, topics: list):
        self.management_v.display_topic_list_in_table(topics)
        topic_id = self.management_v.input_form_get_topic_by_id(topics)
        if topic_id != 'q':
            self.management_m.delete_topic(int(topic_id), topics)
            self.management_v.display_announcement("<i> Remove topic successfully!")
