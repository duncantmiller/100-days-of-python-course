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

def reset_positions(right_paddle, left_paddle):
    """calls paddle resets"""
    right_paddle.reset_paddle()
    left_paddle.reset_paddle()

def bounce_if_hits_side(ball):
    """check if the ball is over the y edge and bounce"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

def score_right_if_cross_left_goal(ball, right_score, right_paddle, left_paddle):
    """check if passed left goal"""
    if ball.xcor() < -380:
        right_score.increment_points()
        if right_score.score == 7:
            right_score.print_game_over()
        else:
            reset_positions(right_paddle, left_paddle)
            ball.serve_left()

def score_left_if_cross_right_goal(ball, left_score, right_paddle, left_paddle):
    """check if passed right goal"""
    if ball.xcor() > 380:
        left_score.increment_points()
        if left_score.score == 7:
            left_score.print_game_over()
        else:
            reset_positions(right_paddle, left_paddle)
            ball.serve_right()

def check_for_winner(right_score, left_score):
    """check if there is a winner"""
    if left_score.score == 7 or right_score.score == 7:
        left_score.print_game_over()
        return False
    return True

def bounce_if_hits_right_paddle(ball, right_paddle, left_paddle):
    """bounce if hits right paddle"""
    if ball.was_last_hit_left():
        for link in right_paddle.links:
            if link.distance(ball) < 15:
                ball.bounce_x()
                ball.set_last_hit("right")
                shrink_if_needed(ball.hits, left_paddle, right_paddle)
                break

def shrink_if_needed(hits, left_paddle, right_paddle):
    """shrink paddles if hits multiple of 10"""
    if hits != 0 and hits % 10 == 0:
        left_paddle.shrink()
        right_paddle.shrink()

def bounce_if_hits_left_paddle(ball, right_paddle, left_paddle):
    """bounce if hits left paddle"""
    if ball.was_last_hit_right():
        for link in left_paddle.links:
            if link.distance(ball) < 15:
                ball.bounce_x()
                ball.set_last_hit("left")
                shrink_if_needed(ball.hits, left_paddle, right_paddle)
                break

is_game_on = True
while is_game_on:
    ball.move()
    screen.update()

    bounce_if_hits_side(ball)
    score_right_if_cross_left_goal(ball, right_score, right_paddle, left_paddle)
    score_left_if_cross_right_goal(ball, left_score, right_paddle, left_paddle)
    is_game_on = check_for_winner(right_score, left_score)
    bounce_if_hits_right_paddle(ball, right_paddle, left_paddle)
    bounce_if_hits_left_paddle(ball, right_paddle, left_paddle)

screen.exitonclick()
