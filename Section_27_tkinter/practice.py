import tkinter

window = tkinter.Tk()

window.title("A GUI Program")
window.minsize(width=500, height=300)
label = tkinter.Label(text="Label 1", font=("Arial", 24, "bold"))
label.pack()
button = tkinter.Button(text="click me")
button.pack()

window.mainloop()
