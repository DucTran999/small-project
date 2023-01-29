class Validate:
    """A class providing methods to ensure the player's inputs are valid."""
    
    @classmethod
    def validate_player_choice(cls) -> int:
        """Make sure the player enters existing options (1 -> 4)."""
        direction_message = "-> Enter your choice: "
        while True:  # Allow the player to re-enter until the input is valid.
            try: 
                player_input = int(input(direction_message))
                if 0 < player_input < 5: 
                    return player_input
                print("<!> Please enter 1 -> 4.")
            except ValueError:  # Show alert when player input is a character. 
                print("<!> Please enter number only!")
    
    @classmethod
    def validate_player_name(cls) -> str:
        """Make sure the player enters name is valid."""
        direction_message = "-> Your name: "
        while True:  # Allow the player to re-enter until the input is valid.
            player_name = input(direction_message).strip()
            alert_message = "<!> NOT VALID NAME"
            alert_detail = "<i> Your name is empty or over 20 character!"
            if 0 < len(player_name) < 21:
                return player_name
            print(alert_message, alert_detail, sep='\n')