from turtle import Turtle

# START_LEFT_POSITION = (-410, 0)
# START_RIGHT_POSITION = (410, 0)
UP = 90
DOWN = 270



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(4, 1)
        self.color("white")
        self.penup()
        self.goto(position)


    def left_up(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() + 20)

    def left_down(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() - 20)

    def right_up(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() + 20)

    def right_down(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() - 20)





