import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"

def retrieve_words():
    data = pandas.read_csv("data/french_words.csv")
    data_frame = pandas.DataFrame(data)
    dictionary = pandas.DataFrame.to_dict(data_frame, orient='records')
    print(dictionary)

window = tk.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
correct_image = tk.PhotoImage(file="images/right.png")
correct_button = tk.Button(image=correct_image, highlightthickness=0)
correct_button.grid(column=1, row=2)
incorrect_image = tk.PhotoImage(file="images/wrong.png")
incorrect_button = tk.Button(image=incorrect_image, highlightthickness=0)
incorrect_button.grid(column=0, row=2)

retrieve_words()
tk.mainloop()
