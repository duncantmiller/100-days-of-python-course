"""imports"""
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

answer = screen.textinput(title="Guess the State", prompt="What's another state name?")

data = states_data[states_data.state == answer]

print(data)

turtle.mainloop()
