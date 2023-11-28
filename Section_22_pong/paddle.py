"""import turtle"""
from turtle import Turtle

LINK_SIZE = 20
PADDLE_LINKS = 5

class Paddle():
    """Paddle class"""

    def __init__(self, side):
        self.links = []
        self._make_links()
        self.reset_paddle(side)

    def _make_links(self):
        """builds the links"""
        for _ in range(PADDLE_LINKS):
            link = Turtle()
            link.shape("square")
            link.color("white")
            self.links.append(link)
            link.penup()

    def up(self):
        """move paddle up 1"""
        self._move_paddle(1)

    def down(self):
        """move paddle down 1"""
        self._move_paddle(-1)

    def _move_paddle(self, amount):
        """move paddle by amount"""
        for link in self.links:
            link.sety(link.ycor() + (amount * LINK_SIZE))

    def reset_paddle(self, side):
        """set paddle at home position"""
        if side == "right":
            home = 350
        else:
            home = -350
        for index, link in enumerate(self.links):
            link.setpos(home, 40 - (index * LINK_SIZE))
