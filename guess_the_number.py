""" A small funny game. I chose a number and you have 3 chance to guess it. """
import sys
from random import randint

def generate_secret_number():
    # use function randint() to generate a number in range.
    secret_num = randint(1, 10)
    return secret_num

def check_guess(secret_num, friend_guess):
    # Check friend's guess and give some hint.
    if secret_num < friend_guess:
        print('Your guess is too high.')
    elif secret_num > friend_guess:
        print('Your guess is too low.')
    else:
        return True
    return False

def start_a_new_game():
    secret_num = generate_secret_number()
    try:
        # give your friend 3 guess.
        for chance in range(1, 4):
            if chance == 1:
                friend_guess = input("Enter your guess: ")
                if check_guess(secret_num, int(friend_guess)):
                    print(f'OMG. You guess it at first chance!')
                    break
            elif chance == 2:
                friend_guess = input("Your second chance: ")
                if check_guess(secret_num, int(friend_guess)):
                    print(f'Yes, my secret number is: {secret_num}. You won!')
                    break
            else:
                friend_guess = input("You last chance: ")
                if check_guess(secret_num, int(friend_guess)):
                    print(f"Ahh! I almost win. {secret_num} is correct.")
                else:
                    print("LOL. I win!")
    except ValueError:
        # if you friend answer a letter.
        print("I said number. What's wrong with you!")
        print("I don't want to play with you! Goodbye.")
        sys.exit()
            
""" The main programme."""
def guess_number_programme():
    message = 'I had chosen a secret number in range 1 to 10'
    message += "\nYou have 3 chances to guess it."
    print(message)
    while True:
        answer = input("Do you want to play? ('y' : Yes and 'n' : No) ")
        if answer.lower() == 'n':
            print("OK. We can do it another time.")
            sys.exit()
        elif answer == 'y':
            start_a_new_game()
            print("-------------------New game ------------------")
        else:
            print("Please typo only 'y' or 'n'")

# Let's enjoy the game.
guess_number_programme()