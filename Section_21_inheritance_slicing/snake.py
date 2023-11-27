UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle

class Snake:
    """Snake class"""

    def __init__(self):
        self.links = []
        self._create_snake()
        self.head = self.links[0]

    def _create_snake(self):
        for _ in range(3):
            self.add_link()

    def up(self):
        """Turn first link up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn first link down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn first link left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn first link right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_link(self):
        """adds a new snake link"""
        link = Turtle()
        link.shape("square")
        link.color("white")
        links = self.links
        if len(links) > 0:
            last_coordinates = links[-1].position()
            new_coordinates = (last_coordinates[0] - 20, last_coordinates[1])
        else:
            new_coordinates = (0, 0)
        link.penup()
        link.setpos(new_coordinates)
        self.links.append(link)

    def move(self):
        """moves all the links to the next forward position"""
        links = self.links
        for link_number in range(len(links) - 1, 0, -1):
            last_coordinates = links[link_number - 1].position()
            links[link_number].goto(last_coordinates)
        self.head.forward(20)
