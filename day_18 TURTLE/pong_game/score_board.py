from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.left_score = 0
        self.right_score = 0
        self.update_score_board()

    def update_score(self, paddle_win):
        if paddle_win == 'LEFT':
            self.left_score += 1
        else:
            self.right_score += 1

        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.left_score}", align='center', font=('Arial', 40, 'normal'))
        self.goto(100, 220)
        self.write(f"{self.right_score}", align='center', font=('Arial', 40, 'normal'))