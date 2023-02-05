import os
import secrets


def generate_secret_number() -> int:
    #The "secrets module" to generate strong random numbers
    #More info at: https://docs.python.org/3/library/secrets.html
    number_list = [num for num in range(1, 11)]
    secret_number = secrets.choice(number_list)
    print("Computer: I have chosen. Now, you can guess it!")
    return secret_number


def is_guess_correct(secret_num: int, player_guess: int) -> bool:
    """ Avaluate the guess and show hint message depending on player guess."""
    
    if player_guess < secret_num:
        print("<i> Your guess is too low.")
    elif player_guess > secret_num:
        print("<i> Your guess is too high.")
    else:
        return True
    return False


def get_player_guess(annoucement_msg: str) -> str:
    """Get player input and make sure it is a number."""
    print(annoucement_msg)
    print(" -> Enter your guess: ", end='')
    while True:  # Allow player enter again until input is valid.
        try:
            player_guess = int(input())
        except ValueError:
            err_message = "<!> Please enter number only!"
            print(err_message)
            print(" -> Enter again: ", end='')
        else:
            return player_guess


def handle_player_guess(secret_num: int) -> None:
    """Give player chance to guess and evalute their guess."""
    
    # computer speechs: A list containing the speeches for each player's guess.
    # ["guess order announcement message", "message if thier guess correct"]
    computer_speechs = [
        ["<?> Your first chance.", "OMG. You guess it at first chance!"],
        ["<?> Your second chance", f"Yes, my secret number is: {secret_num}." ],
        ["<?> Your last chance", f"Ahh! I almost win. {secret_num} is correct."]
    ]
    
    for chance in range(0, 3):
        announcement, congratulation_msg  = computer_speechs[chance]
        player_guess = get_player_guess(announcement)
        if is_guess_correct(secret_num, player_guess):
            print(congratulation_msg)
            return
        print("-" * 25)
        
    # This message will be printed if the player's guesses are all wrong.
    print("Computer: Yeah! I win this game.")  


def start_a_new_game() -> None:
    secret_num = generate_secret_number()
    handle_player_guess(secret_num)


def build_gameplay_path() -> str:
    """Avoid FileNotFoundError just in case the current working directory name
    is small_project or Guessing Number.
    """
    
    cur_directory_path: str = os.getcwd()
    folder_name: str = os.path.basename(cur_directory_path)
    if folder_name == "small_project":
        return f"Guessing Number/guessing_number_gp.txt"
    else:
        return "guessing_number_gp.txt"


def show_alternative_gameplay() -> None:
    contents = (f"#{'Gameplay':-^60}#\n"
                "I pick a number from 1 to 10. You have 3 chances to guess.\n"
                "Also a little hint after the first and second wrong guess.\n"
                "If all your guesses are wrong, I win. If not, you win!"
                f"#{'-' * 60}#")
    print(contents)


def load_gameplay() -> str:
    """Ensuring that error while reading file not crash the game."""
    try:
        gameplay_path: str = build_gameplay_path()
        with open(gameplay_path) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        show_alternative_gameplay()
    else:
        print(contents)


def guess_number_programme():
    """The main function which control the overall game process."""
    load_gameplay()
    invitation = "Do you want to play? [y/n]: "
    while True:
        player_ans = input(invitation).lower()
        if player_ans == 'n':
            print("OK. We can play together at another time!")
            break
        elif player_ans == 'y':
            os.system('cls')
            start_a_new_game()
        else:
            # Handle exception the user's input is not y or n.
            print("<!> Please enter 'y' or 'n'. 'Y' or 'N also accepted.")


# Let's enjoy the game.
guess_number_programme()