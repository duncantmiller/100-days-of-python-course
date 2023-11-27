# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb)

# print(rgb_colors)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

"""turtle graphics"""
import turtle as t
import random

mertle = t.Turtle()
screen = t.Screen()
t.colormode(255)
t.hideturtle()

def move_up_one_row():
    """move to the starting column up one row"""
    mertle.penup()
    mertle.backward(500)
    mertle.left(90)
    mertle.forward(50)
    mertle.right(90)

def draw_painting():
    """Draw a series of dots 10x10"""
    for _ in range(10):
        for _ in range(10):
            color = random.choice(color_list)
            mertle.pencolor(color)
            mertle.dot(20)
            mertle.penup()
            mertle.forward(50)
        move_up_one_row()

mertle.speed(0)
draw_painting()
screen.exitonclick()
