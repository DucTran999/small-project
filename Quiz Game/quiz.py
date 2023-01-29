""" A simple game make your revision more efficient
    If you want more topics or questions. Just add it in folder quiz_resources
"""

import sys
import json
from time import sleep

""" 
    Two basis function of this game:
    load_gameplay(): load gameplay content from gameplay file
    run_game(): operating the game.
"""
def load_gameplay():
    try:
        gameplay_path = 'gameplay/quiz_gameplay.txt'
        with open(gameplay_path) as file_obj:
            gameplay = file_obj.read()
    except FileNotFoundError:
        print("We have some problem while loading the gameplay.")
    else:
        print(gameplay)

def run_game():
    invite_msg1 = "Do you want to play? (y/Yes or n/No) "
    invite_msg2 = "Want to try other topic? (y/Yes or n/No) "
    fisrt_game = True
    
    while True:
        # if the first time player enjoy print invite_msg1
        #  if not, we print invite_msg2
        if fisrt_game:
            player_ans = input(invite_msg1).lower()
            fisrt_game = False
        else:
            player_ans = input(invite_msg2).lower()
        
        handle_player_ans(player_ans)
            
def handle_player_ans(player_ans):
    # handle player input
    if player_ans == 'n' or player_ans == 'no':
        print("OK! Goodbye.")
        sys.exit()
    elif player_ans == 'y' or player_ans == 'yes':
        print("OK! Let's start the game.")
        start_new_game()
    else:
        print("Wanring: ")
        print("---!--- Please enter y or Yes if you want to play.")
        print("--!!!-- Enter n or no if you refuse.")

def start_new_game():
    topics = load_topics()
    show_topics(topics)
    player_chosen = get_player_choice(topics)
    start_quiz(player_chosen, topics)
    
def load_topics():
    try:
        topic_path = "quiz_resource/topics.txt"
        with open(topic_path, 'r') as file_obj:
            topics = file_obj.readlines()
    except Exception as e:
        print("An error has occurred while load topics list.")
        print(f"Error name: {e}")
    else:
        return topics

def show_topics(topics):
    # print list of topics
    number_of_topics = len(topics)
    print("----------------------------------------------")
    print(f"\t\t::: {number_of_topics} Topics Available:::")
    for index, name in enumerate(topics):
        print(f" --- {index}. {name.strip()}", end='\n')
    print("----------------------------------------------")

def get_player_choice(topics):
    # get player choice
    number_of_topic = len(topics)
    while True:
        try:
            # Check player input is valid or not.
            #  only topic's IDs shown are valid.  
            require_msg = "Enter Topic's ID you want (Ex: 0, 1, etc.): "
            player_choice = int(input(require_msg))
            if player_choice < 0 or player_choice >= number_of_topic:
                print("Topic's ID not exist!")
            else:
                return player_choice       
        except ValueError:
            print("Please enter number only!")

def start_quiz(player_chosen, topics):
    quizs = load_quiz(player_chosen, topics)
    confirm_player_ready()
    show_quiz_and_check_player_ans(quizs)

def load_quiz(player_chosen, topics):
    # load all quiz stored in json file
    topic_name = topics[player_chosen].strip()
    quiz_path = f"quiz_resource/{topic_name}_quiz.json"
    try:    
        with open(quiz_path, 'r') as json_obj:
            quiz_list = json.load(json_obj)
    except Exception as e:
        print("An error has occured while loading the quizs.")
        print("---> Error name: {e}")
    else:
        print("Load quizs successful!")
        return quiz_list

def confirm_player_ready():
    # wait flag is used to print suitable message when player not ready.
    wait_flag = 0
    while True:
        # if player ready after 5s show the quizs
        #  if not give them 60s to ready.
        player_ans = input("\t(?)Are you ready? (y/Yes) or (n/No): ").lower()
        
        if player_ans == 'y' or player_ans == 'yes':
            print("Quizs will appear after 5 second!")
            count_down_timer()
            break
        elif player_ans == 'n' or player_ans == 'no':
            if wait_flag == 0:
                print("OK! I give you 60 secondes!")
                wait_flag = 1
                sleep(54)
                print("5s left", end=' ')
                count_down_timer()
            else:
                print("OK! The last 60s!")
                sleep(54)
                print("5s left", end=' ')
                count_down_timer()
                print("Quizs will appear after 5 second!")
                count_down_timer()
                break
        else:
            print("Please enter one of 4: y, n, yes or no.")
            
def count_down_timer():
    # count down last 5 seconds to make player focus
    for i in range(5, 0, -1):
        print(i, end=' ')
        sleep(1)
    print()

def show_quiz_and_check_player_ans(quizs):
    key_ans_list = []
    player_ans_list = []
    for quiz in quizs:
        ans_key = get_quiz_content(quiz)
        key_ans_list.append(ans_key.lower())
        player_ans = validate_player_ans()
        player_ans_list.append(player_ans.lower())
    check_player_ans(key_ans_list, player_ans_list)

def check_player_ans(key_list, ans_list):
    total_correct = 0
    for i in range(0, 5):
        if ans_list[i] != key_list[i]:
            print(f"Question {i}: Wrong answer!. The answer is {key_list[i]}.")
        else:
            print(f"Question {i}: Correct answer!")
            total_correct += 1
    show_encourage_message(total_correct)

def show_encourage_message(total_correct):
    if total_correct == 0:
        print("Total correct: 0 / 5")
        print("Don't worry. Failure is mother's success")
    elif total_correct == 1:
        print("Total correct: 1 / 5")
        print("Don't give up. Persistence is key to success.")
    elif total_correct == 2:
        print("Total correct: 2 / 5")
        print("The more you try, the closer you get to success.")
    elif total_correct == 3:
        print("Total correct: 3 / 5")
        print("Good result! Repeat is mothering of learning.")
    elif total_correct == 4:
        print("Total correct: 4 / 5")
        print("Great! You do it almost perfectly.", end=' ')
        print("I think you really love this field.")  
    else:
        print("Total correct: 5 / 5")
        print("Fantastic! You must be expert in this field.")  

def get_quiz_content(quiz):
    # print the question part 
    control_print_info = 0
    for key, value in quiz.items():
        if control_print_info == 0:
            print(f"Question {key}. {value.capitalize()}")
        elif control_print_info == 4:
            return value
        else:
            print(f"({key}) {value}")
        control_print_info += 1

def validate_player_ans():
    while True:
        player_ans = input("Enter your answer: ").lower()
        if player_ans != 'a' and player_ans != 'b' and player_ans != 'c':
            print("Please enter only A, B or C!")
        else:
            return player_ans
        
def quiz_progame():
    load_gameplay()
    run_game()

# Let's enjoy the game
quiz_progame()