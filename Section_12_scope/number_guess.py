import random
HARD_CHOICES = 5
EASY_CHOICES = 10

def decrement_chances(chances):
    chances -= 1
    return chances

def check_guess(guess, picked_number):
    keep_playing = True
    if guess == picked_number:
        keep_playing = False
        print(f"You win! The number was {picked_number}.")
    elif guess > picked_number:
        print("Sorry too high.")
    else:
        print("Sorry too low.")
    return keep_playing

def set_difficulty(difficulty):
    chances = EASY_CHOICES if difficulty == "easy" else HARD_CHOICES
    return chances

def play():
    difficulty = input("do you want to play hard or easy? Type 'hard' or 'easy':\n")
    chances_left = set_difficulty(difficulty)
    picked_number = random.randint(1, 100)
    print("You will be guessing the number I have picked between 1 and 100.")
    keep_playing = True
    while chances_left > 0 and keep_playing:
        print(f"You have {chances_left} guesses left.")
        guess = int(input("Enter your guess:\n"))
        keep_playing = check_guess(guess, picked_number)
        chances_left = decrement_chances(chances_left)

    if keep_playing:
        print(f"You ran out of guesses! You lost. The number was {picked_number}.")

print("Welcome to the number guessing game")
play()
