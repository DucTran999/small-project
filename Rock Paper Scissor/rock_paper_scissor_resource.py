import random

import file_reader
import utilites


def load_gameplay() -> None:
    filepath = "Rock Paper Scissor/gameplay.txt"
    file_reader.read_file_txt(filepath)


def show_alternative_gameplay() -> None:
    """Clear current console then print alternative gameplay."""

    utilites.delay(1, "Loading gameplay...")
    utilites.clear_console()
    print(
        "\n# --------------------------- Gameplay -------------------------#"
        "\n| We have three choices Rock, Paper and Scissor.                |"
        "\n| Follow these rules below:                                     |"
        "\n|    + Rock beats scissors                                      |"
        "\n|    + Scissor beats paper                                      |"
        "\n|    + Paper beats rock.                                        |"
        "\n| We will play 3 sets and who win 2 sets will win the match.    |"
        "\n# --------------------------------------------------------------#"
    )


def start_new_match() -> None:
    """Processing a game."""

    result_tracking = {"win": 0, "lose": 0, "tie": 0}
    # Clear console before starting a new game so players can track it easier.
    print("Computer: Let's play!")
    utilites.delay(1)
    utilites.clear_console()
    for set in range(1, 3):
        set_result = handle_set(set)
        new_record = result_tracking.get(set_result) + 1
        result_tracking.update({set_result: new_record})

    handle_set_three(result_tracking)


def handle_set(set_order: int) -> str:
    """Handle all events at this set.

    Processing steps:
    1. Get player and computer choice.
    2. Judging the winner.
    """

    # Small delay to make sure the computer choice is different.
    # More info: at technical specification index in rock_paper_scissor_info.txt
    utilites.delay(3, "3 seconds for thinking...")
    set_info = f"SET {set_order}"
    print(f"{set_info:-^60}")

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(
        f"\t---- Player: {format_choice(player_choice)} versus "
        f"Computer: {format_choice(computer_choice)} ----"
    )

    return get_result(player_choice, computer_choice)


def get_player_choice() -> str:
    """Get the player's choice and make sure it's valid."""

    valid_choices = ["s", "p", "r"]
    direction_message = "-> Enter s(scissor), p (paper), r (rock): "
    while True:
        user_ans = input(direction_message).lower().strip()
        if user_ans in valid_choices:
            return user_ans
        print("<!> Invalid! Please enter s, p or r!")


def get_computer_choice() -> str:
    """Generate computer choice in random."""

    # Generate the seed
    factor_1 = random.randint(1545548, 45676765464)
    factor_2 = random.randint(5465786, 456745454464)
    seed_generated = factor_1 * factor_2
    random.seed(seed_generated)
    choice_list = ["s", "r", "p"]
    random.shuffle(choice_list)

    computer_choice = random.choice(choice_list)
    return computer_choice


def get_result(player_choice: str, computer_choice: str) -> str:
    """Evaluation of set results from the player's perspective."""

    player_win_cases = [
        ["r", "s"],
        ["s", "p"],
        ["p", "r"]
    ]
    if player_choice == computer_choice:
        print("<i> Set: Tie!")
        return "tie"
    if [player_choice, computer_choice] in player_win_cases:
        print("<i> You won this set!")
        return "win"
    print("<i> You lost this set!")
    return "lose"


def format_choice(short_key: str) -> str:
    choice_formated: dict = {
        "s": "Scissor",
        "r": "Rock",
        "p": "Paper"
    }
    return choice_formated.get(short_key, "Not defind")


def handle_set_three(result_tracking: dict) -> None:
    """Review the results after two sets and start a third set if necessary."""

    times_list = list()  # Easier to get the win, lose, and tie times.
    # If a player has 2 wins or loses games. Game 3 is not necessary.
    for result, times in result_tracking.items():
        times_list.append(times)
        if result != "tie" and times == 2:
            print(f"#-------> You {result} to fast! <-------#")
            return

    final_set_rs = handle_set(3)
    finding_the_winner(times_list, final_set_rs)


def finding_the_winner(times_list, final_set_rs: str):
    win, lose, tie = times_list

    if win == lose:
        final_rs = f"{final_set_rs.upper()} GAME!"
        print(f"#{final_rs:-^60}#")
        return

    if (tie == lose and final_set_rs == "win") or (
        tie == win and final_set_rs == "lose"
    ):
        print(f"#{'TIE MATCH!':-^60}#")
    elif tie == lose:
        print(f"#{'YOU LOST!':-^60}#")
    elif tie == win:
        print(f"#{'YOU WON!':-^60}#")
