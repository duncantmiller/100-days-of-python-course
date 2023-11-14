import random
import hangman_art
import hangman_words

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
display = []
guesses = []

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#TODO-2: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangman_art.logo)

print(f"testing {chosen_word}")

for _ in chosen_word:
    display.append("_")

def print_array_as_string(display):
    print("".join(display) + "\n")

print_array_as_string(display)

while display.count("_") > 0:
    guess = input("Guess a letter:\n").lower()

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
            #TODO-3: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

            print(f"\nSorry {guess} is not in the word, you loose a life. Lives remaining: {lives}")
            print(hangman_art.stages[lives])
            if lives == 0:
                print("You loose.")
                exit()
        #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

        #Join all the elements in the list and turn it into a String.
        print_array_as_string(display)

print("You win!")

