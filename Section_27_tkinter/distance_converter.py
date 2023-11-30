import tkinter as tk

def calculate():
    miles = float(miles_field.get())
    km = miles * 1.609
    answer_label.config(text=km)

window = tk.Tk()
window.config(padx=20, pady=20)

miles_field = tk.Entry(width=10)
miles_field.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

answer_label = tk.Label(text="0")
answer_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

tk.mainloop()
