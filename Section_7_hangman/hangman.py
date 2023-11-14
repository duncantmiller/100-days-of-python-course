import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"testing {chosen_word}")

display = []
for _ in chosen_word:
    display.append("_")

print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while display.count("_") > 0:
    guess = input("Guess a letter:\n").lower()

    if chosen_word.find(guess) >= 0:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                display[index] = letter

    print(display)

print("You win!")

