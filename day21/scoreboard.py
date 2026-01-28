from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "italic")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def count(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()