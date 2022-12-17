"""The main page of the game"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(1)

pong = Paddle((0, -280))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(pong.left, "Left")
screen.onkey(pong.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    # Detect player paddle misses
    if ball.ycor() < -280:
        ball.reset_position()
        score.player_point()


    # Detect collision with wall




screen.exitonclick()

# xcor > 280 == Right side
# xcor < -280 == left side
# ycor > 280 == top side
# ycor < -280 == bottom
