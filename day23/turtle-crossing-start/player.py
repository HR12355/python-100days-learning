from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()#ここで自分はタートルなので、新たに作らなくてもいい。
        self.shape("turtle")
        self.color("darkgreen", "lime")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)


    def move(self):
        """前進する"""
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)



