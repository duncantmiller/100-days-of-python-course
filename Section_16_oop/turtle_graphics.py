"""testing with turtle graphics"""
from turtle import Turtle, Screen

natalie = Turtle()
screen = Screen()

natalie.shape("turtle")
natalie.color("purple", "green")
natalie.pensize(10)
natalie.pendown()
natalie.left(90)
natalie.forward(100)
natalie.color("orange", "green")
natalie.left(90)
natalie.forward(100)
natalie.color("teal", "green")
natalie.left(90)
natalie.forward(100)
natalie.color("blue", "green")
natalie.left(90)
natalie.forward(100)
screen.exitonclick()
