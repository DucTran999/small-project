class Validate:
    """Validate all input from player."""
    
    def validate_player_choice(self):
        """Ensure player input only 1, 2 or 3"""
        
        while True:
            try:
                player_inp = int(input("-> Your choice: "))
                if player_inp > 0 and player_inp < 4:
                    return player_inp
                else:
                    print("<!> Please enter 1, 2 or 3!")
            except ValueError:
                print("<!> Enter number only!")

    def validate_player_name(self):
        """Ensure player input name not over 20 chars and not empty.
            Nickname accepted.
        """
        
        while True:
            player_inp = input("Enter your name: ").strip()
            if len(player_inp) == 0:
                print("<!> Empty name or all whitespace is not excepted!")
            elif len(player_inp) > 20:
                print("<!> Your name is over 20 chars!")
            else:
                return player_inp.capitalize()

    def validate_hippo_exist(self, order_list):
        while True:
            try:
                player_inp = int(input("-> Enter hippo order: "))
                if player_inp in order_list:
                    return player_inp
                else:
                    print("<!> Hippo order not valid!")
            except ValueError:
                print("<!> Enter number only!")           