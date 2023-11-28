from turtle import Turtle

class Scoreboard(Turtle):
    """Keeps track of the score"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self._print_score()

    def increment_score(self):
        """Adds one to score"""
        self.score += 1
        self._print_score()

    def print_game_over(self):
        """Prints game over"""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))

    def _print_score(self):
        """Prints the score"""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
