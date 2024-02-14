from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')

    def move_ball(self):
        # is_move = True
        # for _ in range(10):
        self.penup()
        self.setheading(30)
        self.backward(10)

    def detect_wall_collision(self):
        if self.xcor() > 390 or self.xcor() < -390:
            return False
        else:
            return True
