import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((370, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

screen.exitonclick()
