import random
import hangman_art
import hangman_words

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
display = []
guesses = []

print(hangman_art.logo)

for _ in chosen_word:
    display.append("_")

def print_array_as_string(display):
    print("".join(display) + "\n")

print_array_as_string(display)

while display.count("_") > 0:
    guess = input("Guess a letter:\n").lower()[0]

    if guesses.count(guess) > 0:
        print(f"\nYou've already guessed the letter: {guess}\n")
    else:
        guesses.append(guess)
        if chosen_word.find(guess) >= 0:
            for index, letter in enumerate(chosen_word):
                if guess == letter:
                    display[index] = letter
        else:
            lives -= 1
            print(f"\nSorry {guess} is not in the word, you loose a life. Lives remaining: {lives}")
            print(hangman_art.stages[lives])
            if lives == 0:
                print("You loose.")
                exit()
        print_array_as_string(display)

print("You win!")

