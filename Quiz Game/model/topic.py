from .quiz import Quiz


class Topic:
    """This class represent a Topic."""
    def __init__(self, topic_name: str, quizzes: list[Quiz]) -> None:
        self.__topic_name = topic_name
        self.__quizzes = quizzes
    
    @property
    def topic_name(self) -> str:
        return self.__topic_name

    @topic_name.setter
    def topic_name(self, new_name: str) -> None:
        self.topic_name = new_name.lower()
    
    @property
    def quizzes(self) -> list[Quiz]:
        return self.__quizzes
    
    @quizzes.setter
    def quizzes(self, new_quizzes: list[Quiz]):
        self.__quizzes = new_quizzes