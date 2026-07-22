from turtle import Turtle
import random

PLUS_MINUS = [1, -1]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = -10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # self.y_move = -10これだと、毎回数字を設定しないといけない
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self):
        self.x_move *= -1
        self.y_move *= random.choice(PLUS_MINUS)
        self.goto(0, 0)
        self.move_speed = 0.1




