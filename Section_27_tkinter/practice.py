import tkinter

window = tkinter.Tk()

window.title("A GUI Program")
window.minsize(width=500, height=300)
label = tkinter.Label(text="Label 1", font=("Arial", 24, "bold"))
label.pack()

def button_clicked():
    text = field.get()
    label.config(text=text)

button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

field = tkinter.Entry(width=10)
field.pack()

window.mainloop()
