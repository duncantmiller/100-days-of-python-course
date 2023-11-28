from turtle import Turtle

class Scoreboard(Turtle):
    """Keeps track of the score"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        with open("high_score.txt", encoding="utf-8") as file:
            self.high_score = int(file.read())
        file.close()
        self._print_score()

    def increment_score(self):
        """Adds one to score"""
        self.score += 1
        self._print_score()

    def reset(self):
        """Resets score and high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w", encoding="utf-8") as file:
                file.write(str(self.high_score))
        self.score = 0
        self._print_score()

    def _print_score(self):
        """Prints the score"""
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
