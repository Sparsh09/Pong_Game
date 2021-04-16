from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()

        self.goto(-100, 200)
        self.write(self.l_score, align="Center", font=("Courier", 80, "normal"))

        self.goto(100, 200)
        self.write(self.r_score, align="Center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.updatescoreboard()

    def r_point(self):
        self.r_score += 1
        self.updatescoreboard()

    def winner(self, winner):
        print(winner)
        self.goto(0,0)
        self.write(f"{winner} Wins", align="Center", font=("Courier", 60, "normal"))
