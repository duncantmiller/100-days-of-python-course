"""turtle graphics"""
import turtle as t

mertle = t.Turtle()
screen = t.Screen()

def move_up():
    mertle.setheading(90)
    mertle.forward(10)

def move_down():
    mertle.setheading(270)
    mertle.forward(10)

def move_right():
    mertle.setheading(0)
    mertle.forward(10)

def move_left():
    mertle.setheading(180)
    mertle.forward(10)

def clear():
    mertle.clear()
    mertle.penup()
    mertle.home()
    mertle.pendown()

screen.listen()
screen.onkey(fun=move_up, key="w")
screen.onkey(fun=move_down, key="s")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
