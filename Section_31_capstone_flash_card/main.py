import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50)
canvas = tk.Canvas(width=200, height=200)
card_front_image = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(150, 100, image=card_front_image)
canvas.grid(column=1, row=0)

correct_image = tk.PhotoImage(file="images/right.png")
correct_button = tk.Button(image=correct_image, highlightthickness=0)
correct_button.grid(column=0, row=2)
incorrect_image = tk.PhotoImage(file="images/wrong.png")
incorrect_button = tk.Button(image=incorrect_image, highlightthickness=0)
incorrect_button.grid(column=2, row=2)

tk.mainloop()
