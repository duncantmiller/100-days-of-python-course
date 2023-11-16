import random
hard_chances = 5
easy_chances = 10

print("Welcome to the number guessing game")
difficulty = input("do you want to play hard or easy? Type 'hard' or 'easy':\n")
chances = easy_chances if difficulty == "easy" else hard_chances
chances_left = chances
picked_number = random.randint(1, 101)
print("You will be guessing the number I have picked between 1 and 100.")
keep_playing = True
while chances_left > 0 and keep_playing:
    print(f"You have {chances_left} guesses left.")
    guess = int(input("Enter your guess:\n"))
    if guess == picked_number:
        keep_playing = False
        print(f"You win! The number was {picked_number}.")
    elif guess > picked_number:
        print("Sorry too high.")
    else:
        print("Sorry too low.")
    chances_left -= 1

if keep_playing:
    print(f"You ran out of guesses! You lost. The number was {picked_number}.")





