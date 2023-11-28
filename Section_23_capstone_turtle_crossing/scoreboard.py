"""import turtle"""
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """scoreboard class"""
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setpos(-200, 250)
        self._print_level()

    def increment_level(self):
        """increment level"""
        self.level += 1
        self._print_level()

    def print_game_over(self):
        """Prints game over"""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def _print_level(self):
        """Prints the score"""
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
