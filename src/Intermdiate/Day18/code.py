from turtle import Turtle, Screen

turtle_obj = Turtle()
angle = 360
turtle_obj.speed("fastest")
while angle > 0:
    turtle_obj.circle(100)
    turtle_obj.right(angle)
    angle -= 1

screen = Screen()
screen.exitonclick()
