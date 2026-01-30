from turtle import Turtle

FONT = ("VT323", 50, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.update_score()
        self.l_player = "1P"
        self.r_player = "2P"


    def left_score_up(self):
        self.clear()
        self.left_score += 1
        self.update_score()

    def right_score_up(self):
        self.clear()
        self.right_score += 1
        self.update_score()

    def update_score(self):
        self.write(f"{self.left_score}   {self.right_score}", False, "center", FONT)

    def winner(self, player):
        self.goto(0, 0)
        self.write(f"{player} WIN!!", False, "center", FONT)

# mainでpaddle_choiceを指定しても、calssの中の大元の
# self.left_score = 0
# self.right_score = 0
# は変動しない。
"""    def score_up(self, paddle_choice):
        self.clear()
        paddle_choice += 1
        self.update_score()"""