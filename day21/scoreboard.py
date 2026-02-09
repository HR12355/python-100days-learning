from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "italic")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt", mode="r") as data:
            score_data = data.read()
            self.high_score = int(score_data)
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.write(f"SCORE: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)

    def count(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()