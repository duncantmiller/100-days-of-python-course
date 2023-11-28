from turtle import Turtle

class Paddle():
    """Paddle class"""

    def __init__(self):
        self.links = []
        self._make_links()
        self.head = self.links[0]

    def _make_links(self):
        """builds the links"""
        for index in range(5):
            link = Turtle()
            link.shape("square")
            link.color("white")
            self.links.append(link)
            link.penup()
            link.setpos(350, 40 - (index * 20))

    def up(self):
        """move paddle up 1"""
        self._move_paddle(1)

    def down(self):
        """move paddle down 1"""
        self._move_paddle(-1)

    def _move_paddle(self, amount):
        """move paddle by amount"""
        for link in self.links:
            link.sety(link.ycor() + (amount * 20))
