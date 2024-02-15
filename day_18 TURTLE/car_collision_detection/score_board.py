from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level : {self.level}", align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('Courier', 25, 'normal'))
