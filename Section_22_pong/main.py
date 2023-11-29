"""pong"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Simone Pong")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
right_score = Scoreboard("right")
left_score = Scoreboard("left")

ball.serve_right()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

def reset_positions():
    """calls paddle resets"""
    right_paddle.reset_paddle()
    left_paddle.reset_paddle()

def bounce_if_hits_side():
    """check if the ball is over the y edge and bounce"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

def score_right_if_cross_left_goal():
    """check if passed left goal"""
    if ball.xcor() < -380:
        right_score.increment_points()
        if right_score.score == 7:
            right_score.print_game_over()
        else:
            reset_positions()
            ball.serve_left()

def score_left_if_cross_right_goal():
    """check if passed right goal"""
    if ball.xcor() > 380:
        left_score.increment_points()
        if left_score.score == 7:
            left_score.print_game_over()
        else:
            reset_positions()
            ball.serve_right()

def check_for_winner():
    """check if there is a winner"""
    if left_score.score == 7 or right_score.score == 7:
        left_score.print_game_over()
        return False
    return True

def bounce_if_hits_right_paddle():
    """bounce if hits right paddle"""
    if ball.was_last_hit_left():
        for link in right_paddle.links:
            if link.distance(ball) < 15:
                ball.bounce_x()
                ball.set_last_hit("right")
                shrink_if_needed()
                break

def shrink_if_needed():
    """shrink paddles if hits multiple of 10"""
    if ball.hits != 0 and ball.hits % 10 == 0:
        left_paddle.shrink()
        right_paddle.shrink()

def bounce_if_hits_left_paddle():
    """bounce if hits left paddle"""
    if ball.was_last_hit_right():
        for link in left_paddle.links:
            if link.distance(ball) < 15:
                ball.bounce_x()
                ball.set_last_hit("left")
                shrink_if_needed()
                break

is_game_on = True
while is_game_on:
    ball.move()
    screen.update()

    bounce_if_hits_side()
    score_right_if_cross_left_goal()
    score_left_if_cross_right_goal()
    is_game_on = check_for_winner()
    bounce_if_hits_right_paddle()
    bounce_if_hits_left_paddle()

screen.exitonclick()
