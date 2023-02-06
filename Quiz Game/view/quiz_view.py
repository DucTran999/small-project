class QuizView:
    """In charge of presenting Quiz's parts."""
    
    @classmethod
    def print_long_string(cls, long_string: str) -> None:
        """Print string has length over 80 characters. 
        
        Since some questions are too long, they need to be split up for readability.
        So break the question into multiple lines and up to 15 words per line.
        
        Sub-method:
        - is_end_with_newline: Determine whether the current word is the last word
        of the line or not. 
        """ 
        words = long_string.strip().split(" ")
        word_ind = 0
        for word in words:
            word_ind += 1
            if cls.is_end_with_newline(word_ind, len(words)):
                print(word, end='\n')
                word_ind = 0
            else:
                print(word, end=' ')
    
    @classmethod
    def is_end_with_newline(cls, word_ind: int, words_len: int) -> bool:
        is_fifth_word = (word_ind == 15)
        is_last_word = (word_ind == words_len)
        return True if (is_fifth_word or is_last_word) else False

    @classmethod
    def display_question(cls, question_id: int, question: str) -> None:
        print(f"<?> Question {question_id}:")
        cls.print_long_string(question)
    
    @classmethod
    def display_choices_list(cls, choices: list[str]) -> None:
        OPTION = ["A", "B", "C"]
        for ind, choice in enumerate(choices):
            format_choice = f"({OPTION[ind]}) {choice}"
            cls.print_long_string(format_choice)
            
    @classmethod
    def display_answer_key(cls, answer: str) -> None:
        print(f"<i> Answer: {answer}")