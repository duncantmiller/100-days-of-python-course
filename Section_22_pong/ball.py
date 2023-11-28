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
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.1

    def serve_right(self):
        """set a random angle heading to the right"""
        self.setpos(0, 0)
        self.move_speed = 0.1
        self.x_move *= random.uniform(-1, -0.5)
        self.y_move *= random.choice([-1, 1])

    def serve_left(self):
        """set a random angle heading to the right"""
        self.setpos(0, 0)
        self.move_speed = 0.1
        self.x_move *= random.uniform(-1, -0.5)
        self.y_move *= random.choice([-1, 1])

    def move(self):
        """move forward"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """calculate bounce up/down"""
        self.y_move *= -1

    def bounce_x(self):
        """calculate bounce right/left"""
        self.x_move *= -1
        self.move_speed *= 0.9
