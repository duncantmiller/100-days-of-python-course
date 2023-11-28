"""import turtle and random"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """CarManager class"""

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.generate_cars()

    def add_row_of_cars(self):
        """randomly add rows of cars"""
        if random.choice(range(10)) == 1:
            self.generate_cars()

    def generate_cars(self):
        """create a row of cars"""
        for y_coordinate in range(-220, 250, 20):
            if random.choice(range(8)) == 1:
                car = Turtle()
                car.shape("square")
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.color(random.choice(COLORS))
                car.penup()
                car.setpos(280, y_coordinate)
                self.cars.append(car)

    def move_cars(self):
        """move all the cars"""
        for car in self.cars:
            car.setx(car.xcor() - self.move_distance)
