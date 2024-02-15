import random
from turtle import Turtle


class Car:

    def __init__(self):
        super().__init__()
        self.moving_speed = 0.3
        self.car_list = []
        self.position = []
        self.create_cars()
        for _ in range(15):
            self.create_cars()

    def create_cars(self):
        car = Turtle()
        car.penup()
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(color)
        random_x = random.randint(-100, 1000)
        random_y = random.randint(-250, 250)
        position_cor = (random_x, random_y)
        car.setheading(180)
        car.goto(random_x, random_y)
        self.car_list.append(car)
        self.position.append(position_cor)

    def move_cars(self):
        for car in self.car_list:
            car.forward(10)

    def update_car_speed(self):
        self.moving_speed *= 0.8

    # def reset_positions(self):
    #     for index, car in enumerate(self.car_list):
    #         if car.xcor() < -380.0:
    #             car.goto(self.position[index])

    def restart(self):
        for index, car in enumerate(self.car_list):
            car.clear()
            car.goto(self.position[index])
