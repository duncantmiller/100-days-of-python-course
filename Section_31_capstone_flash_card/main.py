import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
ENGLISH = "English"
FRENCH = "French"

def retrieve_words():
    """read the file contents and return a dictionary"""
    data = pandas.read_csv("data/french_words.csv")
    data_frame = pandas.DataFrame(data)
    dictionary = pandas.DataFrame.to_dict(data_frame, orient='records')
    return dictionary

def select_random_entry_from(dictionary):
    """get a random word combination"""
    return random.choice(dictionary)

def update_word_text(language, entry):
    """updates the word on the card"""
    canvas.itemconfig(word_text, text=entry[language])

def update_language_text(language):
    """updates the language on the card"""
    canvas.itemconfig(language_text, text=language)

def update_card_for(language):
    """updates the the card color"""
    if language == ENGLISH:
        canvas.itemconfig(card_image, image=card_back_image)
        canvas.itemconfig(language_text, fill="White")
        canvas.itemconfig(word_text, fill="White")
    else:
        canvas.itemconfig(card_image, image=card_front_image)
        canvas.itemconfig(language_text, fill="Black")
        canvas.itemconfig(word_text, fill="Black")

def next_word():
    """set up the next word"""
    window.after_cancel(timer)
    entry = select_random_entry_from(dictionary)
    update_word_text(FRENCH, entry)
    update_language_text(FRENCH)
    update_card_for(FRENCH)
    start_timer(entry)

def flip_card(language, entry):
    """flips the card and updates the text"""
    update_language_text(language)
    update_word_text(language, entry)
    update_card_for(language)

def start_timer(entry):
    """start the timer on the new word"""
    return window.after(3000, flip_card, ENGLISH, entry)

window = tk.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
correct_image = tk.PhotoImage(file="images/right.png")
correct_button = tk.Button(image=correct_image, highlightthickness=0, command=next_word)
correct_button.grid(column=1, row=2)
incorrect_image = tk.PhotoImage(file="images/wrong.png")
incorrect_button = tk.Button(image=incorrect_image, highlightthickness=0, command=next_word)
incorrect_button.grid(column=0, row=2)

dictionary = retrieve_words()
entry = select_random_entry_from(dictionary)
update_word_text(FRENCH, entry)

timer = start_timer(entry)

tk.mainloop()
