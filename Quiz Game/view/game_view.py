from view.view import View
from view.topic_view import TopicView
from view.prevent_invalid_input import PreventInvalidInput

from model.topic import Topic


class GameView(View, TopicView):
        
    def display_game_screen(self) -> None:
        self.render_banner()
        self.render_menu()
        option_valid = [option for option in range(1, 4)]
        return PreventInvalidInput.user_enter_menu_option(option_valid)
    
    def render_menu(self) -> None:
        name = "new game menu"
        options = {
            "1": "Review",
            "2": "Do Quiz",
            "3": "Go Back"
            }
        print(f"{name.upper():-^60}")
        for order, option_name in options.items():
            option = f"{order}. {option_name}"
            print(f"{option: ^60}") 
    
    def get_topic_review_id(self, topics: list[str]):
        self.display_topic_list_in_table(topics)
        return PreventInvalidInput.user_enter_topic_id(topics)
    
    def display_topic_for_review(self, topic: Topic) -> None:
        self.display_topic_name(topic.topic_name)
        self.display_quizzes_review_format(topic.quizzes)
    
    def display_topic_for_test(self, 
                                  topic_name: str,
                                  quizzes_for_test: list
                                  ) -> None:
        self.display_topic_name(topic_name)
        user_ans = list()
        ans_key = list()
        for quiz_id, quiz in enumerate(quizzes_for_test):
            self.display_quiz_test_format(quiz_id, quiz)
            user_ans.append(PreventInvalidInput.user_enter_answer())
            ans_key.append(quiz.answer)
        return user_ans, ans_key

    def display_test_result(self, grade: int,
                            user_ans: list[str], ans_key: list[str]
                            ) -> None:
        print(f"{'Result':-^60}")
        self.render_judgment(grade)
        print(f" -> <i> Your answer: {user_ans}")
        print(f" -> <i> Key answer : {ans_key}") 
        
    def render_judgment(self, grade: int) -> None:
        grade_band_0 = "\t<i> Don't worry. Failure is mother's success"
        grade_band_1 = "\t<i> Don't give up. Persistence is key to success."
        grade_band_2 = "\t<i> The more you try, the closer you get to success."
        grade_band_3 = "\t<i> Good result! Repeat is mothering of learning."
        grade_band_4 = "\t<i> Great! You do it almost perfectly. You must really love this field."
        grade_band_5 = "\t<i> Fantastic! You must be expert in this field."
        
        judgement_msg = f"<i> Your grade: {grade}\n"
        if grade == 0:
            judgement_msg = judgement_msg + grade_band_0
        elif 0 < grade <= 20:
            judgement_msg = judgement_msg + grade_band_1
        elif 20 < grade <= 40:
            judgement_msg = judgement_msg + grade_band_2
        elif 40 < grade <= 60:
            judgement_msg = judgement_msg + grade_band_3
        elif 60 < grade < 80:
            judgement_msg = judgement_msg + grade_band_4
        else:     
            judgement_msg = judgement_msg + grade_band_5
        
        print(judgement_msg)
            