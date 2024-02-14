from turtle import Screen, Turtle

POSITION = [(370, 0), (-370, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

paddle = Turtle(shape='square')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.color('white')
paddle.goto(370, 0)


def move_paddle_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def move_paddle_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(move_paddle_up, "Up")
screen.onkey(move_paddle_down, "Down")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
