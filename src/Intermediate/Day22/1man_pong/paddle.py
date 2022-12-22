"""The part of the program that controls the paddle"""
from turtle import Turtle


class Paddle(Turtle):
    """The paddle class"""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def left(self):
        new_x = self.xcor() - 20
        while new_x != -360:
            self.goto(new_x, self.ycor())
            break

    def right(self):
        new_y = self.xcor() + 20
        while new_y != 360:
            self.goto(new_y, self.ycor())
            break

