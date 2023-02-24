class Quiz:
    """This class represent a Quiz."""
    __question: str 
    __choices: list[str]
    __answer: str
    
    def __init__(self, question: str, choices: list, answer: str) -> None:
        self.__question = question.strip()
        self.__choices = choices
        self.__answer = answer.strip()
    
    @property
    def question(self) -> None:
        return self.__question
    
    @question.setter
    def question(self, content: str) -> None:
        self.__question  = content
    
    @property
    def choices(self) -> None:
        return self.__choices
    
    @choices.setter
    def choices(self, new_choices: list) -> None:
        self.__choices = new_choices
    
    @property
    def answer(self) -> str:
        return self.__answer
    
    @answer.setter
    def answer(self, new_answer: str) -> None:
        self.__answer = new_answer
      