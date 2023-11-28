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

    def serve_right(self):
        """set a random angle heading to the right"""
        self.setpos(0, 0)
        self.setheading(random.randint(-45, 45))

    def serve_left(self):
        """set a random angle heading to the right"""
        self.setpos(0, 0)
        self.setheading(random.randint(135, 225))

    def move(self):
        """move forward"""
        self.forward(10)

    def bounce_down(self):
        """calculate bounce heading down"""
        self.setheading(self.heading() - 90)

    def bounce_up(self):
        """calculate bounce heading up"""
        self.setheading(self.heading() + 90)
