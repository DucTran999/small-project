class PreventInvalidInput:
    """Ensure user input is valid.
    
    This class provides methods that handle surprise code, which may cause 
    the exception, to improve program fault tolerance.
    
    Available methods:
    - user_enter_menu_option.
    - user_enter_topic_id.
    - user_enter_answer: use in quizzing.
    - user_enter_input_with_confirm.
    """
    @staticmethod
    def user_enter_menu_option(options_valid: list[int]) -> int:
        while True:
            try:
                user_input = int(input("=> Enter option: "))
                if user_input not in options_valid:
                    raise IndexError
            except (ValueError, IndexError):
                print("<!> Invalid option!")
            else:
                return user_input

    @staticmethod
    def user_enter_topic_id(topics: list[str]) -> int:
        options_valid = [str(option) for option in range(len(topics))]
        options_valid.append('q')
        while True:
           try:
               user_input = input("=> Enter topic id or 'q' to quit: ")
               if user_input not in options_valid:
                   raise IndexError
           except IndexError:
               print("<!> Invalid option!")
           else:
               return user_input
           
    @classmethod
    def user_enter_answer(cls):
        valid_choices = ["A", "B", "C"]
        while True:
            try:
                user_ans = input("=> Enter your answer: ").upper()
                if user_ans not in valid_choices:
                    raise IndexError
            except IndexError:
                print("Answer Invalid!")
            else:
                return user_ans
            
    @classmethod
    def user_enter_topic_name(cls):
        while True:
            try:
                user_inp = input("=> Enter topic name: ").strip()
                if len(user_inp) == 0:
                    raise ValueError
            except ValueError:
                print("Empty not allow!")
            else:
                return user_inp
    
    @classmethod
    def user_enter_input_need_confirm(cls, context: str):
        """Ensure user input has been confirmed.
        
        Users can review their input before confirming to store it. 
        
        Sub-method:
        - user_enter_confirmation:
        """
        while True:
            user_inp = input(f"=> Enter {context}: ")
            try:
                user_confirmation = cls.user_enter_confirmation()
                if user_confirmation == 'n':
                    raise ValueError
            except ValueError:
                print("<!> Current text is rejected.")
            else:
                return user_inp
    
    @classmethod
    def user_enter_confirmation(cls):
        valid_ans = ['y', 'n']
        while True:
            try:
                direction = "=> Enter [y] to confirm or [n] to reject: "
                user_confirm = input(direction).lower()
                if user_confirm not in valid_ans:
                    raise IndexError
            except IndexError:
                print("Please enter y or n!")
            else:
                return user_confirm
    
    @classmethod
    def user_enter_new_topic_name(cls, topics: list[str]):
        while True:
            try:
                new_name = cls.user_enter_topic_name()
                if new_name.lower() in topics:
                    raise ValueError
            except ValueError:
                print(f"<!> {new_name} already exist!")
            else:
                return new_name
    
    @classmethod
    def user_enter_quiz_id(cls, quiz_qty: int) -> int:
        options_valid = [str(option) for option in range(quiz_qty)]
        options_valid.append('q')
        while True:
           try:
               user_input = input("=> Enter quiz id or 'q' to quit: ")
               if user_input not in options_valid:
                   raise IndexError
           except IndexError:
               print("<!> Invalid option!")
           else:
               return user_input
    
    @classmethod
    def user_enter_quiz_edit(cls, context, current_content):
        print(f"Do you want to edit {context}?")
        user_confirmation = cls.user_enter_confirmation()
        if user_confirmation == 'y':
            return cls.user_enter_input_need_confirm(context)
        else:
            return current_content
            