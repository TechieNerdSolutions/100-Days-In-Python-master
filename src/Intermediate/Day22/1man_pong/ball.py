"""The Ball module"""
from turtle import Turtle


class Ball(Turtle):
    """The Ball Class"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """The ball move function"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if self.ycor() >= 295:
            self.y_move *= -1
        if self.xcor() >= 360 or self.xcor() <= -360:
            self.move_x()

    def move_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_x()
