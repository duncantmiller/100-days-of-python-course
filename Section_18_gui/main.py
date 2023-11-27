"""turtle graphics"""
from turtle import Screen
import turtle as t
import random

mertle = t.Turtle()
screen = Screen()
t.colormode(255)
mertle.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

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
        color = random_color()
        mertle.pencolor(color)
        mertle.right(random.choice(directions))
        mertle.forward(25)

def draw_spirograph(gap_size):
    """Draw a series of circles in a circle"""
    for _ in range(int(360 / gap_size)):
        mertle.setheading(gap_size + mertle.heading())
        color = random_color()
        mertle.pencolor(color)
        mertle.circle(50)

# draw_shapes()
# random_walk()
mertle.speed(0)
draw_spirograph(10)
screen.exitonclick()
