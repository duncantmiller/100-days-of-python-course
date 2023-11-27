"""turtle graphics"""
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Field's snake game")

field = Turtle()
field.shape("square")
field.color("white")

screen.exitonclick()
