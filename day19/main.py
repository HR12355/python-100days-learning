# =====================
# Day19 学習メモ
# ======================
# やったこと
# turtle graphics
# 高次関数
# 位置引数、キーワード引数
# 分かったこと
# モジュールのドキュメントを読むこと
# 詰まったこと

# ======================
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="亀レース", prompt="どの色の亀が勝つ？Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

for num in range(0, 6):
    kame = Turtle(shape="turtle")
    kame.color(colors[num])
    kame.penup()
    kame.goto(x=-230, y=-100 + (num * 40))
    all_turtle.append(kame)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"あなたの勝ち‼ 勝利した亀の色:{winning_color}")
            else:
                print(f"あなたの負け. 勝利した亀の色:{winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Etch A Sketch
"""def move():
    kame.forward(50)

def back():
    kame.backward(50)

def turn_l():
    new_head = kame.heading() + 10
    kame.setheading(new_head)

def turn_r():
    kame.right(10)

def clear():
    kame.reset()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=turn_l)
screen.onkey(key="d", fun=turn_r)
screen.onkey(key="c", fun=clear)"""





screen.listen()
# screen.onkey(key="space", fun=move)#引数なしの関数
screen.exitonclick()