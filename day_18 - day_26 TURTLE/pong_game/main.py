import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((370, 0))
left_paddle = Paddle((-370, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")


def detect_paddle_collision():
    pass


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move_ball()

    is_collide, paddle_scored = ball.detect_wall_collision()

    if is_collide:
        ball.update_ball()
        score_board.update_score(paddle_scored)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball()

    if (ball.xcor() > - 340 and left_paddle.distance(ball) < 50
            or ball.xcor() > 340 and right_paddle.distance(ball) < 50):
        ball.bounce_ball()

screen.exitonclick()
