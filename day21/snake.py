from turtle import Turtle

#定数はすべて大文字 (all caps)
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

# 欲しい要素：三体のブロック、先頭のブロック、先頭以外は前のブロックに移動
class Snake:
    # snake = Snake()で呼び出すとinitが適用されるイメージ
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #コードを見て、先頭とすぐわかる


    def create_snake(self):
        """3体のブロック"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):#先頭以外は前のブロックに移動
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # 最後のセグメントが最後から二番目のセグメントの座標に移動
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


