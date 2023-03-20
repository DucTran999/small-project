from view.edit_topic_view import EditTopicView

from model.edit_topic_model import EditTopicModel
from model.topic import Topic

from utils.function_helper import FunctionHelper


class EditTopicController:
    """Operate topic editing features:

    Available Features:
    - Rename topic
    - Add quiz
    - Edit quiz
    - Delete quiz.
    """
    is_running = True
    
    def __init__(self, edit_v: EditTopicView, edit_m: EditTopicModel) -> None:
        self.edit_v = edit_v
        self.edit_m = edit_m
    
    def run(self, topic_name: str, topics: list[str]) -> None:
        topic_obj = self.edit_m.get_topic(topic_name)
        while self.is_running:
            user_inp = self.edit_v.display_edit_screen(topic_name)
            self.handle_user_choice(user_inp, topics, topic_obj)
    
    def handle_user_choice(self, user_choice: int, topics: list[str], topic_obj):
        if user_choice == 1:
            FunctionHelper.clear_console()
            self.handle_rename_topic_option(topics, topic_obj)
            self.is_running = False
        elif user_choice == 2:
            FunctionHelper.clear_console()
            self.handle_add_quiz_option(topic_obj)
        elif user_choice == 3:
            FunctionHelper.clear_console()
            self.handle_edit_quiz_option(topic_obj)
        elif user_choice == 4:
            FunctionHelper.clear_console()
            if topic_obj.quizzes:
                self.handle_delete_quiz_option(topic_obj)
            else:
                print("<i> No quiz is available")
        else:
            FunctionHelper.clear_console()
            self.is_running = False
    
    def handle_rename_topic_option(self, topics: list[str], topic: Topic):
        new_name = self.edit_v.input_form_new_topic_name(topics)
        self.edit_m.rename_topic(topics, topic.topic_name, new_name)
    
    def handle_add_quiz_option(self, topic: Topic):
        """Add new quiz to topic.
        
        Allows users to add multiple quizzes at a time.
        """
        quizzes_current = topic.quizzes
        quizzes_new = self.edit_v.input_form_create_quiz_list()
        if quizzes_new:
            quizzes_merge = quizzes_current + quizzes_new
            self.edit_m.add_new_quiz(topic.topic_name, quizzes_merge)
            self.edit_v.display_announcement("<i> Add quiz successful!")
        else:
            self.edit_v.display_announcement("<i> Nothing change!")
    
    def handle_edit_quiz_option(self, topic):
        """Edit 1 quiz each time.
        
        Unit of work:
        - display all quizzes in topic.
        - Enter quiz id want to edit.
        - Edit quiz.
        """
        self.edit_v.display_quizzes_review_format(topic.quizzes)
        self.edit_v.display_announcement("<?> Which quiz do you want to edit?")
        quiz_id = self.edit_v.input_form_quiz_id(len(topic.quizzes))
        if quiz_id != 'q':
            FunctionHelper.clear_console()
            quizzes = self.edit_v.input_form_edit_quiz(topic.quizzes, int(quiz_id))
            self.edit_m.add_new_quiz(topic.topic_name, quizzes)
            self.edit_v.display_announcement("<i> Quiz updated!")
        
    def handle_delete_quiz_option(self, topic):
        """Delete quiz by id
        
        The user is only allowed to delete quizzes one by one.
        """
        self.edit_v.display_quizzes_review_format(topic.quizzes)
        quiz_id = self.edit_v.input_form_quiz_id(len(topic.quizzes))
        if quiz_id != 'q':
            self.edit_m.delete_quiz_by_id(topic, int(quiz_id))
            print(f"Quiz id {quiz_id} has removed!")