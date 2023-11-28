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

def reset_positions(right_paddle, left_paddle):
    """resets paddle positions"""
    right_paddle.reset_paddle("right")
    left_paddle.reset_paddle("left")

is_game_on = True
while is_game_on:
    ball.move()
    screen.update()

    for link in right_paddle.links:
        if link.distance(ball) < 15:
            ball.bounce_x()
    for link in left_paddle.links:
        if link.distance(ball) < 15:
            ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.xcor() > 380:
        right_score.increment_points()
        if right_score.score == 7:
            right_score.print_game_over()
            is_game_on = False
        else:
            reset_positions(right_paddle, left_paddle)
            ball.serve_left()
    elif ball.xcor() < -380:
        left_score.increment_points()
        if left_score.score == 7:
            left_score.print_game_over()
            is_game_on = False
        else:
            reset_positions(right_paddle, left_paddle)
            ball.serve_right()

screen.exitonclick()
