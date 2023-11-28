"""import turtle"""
from turtle import Turtle

LINK_SIZE = 20
PADDLE_LINKS = 5

class Paddle():
    """Paddle class"""

    def __init__(self, home_xcor):
        self.links = []
        self._make_links()
        self.home_xcor = home_xcor
        self.reset_paddle()

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

    def reset_paddle(self):
        """set paddle at home position"""
        for index, link in enumerate(self.links):
            link.setpos(self.home_xcor, 40 - (index * LINK_SIZE))

    def shrink(self):
        """shrink if possible"""
        if len(self.links) > 1:
            self.links[-1].hideturtle()
            new_links = self.links[:-1]
            self.links = new_links
