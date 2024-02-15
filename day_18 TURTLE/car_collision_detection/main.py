from turtle import Screen
from timmy import Timmy

screen = Screen()
screen.setup(width=700, height=600)
screen.tracer(0)

timmy = Timmy()

screen.listen()
screen.onkey(timmy.move, "Up")

is_game_on = True
while is_game_on:
    screen.update()



screen.exitonclick()
