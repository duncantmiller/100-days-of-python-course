"""pong"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
# from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Field Pong")
screen.tracer(0)

# scoreboard = Scoreboard()

paddle = Paddle()
ball = Ball()

ball.set_serve_heading()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

is_game_on = True
while is_game_on:
    ball.move()
    screen.update()
    time.sleep(0.2)

screen.exitonclick()
