"""turtle graphics"""
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Field's snake game")

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
    turtle.setpos(new_coordinates)
    turtles.append(turtle)

for _ in range(3):
    add_turtle()

screen.exitonclick()
