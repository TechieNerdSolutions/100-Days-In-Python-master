"""Building a Turtle race game"""
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1000, height=800)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "gold", "black", "chartreuse", "deep sky blue"]

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color {colors}: ")
y_positions = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225, ]
all_turtles = []

# Create 10 turtles
for turtle_index in range(0, 10):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-460, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 460:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                win = screen.textinput(title="Hooray", prompt=f"You've won! The {winning_color} turtle is the winner")
                # print(f"You've won! The {winning_color} turtle is the winner")
            else:
                lost = screen.textinput(title="Oh", prompt=f"Sorry you lost! The {winning_color} turtle is the winner")
                # print(f"Sorry you lost! The {winning_color} turtle is the winner")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
