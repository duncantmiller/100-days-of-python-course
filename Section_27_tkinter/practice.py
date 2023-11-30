import tkinter

window = tkinter.Tk()

window.title("A GUI Program")
window.minsize(width=500, height=300)
label = tkinter.Label(text="Label 1", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

def button_clicked():
    text = field.get()
    label.config(text=text)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)
button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

field = tkinter.Entry(width=10)
field.grid(column=3, row=2)

window.mainloop()
