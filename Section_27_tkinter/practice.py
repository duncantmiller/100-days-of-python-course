import tkinter

window = tkinter.Tk()

def add(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add(1, 2, 3, 4))
window.title("A GUI Program")
window.minsize(width=500, height=300)
label = tkinter.Label(text="Label 1", font=("Arial", 24, "bold"))
label.pack()

window.mainloop()
