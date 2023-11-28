"""import turtle"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """player class"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.reset_position()

    def reset_position(self):
        """return home"""
        self.setpos(STARTING_POSITION)

    def move_up(self):
        """move up"""
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        """move left"""
        self.setx(self.xcor() - MOVE_DISTANCE)

    def move_right(self):
        """move right"""
        self.setx(self.xcor() + MOVE_DISTANCE)
