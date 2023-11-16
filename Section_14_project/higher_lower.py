import game_data
import art
import random
import os

print(art.logo)
print("Welcome to the higher lower game. I will give you two choices and you have to tell me which \
      has more followers, if you win you keep going until you loose.")

def follower_count(choice):
    return choice["follower_count"]

def name(choice):
    return choice['name']

def print_name(choice):
    print(f"Name: {name(choice)}")

def print_description(choice):
    print(f"Description: {choice['description']}")

def print_followers(choice):
    print(f"Followers: {follower_count(choice)}")

def check_correct(guess, followers_1, followers_2):
    if guess == "h":
        if followers_1 < followers_2:
            return True
        else:
            return False
    elif followers_1 > followers_2:
        return True
    return False

def select_random_choice():
    return random.choice(game_data.data)

def are_choices_duplicates(choice_1, choice_2):
    return choice_1 == choice_2

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

correct_answers = 0
keep_playing = True
choice_1 = select_random_choice()
choice_2 = select_random_choice()
while keep_playing:
    need_new_choices = are_choices_duplicates(choice_1, choice_2)
    while need_new_choices:
        choice_2 = select_random_choice()
        need_new_choices = are_choices_duplicates(choice_1, choice_2)
    print_name(choice_1)
    print_description(choice_1)
    print_followers(choice_1)
    print(art.vs)
    print_name(choice_2)
    print_description(choice_2)
    guess = input(f"\nDoes {name(choice_2)} have a higher type 'h' or lower type 'l' follower count than {name(choice_1)}:\n")
    if check_correct(guess, follower_count(choice_1), follower_count(choice_2)):
        clear()
        print("Correct!")
        correct_answers += 1
    else:
        print("Sorry you loose.")
        keep_playing = False
    print(f"Correct answers: {correct_answers}\n")
    choice_1 = choice_2
    choice_2 = select_random_choice()
