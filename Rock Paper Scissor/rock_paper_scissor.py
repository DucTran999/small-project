import rock_paper_scissor_resource as game_feature


def rock_paper_scissor() -> None:
    """Overall game processing.

    1. Showing the gameplay.(Only first launch)
    2. Giving invitation and handling player's answer.
    """

    game_feature.load_gameplay()
    invite_msg = "Do you want to play? [y/n/gameplay]: "

    # The players can play many times and re-enter if they mistype.
    while True:
        player_ans = input(invite_msg)
        if player_ans == "n":
            print("OK! Let's play next time.")
            break
        elif player_ans == "y":
            game_feature.start_new_match()
        elif player_ans == "gameplay":
            game_feature.show_alternative_gameplay()
        else:
            # Show the message below in case their input is not valid.
            print("Please enter y, n or 'gameplay'.")


# Let's enjoy the game.
rock_paper_scissor()
