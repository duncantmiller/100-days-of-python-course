"""import turtle"""
from turtle import Turtle

LINK_SIZE = 20

class Paddle(Turtle):
    """Paddle class"""

    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.reset_paddle(side)

    def up(self):
        """move paddle up 1"""
        self._move_paddle(1)

    def down(self):
        """move paddle down 1"""
        self._move_paddle(-1)

    def _move_paddle(self, amount):
        """move paddle by amount"""
        self.sety(self.ycor() + (amount * LINK_SIZE))

    def reset_paddle(self, side):
        """set paddle at home position"""
        if side == "right":
            self.goto(350, 0)
        else:
            self.goto(-350, 0)
