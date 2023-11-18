"""turtle graphics"""
from turtle import Turtle, Screen

mertle = Turtle()
screen = Screen()

mertle.shape("turtle")

def draw_shape(number, color):
    """draw individual shape"""
    mertle.pencolor(color)
    for _ in range(number):
        mertle.forward(100)
        mertle.right(360/number)

colors = ["red", "green", "blue", "yellow", "black", "indigo", "violet", "orange", "pink", "cyan"]

def draw_shapes():
    """draw shapes starting with square and adding on more side each time"""
    for number in range(10):
        color = colors[number]
        draw_shape(number + 4, color)

draw_shapes()
screen.exitonclick()
