from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write("Score: "+ str(self.score), False,"center",("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", ("Arial", 20, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
