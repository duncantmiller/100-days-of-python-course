from turtle import Turtle

class Snake:
    """Snake class"""

    def __init__(self):
        self.links = []
        self._create_snake()

    def _create_snake(self):
        for _ in range(3):
            self.add_link()

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
        links[0].forward(20)
