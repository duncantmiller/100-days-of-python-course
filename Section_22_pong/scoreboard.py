class Scoreboard():
    """scoreboard class"""
    def __init__(self):
        self.left_score = 0
        self.right_score = 0

    def point_right(self):
        """increment right score"""
        self.right_score += 1

    def point_left(self):
        """increment left score"""
        self.left_score += 1
