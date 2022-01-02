from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.display_score()

    def display_score(self):
        self.goto(50, 230)
        self.write(self.r_score, align="center", font=('Arial', 35, 'normal'))
        self.goto(-50, 230)
        self.write(self.l_score, align="center", font=('Arial', 35, 'normal'))

    def update_right(self):
        self.r_score += 1
        self.clear()
        self.display_score()

    def update_left(self):
        self.l_score += 1
        self.clear()
        self.display_score()
