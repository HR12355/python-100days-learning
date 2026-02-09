from turtle import Turtle

FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level()

    def level(self):
        self.write(f"LEVEL: {self.scoreboard}", False, "left", FONT)

    def level_up(self):
        self.scoreboard += 1
        self.clear()
        self.level()

    def test(self):#test用　別で亀を作らなくてもかけた。おそらくclear()のせいかも
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)