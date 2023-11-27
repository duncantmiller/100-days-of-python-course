"""turtle graphics"""
import turtle as t
import random

is_game_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

if user_bet:
    is_game_on = True

turtles = []
for number in range(6):
    color = colors[number]
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-230, y=(number*30)-50)
    turtles.append(turtle)

while is_game_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print(f"Sorry you lost, the {winning_color} turtle won.")

screen.exitonclick()
