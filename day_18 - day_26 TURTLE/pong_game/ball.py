from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.angle = 30
        self.moving_speed = 0.1

    def move_ball(self):
        self.penup()
        self.setheading(self.angle)
        self.forward(10)

    def detect_wall_collision(self):
        if self.xcor() > 385:
            # return 'LEFT'
            return True, 'LEFT'
        elif self.xcor() < -390:
            # return 'RIGHT'
            return True, 'RIGHT'
        return False, None

    def bounce_ball(self):
        self.angle += 90
        self.moving_speed *= 0.9

    def update_ball(self):
        self.home()
        self.moving_speed = 0.1

