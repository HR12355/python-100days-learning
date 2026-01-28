# =====================
# Day21 学習メモ
# ======================
# やったこと
# 蛇ゲームの続き
# クラス継承
# スライシング リストをスライスして取得。ex: piano_keys[2:5] リストの2，3，4番目をとる。中身がタプルと似てる
# 分かったこと
# super().で継承する
# 詰まったこと

# ======================
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # アニメーションをoffにする。

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    #食べ物とぶつかった時
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.count()

    #壁とぶつかった時
    if 285 < snake.head.xcor() or snake.head.xcor() < -285 or 285 < snake.head.ycor() or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

    #尻尾とぶつかった時
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:#distanceの引数にturtleも入れられる
    #         game_is_on = False
    #         scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:#distanceの引数にturtleも入れられる
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()