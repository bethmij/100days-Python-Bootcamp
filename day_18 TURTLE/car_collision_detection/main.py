import time
from turtle import Screen
from timmy import Timmy
from car import Car
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=700, height=600)
screen.tracer(0)

timmy = Timmy()
car = Car()
score_board = ScoreBoard()

screen.listen()
screen.onkey(timmy.move, "Up")

is_game_on = True
FINISH_LINE = 250

while is_game_on:
    screen.update()
    time.sleep(car.moving_speed)
    car.move_cars()
    # car.reset_positions()

    for cars in car.car_list:
        if cars.distance(timmy) < 20:
            score_board.game_over()
            is_game_on = False

    if timmy.ycor() > FINISH_LINE:
        score_board.update_level()
        timmy.update()
        car.restart()
        car.update_car_speed()
        print(car.moving_speed)

screen.exitonclick()
