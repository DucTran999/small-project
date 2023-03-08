class Validation:
    """Ensuring user input is valid
    
    This class provides methods to validate the user input. The Views call these
    methods to present a complete input form. If a user makes a mistake, let them
    re-enter it. That increases the program error resistance and also makes the 
    Controller thinner.
    """
    @classmethod
    def get_user_option(cls, valid_options: tuple, message: str):
        while True:
            try:
                user_inp = input(message)
                cls.user_option_validation(user_inp, valid_options)
            except ValueError as e:
                print(e)
            else:
                return user_inp
    
    @classmethod
    def user_option_validation(cls, user_inp, valid_inp: list):
        if user_inp not in valid_inp:
            raise ValueError('Invalid option!')
        else:
            return user_inp
    
    @classmethod
    def get_player_name(cls, avoid_name: str):
        while True:
            try:
                user_inp = input("=> Enter player name: ").strip()
                cls.user_name_validation(user_inp, avoid_name)
            except ValueError as e:
                print(e)
            else:
                return user_inp
    
    @classmethod
    def user_name_validation(cls, name: str, avoid_name: str):
        if len(name) == 0:
            raise ValueError("<!> Empty name not excepted!")
        elif len(name) > 30:
            raise ValueError('<!> Name cannot over 30 chars')
        elif name == avoid_name:
            raise ValueError('<!> Name exist!')
        else:
            return name
    
    @classmethod
    def get_seahorse_id(cls, id_list: list[int], message):
        while True:
            try:
                user_inp = int(input(message))
                cls.user_option_validation(user_inp, id_list)
            except ValueError:
                print('Invalid id')
            else:
                return user_inp
    
    @classmethod
    def seahorse_id_vali(cls, user_inp, valid_inp: list):
        if user_inp not in valid_inp:
            raise ValueError('Invalid option!')
        else:
            return user_inp