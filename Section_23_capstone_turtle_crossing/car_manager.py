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

    def generate_cars(self):
        """create a row of cars"""
        for y_coordinate in range(-220, 250, 15):
            if random.choice([1, 2, 3]) == 1:
                car = Turtle()
                car.shape("square")
                car.color(random.choice(COLORS))
                car.penup()
                car.setpos(280, y_coordinate)
                self.cars.append(car)

    def move_cars(self):
        """move all the cars"""
        for car in self.cars:
            car.setx(car.xcor() - self.move_distance)
