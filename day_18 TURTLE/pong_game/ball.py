from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.angle = 30

    def move_ball(self):
        self.penup()
        self.setheading(self.angle)
        self.forward(10)

    def detect_wall_collision(self):
        if self.xcor() > 390 or self.xcor() < -390:
            return False
        return True

    def bounce_ball(self):
        self.angle += 90
