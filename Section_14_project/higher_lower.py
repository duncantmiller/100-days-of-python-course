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
while keep_playing:
    choices = random.choices(game_data.data, k=2)
    print(choices)
    print_name(choices[0])
    print_description(choices[0])
    print_followers(choices[0])
    print(art.vs)
    print_name(choices[1])
    print_description(choices[1])
    guess = input("Higher type 'h' or lower type 'l'?:\n")
    if guess == "h":
        if follower_count(choices[0]) < follower_count(choices[1]):
            print("Correct!")
            correct_answers += 1
        else:
            print("Sorry you loose.")
            keep_playing = False
    elif follower_count(choices[0]) > follower_count(choices[1]):
        print("Correct!")
        correct_answers += 1
    else:
        print("Sorry you loose.")
        keep_playing = False
    print(f"Correct answers: {correct_answers}")
