from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.forward(100)
tim.right(90)

for _ in range(4):
    tim.forward(100)
    tim.left(90)
