"""The part of the program that handles the score"""
from turtle import Turtle


class Score(Turtle):
    """The module for keeping the score"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the current score"""
        self.clear()
        self.goto(0, 240)
        self.write(self.player_score, align="center", font=("Courier", 40, "normal"))

    def player_point(self):
        """Increment score when called"""
        self.player_score += 1
        self.update_scoreboard()
