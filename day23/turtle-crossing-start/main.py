import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

START_COUNT = 20
FONT_GAME_OVER = ("Arial Black", 28, "bold")

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)#アニメーション停止

#game overの出力
turtle = Turtle()
turtle.hideturtle()
def game_over():
    turtle.write("Game Over", False, "center", FONT_GAME_OVER)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()

counter = 0 #hint
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()

    # 車を一定間隔で出現させる
    counter += 1
    if counter > START_COUNT:# 0.1 * 20 = 2s
        car.create_car()
        counter = 0

    # 亀のゴール地点
    if player.ycor() >= 290.0:
        player.restart()
        car.car_speed += 5
        START_COUNT *= 0.7
        scoreboard.level_up()

    # 車との衝突
    for car_item in car.cars:
        x_distance = abs(car_item.xcor() - player.xcor())
        y_distance = abs(car_item.ycor() - player.ycor())
        if x_distance < 28 and y_distance < 18:
            game_is_on = False
            game_over()
            # scoreboard.test()


screen.exitonclick()#ループの外に書く
