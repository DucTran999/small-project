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
                user_inp = input(message).strip()
                cls.user_option_validation(user_inp, valid_options)
            except ValueError as e:
                print(e)
            else:
                return user_inp
    
    @classmethod
    def user_option_validation(cls, user_inp: str, valid_inp: list):
        if user_inp in valid_inp:
            return user_inp
        else:
            raise ValueError('Invalid option!')
    
    @classmethod
    def get_player_name(cls, avoid_name: str, message: str):
        while True:
            try:
                user_inp = input(message).strip()
                cls.user_name_validation(user_inp, avoid_name)
            except ValueError as e:
                print(e)
            else:
                return user_inp
    
    @classmethod
    def user_name_validation(cls, name: str, avoid_name: str):
        if len(name) == 0:
            raise ValueError("<!> Empty name not excepted!")
        elif len(name) > 20:
            raise ValueError('<!> Name cannot over 30 chars')
        elif name == avoid_name:
            raise ValueError('<!> Name exist!')
        else:
            return name
    
    @classmethod
    def get_seahorse_id(cls, id_list: list[int], message):
        while True:
            try:
                user_inp = input(message).strip()
                return cls.seahorse_id_valid(user_inp, id_list)
            except ValueError as err_message:
                print(err_message)
    
    @classmethod
    def seahorse_id_valid(cls, user_inp: str, valid_inp: list):
        if len(user_inp) == 0:
            raise ValueError("Empty is invalid.")
        elif int(user_inp) not in valid_inp:
            raise ValueError("Invalid id")
        else:
            return int(user_inp)