import game_data
import art
import random

correct_answers = 0

print(art.logo)
print("Welcome to the higher lower game. I will give you two choices and you have to tell me which \
      has more followers, if you win you keep going until you loose.")

def follower_count(choice):
    return choice["follower_count"]

def print_name(choice):
    print(f"Name: {choice['name']}")

def print_description(choice):
    print(f"Description: {choice['description']}")

def print_followers(choice):
    print(f"Followers: {follower_count(choices[0])}")

keep_playing = True
choices = random.choices(game_data.data, k=2)
choice_1 = choices[0]
choice_2 = choices[1]
while keep_playing:
    print_name(choice_1)
    print_description(choice_1)
    print_followers(choice_1)
    print(art.vs)
    print_name(choice_2)
    print_description(choice_2)
    guess = input("Higher type 'h' or lower type 'l'?:\n")
    if guess == "h":
        if follower_count(choice_1) < follower_count(choice_2):
            print("Correct!")
            correct_answers += 1
        else:
            print("Sorry you loose.")
            keep_playing = False
    elif follower_count(choice_1) > follower_count(choice_2):
        print("Correct!")
        correct_answers += 1
    else:
        print("Sorry you loose.")
        keep_playing = False
    print(f"Correct answers: {correct_answers}")
    choice_1 = choice_2
    choice_2 = random.choice(game_data.data)
