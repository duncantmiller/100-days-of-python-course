"""turtle graphics"""
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Field's snake game")
screen.tracer(0)

turtles = []

def add_turtle():
    turtle = Turtle()
    turtle.shape("square")
    turtle.color("white")
    if len(turtles) > 0:
        last_coordinates = turtles[-1].position()
        new_coordinates = (last_coordinates[0] - 20, last_coordinates[1])
    else:
        new_coordinates = (0, 0)
    turtle.penup()
    turtle.setpos(new_coordinates)
    turtles.append(turtle)

for _ in range(3):
    add_turtle()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for turtle_number in range(len(turtles) - 1, 0, -1):
        last_coordinates = turtles[turtle_number - 1].position()
        turtles[turtle_number].goto(last_coordinates)
    turtles[0].forward(20)

screen.exitonclick()
