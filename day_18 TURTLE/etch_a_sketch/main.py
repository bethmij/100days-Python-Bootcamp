from turtle import Turtle, Screen

timmy = Turtle()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_clockwise():
    timmy.right(5)


def move_anti_clockwise():
    timmy.left(5)


def clear_drawing():
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_clockwise, "d")
screen.onkey(move_anti_clockwise, "a")
screen.onkey(clear_drawing, "c")
screen.exitonclick()
