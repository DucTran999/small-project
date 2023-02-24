from dao.topic_dao import TopicDAO
from dao.file_helper import FileHelper

from model.topic import Topic
from model.quiz import Quiz


class TopicDAOImplement(TopicDAO):
    """Processing topic data.
    
    This class is responsible for processing the data of the topic before writing
    or after reading from the file.
    """

    def get_all_topic_from_file(self):
        """Get list topics (name only)"""
        topics_raw = FileHelper.read_text_file("topics")
        if topics_raw != None:
            return [topic.strip() for topic in topics_raw]
        return topics_raw
    
    def get_topic_by_name_from_file(self, topic_name: str) -> Topic:
        """Get topic data by name.
        
        sub-method:
        - convert_quiz_dict_to_object: packaging the data extracted from the quiz
        dictionary to the Quiz object.
        
        Unit of work:
        - read topic's quizzes from the corresponding JSON file assign to 
        quizzes_raw variable.
        - If quizzes_raw is not None. Return Topic Object after processing quiz
        list. Otherwise, return it directly.
        """
        quizzes_raw = FileHelper.read_json_file(topic_name)
        quizzes_obj = list()
        if quizzes_raw != None:
            for quiz in quizzes_raw:
                quizzes_obj.append(self.convert_quiz_dict_to_object(quiz))
            return Topic(topic_name, quizzes_obj)
        return quizzes_raw
    
    def convert_quiz_dict_to_object(self, quiz: dict):
        question = quiz.get("question")
        ANSWER_OPTION = ["A", "B", "C"]
        choices = list()
        for option in ANSWER_OPTION:
            choices.append(quiz.get(option))
        answer_key = quiz.get("Answer")
        return Quiz(question, choices, answer_key)
    
    def add_topic_to_file(self, topic_name: str):
        FileHelper.append_text_file("topics", topic_name)
    
    def add_quiz_to_file(self, topic_name: str, quizzes: list[Quiz]):
        quizzes_dict = list()
        for quiz in quizzes:
            quizzes_dict.append(self.convert_quiz_to_dict_type(quiz))
        FileHelper.write_json_file(topic_name, quizzes_dict)

    def convert_quiz_to_dict_type(self, quiz: Quiz) -> dict:
        option_a, option_b, option_c = quiz.choices
        quiz_dict = {
            "question": quiz.question,
            "A": option_a,
            "B": option_b,
            "C": option_c,
            "Answer": quiz.answer
        }
        return quiz_dict
    
    def delete_topic_from_file(self, topic_name: str, topics: list[str]):
        FileHelper.write_text_file("topics", topics)
        FileHelper.delete_json_file(topic_name)
    
    def update_topic_name_to_file(self, topics: list[str], 
                                  old_name: str, new_name: str
                                  ):
        topics.remove(old_name)
        topics.append(new_name)
        topics.sort()
        FileHelper.write_text_file("topics", topics)
        FileHelper.rename_json_file(old_name, new_name)
    
    def delete_quiz_from_file(self, topic: Topic, topic_id):
        quizzes = topic.quizzes
        del quizzes[topic_id]
        FileHelper.write_json_file(topic.topic_name, quizzes)
        