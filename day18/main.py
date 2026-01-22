# =====================
# Day18 学習メモ
# ======================
# やったこと
# turtleモジュール
# タプル
# 分かったこと
# (turtle)documentを参照する。覚える必要はない。
#　heroes等はpythonの標準ライブラリにないため、インストールが必要
# import turtle as t ※t : alias nameで簡略できる randomで試した
# 詰まったこと
# 仮想環境でモジュールをインストールすると、グローバル環境ではなく、特定のフォルダで道具が使える。
# 今は、グローバルにインストールしてる。gitにvenv/はいれない。重いから
# 仮想環境を作ることはできたが、実行する画面がvenvじゃなくて出来なかった。
# ======================
# import の方法
# 1. import turtle
# 2. from turtle import Turtle
# 2.2 from turtle import *　アスタリスクを使えば全てをインポートできる※どこからきてるか判別しづらい
# import turtle as t ※t : alias name
#
# import heroes #heroesはpythonの標準ライブラリにないため、インストールが必要
# print(heroes.gen())

#タプル
# タプルは石に刻むことであり、値を変更することはできない。不変
# my_tuple = (1, 3, 8)
# my_tuple[2] #8

from turtle import Turtle, Screen, colormode
import random as rd
kamezou = Turtle()
#draw a square
kamezou.pencolor("aquamarine2")
# for _ in range(4):
#     kamezou.forward(100)
#     kamezou.left(90)

#破線を書く
# for _ in range(10):
#     kamezou.forward(10)
#     kamezou.penup()
#     kamezou.forward(10)
#     kamezou.pendown()

#三角形、四角形...
"""
side_num = 3
while side_num < 10:
    for _ in range(side_num):
        kamezou.forward(100)
        kamezou.right(360 / side_num)
    side_num += 1
"""

# colors = ["light blue", "orange2", "LightPink1", "light green", "SlateGray1", "turquoise", "violet", "yellow1"]
# def draw_shape(side_num):
#     angle = 360 / side_num
#     for _ in range(side_num):
#         kamezou.forward(100)
#         kamezou.right(angle)
# for draw in range(3, 11):
#     kamezou.pencolor(random.choice(colors))
#     draw_shape(draw)

#ランダムに歩いて描画 Random Walk
#線を太く、描画スピードも早く
"""angle = [0, 90 , 180, 270]
kamezou.speed("fast")
for _ in range(100):
    kamezou.pensize(10)
    kamezou.forward(30)
    kamezou.right(rd.choice(angle))
    # kamezou.setheading(r.choice(angle)) rightだと今の向きから計算し複雑なため、こちらがスマート
    kamezou.color(rd.choice(colors))"""

# カラーをリストからではなく呼び出す
"""colormode(255)
def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    color_tuple  = (r, g, b)
    return color_tuple

angle = [0, 90 , 180, 270]
kamezou.speed("fast")
kamezou.pensize(10)
for _ in range(100):
    kamezou.color(random_color())
    kamezou.forward(30)
    kamezou.setheading(rd.choice(angle))"""

#円を何周も描く
colormode(255)
def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    color_tuple  = (r, g, b)
    return color_tuple

kamezou.speed("fastest")
def draw_circle(times):
    for _ in range(times):
        kamezou.color(random_color())
        kamezou.circle(100)
        kamezou.right(360/ times)

draw_circle(50)



screen = Screen()
screen.exitonclick()

