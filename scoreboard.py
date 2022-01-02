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
        self.goto(100, 230)
        self.write(f"P2: {self.r_score}", align="center", font=('Arial', 35, 'normal'))
        self.goto(-50, 230)
        self.write(f"P1: {self.l_score}", align="center", font=('Arial', 35, 'normal'))

    def update_right(self):
        self.r_score += 1
        self.clear()
        self.display_score()

    def update_left(self):
        self.l_score += 1
        self.clear()
        self.display_score()

    def get_l_score(self):
        return self.l_score
    
    def get_r_score(self):
        return self.r_score
    
    def game_over1(self):
        self.clear()
        self.write("Game Over. Player 1 wins", align="center", font=('Arial', 35, 'normal'))
    
    def game_over2(self):
        self.clear()
        self.write("Game Over. Player 2 wins", align="center", font=('Arial', 35, 'normal'))
