# =====================
# Day20 学習メモ
# ======================
# やったこと
# ヘビゲーム
# クラスでの整理
# 分かったこと
# screen.tracer(0) # アニメーションをoffにする。
# screen.update()  # 描いたものを一気に表示する
# time.sleep(0.1)  # プログラムを0.1sだけ休憩させる
# rangeの新しい使い方。range(start=2, stop=0, step=-1)セグメント引数はわかりやすくするため、pythonではうごかない
#定数はすべて大文字 (all caps)で書く
# 定数を書くことで、その数値を変えればよく、下のコードを変更することが不要。
# ＠暗記ではなく、しくみの理解
# 詰まったこと
# initの考え方　# snake = Snake()で呼び出すとinitが適用されるイメージ
# 何かを繰り返す動作はメソッドに入れてしまう
# self.head = self.segments[0]など、コードをみてわかるようにする。headなので、先頭かな。
# ======================
from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # アニメーションをoffにする。

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update() # 描いたものを一気に表示する
    time.sleep(0.1) # プログラムを0.1sだけ休憩させる

    snake.move()
















screen.exitonclick()