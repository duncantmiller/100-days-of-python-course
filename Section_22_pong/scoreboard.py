"""import turtle"""
from turtle import Turtle

class Scoreboard(Turtle):
    """scoreboard class"""
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.set_position(side)
        self._print_score()

    def set_position(self, side):
        """sets the position of the score for each side"""
        if side == "right":
            self.goto(200, 200)
        else:
            self.goto(-200, 200)

    def increment_points(self):
        """increment right score"""
        self.score += 1
        self._print_score()

    def print_game_over(self):
        """Prints game over"""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))

    def _print_score(self):
        """Prints the score"""
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 80, "normal"))
