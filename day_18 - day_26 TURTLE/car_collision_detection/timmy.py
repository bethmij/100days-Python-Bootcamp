from turtle import Turtle, Screen


class Timmy(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(10)

    def update(self):
        self.goto(0, -280)
