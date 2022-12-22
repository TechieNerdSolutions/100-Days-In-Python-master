from turtle import Turtle, Screen

tur = Turtle()
# Draw a Square Box
n = 4
while n > 0:
    tur.forward(50)
    tur.right(90)
    n -= 1

# Draw a Dashed Line
for _ in range(5):
    tur.forward(10)
    tur.penup()
    tur.forward(10)
    tur.pendown()

# All Angle diagrams
x = 3  # side of the diagram
angle = 60  # default angle of a closed figure(triangle)


def draw_figure(x):
    angler = 360 / x
    for _ in range(x):
        tur.forward(50)
        tur.right(angler)


while x <= 10:
    draw_figure(x)
    x += 1

Screen = Screen()
Screen.exitonclick()
