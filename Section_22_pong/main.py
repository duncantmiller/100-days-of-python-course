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

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
right_score = Scoreboard("right")
left_score = Scoreboard("left")

ball.serve_right()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

is_game_on = True
while is_game_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

    if ball.xcor() > 330 and right_paddle.distance(ball) < 50:
        ball.bounce_left()
    if ball.xcor() < -330 and left_paddle.distance(ball) < 50:
        ball.bounce_right()

    if ball.ycor() > 280:
        ball.bounce_down()
    elif ball.ycor() < -280:
        ball.bounce_up()
    elif ball.xcor() > 380:
        right_score.increment_points()
        ball.serve_left()
    elif ball.xcor() < -380:
        left_score.increment_points()
        ball.serve_right()

screen.exitonclick()
