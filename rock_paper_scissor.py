""" A simple game for kid practices think more logical."""

import sys
from random import randint


"""Check user input is valid or not."""
def get_user_answer():
    user_ans = input("Enter s (scissor), p (paper), r (rock): ").lower()
    user_choice = convert_answer(user_ans)
    if check_answer_valid(user_ans):
        return user_choice

def convert_answer(user_ans):
    # convert user answer:
    # s: scissor, r: rock, p: paper
    if user_ans == 's':
        return 'scissor'
    elif user_ans == 'r':
        return 'rock'
    elif user_ans == 'p':
        return 'paper'
    else:
        print("Please typo only s, r or p!")
        return 'not excepted'
    
def check_answer_valid(user_ans):
    if user_ans == 'not excepted':
        return False
    else:
        return True

"""Generate computer choice in random"""
def get_computer_answer():
    choice_list = ["Scissor", "Rock", "Paper"]
    computer_ans = choice_list[randint(0, 2)]
    return computer_ans

"""Main process to consider who win the round and game"""
def current_round_result(user_choice, computer_choice):
    # consider the final result of current round result
    u_choice = user_choice.title()
    c_choice = computer_choice.title()
    if u_choice == 'Not Excepted':
        print("You break the rule. I don't want to play with you!")
        print("BYE!")
        sys.exit()
    else:    
        print(f"\t...{u_choice} versus {c_choice}...")
        return get_round_result(u_choice, c_choice)
        
def get_round_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(user_choice, computer_choice)
        return 'Tie'
    else:
        return rule_check(user_choice, computer_choice)

def rule_check(user_choice, computer_choice):
    # game rules help to defind match result.
    if user_choice == 'Rock' and computer_choice == 'Scissor':
        return 'Win'
    if user_choice == 'Scissor' and computer_choice == 'Paper':
        return 'Win'
    if user_choice == 'Paper' and computer_choice == 'Rock':
        return 'Win'
    return 'Lose'

def consider_final_result(wins, ties, loses):
    print(f"wins: {wins} ties: {ties} loses: {loses}")
    # the final result is considered after rounds 3
    if wins == 2:
        return "YOU WON THE GAME!"
    elif loses == 2:
        return "YOU LOST THE GAME!"
    elif wins == 1 and ties == 2:
        return "YOU WON THE GAME!"
    elif loses == 1 and ties == 2:
        return "YOU LOST THE GAME!"
    elif (wins == 1 and ties == 1 and loses == 1) or (ties == 3):
        return "GAME TIE!"

""" 2 main function to run this game:
    load_game_play()
    run_game()
"""
def load_game_play():
    # load gameplay from gameplay folder.
    gameplay_path = 'gameplay/rock_paper_scissor_gameplay.txt'
    with open(gameplay_path) as file_object:
        game_play = file_object.read()
    print(game_play)
    
def run_game():
    # Invite player to join the game, if they agree so start the game
    invite_msg = "Do you want to play? (y: 'Yes' or n: 'No') "
    while True:
        player_ans = input(invite_msg).lower()
        if player_ans == 'n':
            print("OK! Let's play next time.")
            sys.exit()
        elif player_ans == 'y':
            start_new_game()
            print("\n------------------- New game ----------------")
        else:
            print("Please enter only 'y' or 'n'.") 

def start_new_game():
    rounds, wins, ties, loses = 1, 0, 0, 0    
    finished_flag = 0 
    
    while rounds < 4:
        
        # get user choice and computer choice
        print(f"Round {rounds}: ")
        user_choice = get_user_answer()
        computer_choice = get_computer_answer()
        match_rs = current_round_result(user_choice, computer_choice)
        print(f"-> Round {rounds} you {match_rs}!")
        
        # tracking total win, tie and lose games.
        if match_rs == 'Win':
            wins += 1
        elif match_rs == 'Tie':
            ties += 1
        elif match_rs == 'Lose':
            loses += 1
        
        # If 2 lose or win contigous two rounds, don't need round 3.
        if rounds == 2: 
            if wins == 2:
                finished_flag = 1
                print("YOU WON THE GAME BY 2 ROUNDS!")
                break
            elif loses == 2:
                finished_flag = 1
                print("YOU LOST THE GAME TOO FAST!")
                break
        
        rounds += 1
    if not finished_flag:
        print(consider_final_result(wins, ties, loses))
        
# main process of the programme
def game_programme():
    load_game_play()
    run_game()

# Let's enjoy the game.
game_programme()