import random
from turtle import Turtle


class Car:

    def __init__(self):
        super().__init__()
        self.moving_speed = 0.3
        self.car_list = []
        self.position = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(color)
            random_y = random.randint(-250, 250)
            position_cor = (350, random_y)
            car.setheading(180)
            car.goto(350, random_y)
            self.car_list.append(car)
            self.position.append(position_cor)

    def move_cars(self):
        for car in self.car_list:
            car.forward(10)

    def update_car_speed(self):
        self.moving_speed *= 0.8



