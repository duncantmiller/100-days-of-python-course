"""turtle graphics"""
from turtle import Turtle, Screen
import random

mertle = Turtle()
screen = Screen()

mertle.shape("turtle")

def draw_shape(number, color):
    """draw individual shape"""
    mertle.pencolor(color)
    for _ in range(number):
        mertle.forward(100)
        mertle.right(360/number)

def draw_shapes():
    """draw shapes starting with square and adding on more side each time"""
    for number in range(10):
        color = colors[number]
        draw_shape(number + 4, color)

def random_walk():
    """Take a random walk with 25 steps in each direction"""
    directions = [0, 90, 180, 270]
    mertle.pensize(10)
    for _ in range(50):
        color = random.choice(colors)
        mertle.pencolor(color)
        mertle.right(random.choice(directions))
        mertle.forward(25)


colors = ["red", "green", "blue", "yellow", "black", "indigo", "violet", "orange", "pink", "cyan"]
# draw_shapes()
random_walk()
screen.exitonclick()
