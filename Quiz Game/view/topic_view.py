from view.quiz_view import QuizView
from view.prevent_invalid_input import PreventInvalidInput

from model.quiz import Quiz
from model.topic import Topic


class TopicView:
    """In charge of presenting data relates to Topic."""
       
    def display_topic_list_in_table(self, topics: list[str]) -> None:
        """Display list topic with id and name.
        
        This method shows the topic list in table format (maximum 4 columns per 
        row). The topics' order is sorted by alphabet.
        
        Sub-method:
        - is_end_with_newline: determine print topic name with newline character
        at the end.
        
         Variables:
        - count: tracking the topic's order each line.
        """
        topics.sort()
        print(f"{'TOPIC LIST':-^60}")
        count = 0
        for topic_order, topic_name in enumerate(topics):
            count += 1
            if self.is_end_with_newline(count, topic_order, len(topics)):
                print(f"{topic_order}. {topic_name}", end='\n')
                count = 0
            else:
                print(f"{topic_order}. {topic_name}", end='\t\t')
        print("-" * 60)
    
    def is_end_with_newline(self, 
                         count: int, 
                         topic_order: int,
                         topic_len: int
                        ) -> bool:
        is_last_topic = (topic_order == topic_len - 1)
        is_forth_topic = (count == 4)
        return True if (is_last_topic or is_forth_topic) else False

    def display_topic_name(self, topic_name: str) -> None:
        topic_banner = f"TOPIC {topic_name.capitalize()}"
        print(f"{topic_banner:-^60}")
    
    def display_quizzes_review_format(self, quizzes: list[Quiz]):
        for quiz_id, quiz in enumerate(quizzes):
            self.display_quiz(quiz_id, quiz)
            input("Press any key to continue...")
        print(f"{'<i> All Quizzes are shown!':-^60}")
    
    def display_quiz(self, quiz_id: int, quiz: Quiz) -> None:
        QuizView.display_question(quiz_id, quiz.question)
        QuizView.display_choices_list(quiz.choices)
        QuizView.display_answer_key(quiz.answer)
         
    def display_quiz_test_format(self, quiz_id, quiz: Quiz) -> None:
        QuizView.display_question(quiz_id, quiz.question)
        QuizView.display_choices_list(quiz.choices)
    
    def display_topic_brief_info(self, topic_id: int, topic_name):
        if topic_id != -1:
            print(f"<i> Found: {topic_name} - id: {topic_id}")
        else:
            print(f"<i> Topic '{topic_name}' not found!")

    def input_form_create_topic(self, topic_name: str) -> Topic:
        quizzes = list()
        while True:
            print("Do you want to add quiz?")
            user_ans = PreventInvalidInput.user_enter_confirmation()
            if user_ans == 'y':
                quiz = self.input_form_create_quiz()
                quizzes.append(quiz)
            else:
                return Topic(topic_name, quizzes)
    
    def input_form_create_quiz_list(self, )-> list[Quiz]:
        quizzes = list()
        while True:
            print("Do you want to add quiz?")
            user_ans = PreventInvalidInput.user_enter_confirmation()
            if user_ans == 'y':
                quiz = self.input_form_create_quiz()
                quizzes.append(quiz)
            else:
                return quizzes
    
    def input_form_edit_quiz(self, quizzes: list[Quiz],
                             quiz_id: int) -> list[Quiz]:
        quiz = quizzes[quiz_id]
        self.display_quiz(quiz_id, quiz)
        # Extract current quiz attribute
        cur_question = quiz.question
        cur_choice_a = quiz.choices[0]
        cur_choice_b = quiz.choices[1]
        cur_choice_c = quiz.choices[2]
        cur_ans_key = quiz.answer
        
        print(f"{'Edit Area':-^60}") 
        quiz.question = PreventInvalidInput.user_enter_quiz_edit("question", cur_question)
        quiz.choices[0] = PreventInvalidInput.user_enter_quiz_edit("option A", cur_choice_a)
        quiz.choices[1] = PreventInvalidInput.user_enter_quiz_edit("option B", cur_choice_b)
        quiz.choices[2] = PreventInvalidInput.user_enter_quiz_edit("option C", cur_choice_c)
        quiz.answer =  PreventInvalidInput.user_enter_quiz_edit("answer key", cur_ans_key).upper()
        return quizzes
        
    def input_form_create_quiz(self) -> Quiz:
        question = PreventInvalidInput.user_enter_input_need_confirm("question")
        option_a = PreventInvalidInput.user_enter_input_need_confirm("option A")
        option_b = PreventInvalidInput.user_enter_input_need_confirm("option B")
        option_c = PreventInvalidInput.user_enter_input_need_confirm("option C")
        answer_key = PreventInvalidInput.user_enter_input_need_confirm("answer key")
        options = [option_a, option_b, option_c]
        return Quiz(question, options, answer_key.upper())