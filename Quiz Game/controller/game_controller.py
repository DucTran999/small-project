from math import ceil

from view.game_view import GameView

from model.game_model import GameModel

from utils.function_helper import FunctionHelper


class GameController: 
    """Operating activities at Game Screen.
    
    Class attribute:
    - is_running: use to keep the game screen continuously visible until user 
    want to exit. 
    """
    is_running = True
    
    def __init__(self, game_view: GameView, game_model: GameModel) -> None:
        self.game_v = game_view
        self.game_m = game_model

    def run(self):
        """The brain of Game Controller
        
        This class always loads the topic list first. This keeps it up to date. 
        Besides, if some error occurs while loading, all features provided at 
        Game Screen will not be available.
        
        Sub-method:
        - handle_user_choice.
        """    
        while self.is_running:
            topics = self.game_m.get_topic_list()
            if topics != None:
                user_choice = self.game_v.display_game_screen() 
                self.handle_user_choice(user_choice, topics)
            else: 
                self.game_v.display_error("<!> 'New Game' feature has errors.")
                break

    def handle_user_choice(self, user_choice: int, topics: list[str]) -> None:
        if user_choice == 1:
            FunctionHelper.clear_console()
            self.handle_review_option(topics)
        elif user_choice == 2: 
            FunctionHelper.clear_console()
            self.handle_do_quiz_option(topics)
        elif user_choice == 3:
            FunctionHelper.clear_console()
            self.is_running = False
    
    def handle_review_option(self, topics: list[str]) -> None:
        """Showing topic list and get topic id entered by user
        
        Sub-method:
        - start_review: display topic's quizzes with answer
        """
        topic_id = self.game_v.get_topic_review_id(topics)
        if topic_id != 'q':
            topic_name = topics[int(topic_id)]
            self.start_review(topic_name)
        else:
            FunctionHelper.clear_console()
    
    def start_review(self, topic_name: str) -> None:
        FunctionHelper.clear_console()
        topic = self.game_m.get_topic_by_name(topic_name)
        self.game_v.display_topic_for_review(topic)
    
    def handle_do_quiz_option(self, topics: list[str]) -> None:
        """Organize a small test for user.
        
        Sub-method:
        - start_quizzing: create list quizzes, grade, and evaluate the results.
        """
        topic_id = self.game_v.get_topic_review_id(topics)
        if topic_id != 'q':
            topic_name = topics[int(topic_id)]
            self.start_quizzing(topic_name)
        else:
            FunctionHelper.clear_console()
    
    def start_quizzing(self, topic_name: str) -> None:
        FunctionHelper.clear_console()
        topic = self.game_m.get_topic_by_name(topic_name)
        quizzes_for_test = self.game_m.get_random_five_quizzes(topic)
        if quizzes_for_test:
            self.tracking_user_do_quiz(topic_name, quizzes_for_test)
        else:
            announcement = f"<!> {topic_name.title()} topic doesn't have quiz!"
            self.game_v.display_announcement(announcement)
            
    def tracking_user_do_quiz(self, topic_name: str, quizzes_for_test: list) -> None:
        """Tracking user quizzing.
        
        Workflow:
        - Get user answers list.
        - Grading
        - display result.
        """
        user_ans, ans_key = self.game_v.display_topic_for_test(topic_name,
                                                               quizzes_for_test)
        grade = self.grading(user_ans, ans_key)
        self.game_v.display_test_result(grade, user_ans, ans_key)
        
    def grading(self, user_ans: list[str], ans_key: list[str]) -> int:
        quiz_qty = len(user_ans)
        correct_ans = 0
        for idx in range(quiz_qty):
            if user_ans[idx] == ans_key[idx]:
                correct_ans += 1

        return ceil(correct_ans / quiz_qty * 100)