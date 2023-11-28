"""imports"""
from turtle import Turtle
import random

class Ball(Turtle):
    """Ball class"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def set_random_heading_right(self):
        """set a random angle heading to the right"""
        self.setheading(random.randint(-45, 45))

    def move(self):
        """move forward"""
        self.forward(10)
