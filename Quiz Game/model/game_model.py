from random import sample

from dao_impl.topic_dao_impl import TopicDAOImplement

from model.quiz import Quiz
from model.topic import Topic


class GameModel:
    """Manipulating data for the game screen.
    
    Manages the objects and validates the data returned to the GameController.
    """
    def __init__(self) -> None:
        self.topic_dao = TopicDAOImplement()

    def get_topic_list(self) -> list | None:
        return self.topic_dao.get_all_topic_from_file()

    def get_topic_by_name(self, topic_name: str) -> list | None:
        return self.topic_dao.get_topic_by_name_from_file(topic_name)
    
    def get_random_five_quizzes(self, topic: Topic) -> list[Quiz]:
        """Select quizzes for creating test.
        
        This method selects random 5 quizzes for creating test. In case topic 
        does not have enough 5 quizzes then all quizzes should be return.
        
        External function:
        - sample(): this function allows selects quiz randomly and distinctly.
        """
        quizzes_qty = len(topic.quizzes)
        quizzes_cpy = topic.quizzes[:]
        if quizzes_qty >= 5:
            return sample(quizzes_cpy, 5)
        else:
            return quizzes_cpy
    