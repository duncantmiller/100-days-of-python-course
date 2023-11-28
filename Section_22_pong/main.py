"""pong"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Field Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
right_score = Scoreboard("right")
left_score = Scoreboard("left")

ball.serve_right()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

is_game_on = True
while is_game_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

    if ball.ycor() > 300:
        ball.bounce_down()
    elif ball.ycor() < -300:
        ball.bounce_up()

    if ball.xcor() > 400:
        right_score.increment_points()
        ball.serve_left()
    elif ball.xcor() < -400:
        left_score.increment_points()
        ball.serve_right()

screen.exitonclick()
