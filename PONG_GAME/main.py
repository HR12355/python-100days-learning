# =====================
# Day22 学習メモ
# ======================
# やったこと
# PONG game
# 分かったこと
# mainとclassの書き分けを理解。この動作をしたときに、ballをどう動かすか。の順序で考える
# 教訓：恐怖心について　何を恐れているか明確にする
# 詰まったこと
# 亀を二つ作るのに、引数positionで作れるようにすること。
# ======================
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


START_LEFT_POSITION = (-410, 0)
START_RIGHT_POSITION = (410, 0)

screen = Screen()
screen.setup(900, 700)
screen.bgcolor("black")
screen.title("MY_PONG")
screen.tracer(0)

paddle_left = Paddle(START_LEFT_POSITION)
paddle_right = Paddle(START_RIGHT_POSITION)

screen.listen()
screen.onkey(paddle_left.left_up, "w")
screen.onkey(paddle_left.left_down, "s")
screen.onkey(paddle_right.right_up, "Up")
screen.onkey(paddle_right.right_down, "Down")

ball = Ball()
score = Score()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()


    ball.move()
    # 上下の壁に衝突
    if ball.ycor() > 330 or ball.ycor() < -320:
        ball.bounce_y()

    # パドルに衝突
    if ball.xcor() < -390 and paddle_left.distance(ball) < 50 or ball.xcor() > 390 and paddle_right.distance(ball) < 50:
        ball.bounce_x()
        ball.move_speed *= 0.6

    # 左右の壁に衝突　ボールをリセット、点数増加
    if ball.xcor() < -440:
        ball.restart()
        score.right_score_up()

    if ball.xcor() > 430:
        ball.restart()
        score.left_score_up()

    if score.left_score == 5:
        score.winner(score.l_player)
        game_is_on = False

    if score.right_score == 5:
        score.winner(score.r_player)
        game_is_on = False




screen.exitonclick()