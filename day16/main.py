# =====================
# Day16 学習メモ
# ======================
# やったこと
# OOP
# class object
# 分かったこと
# pipinstallでよかった。共通環境ではある。仮想環境は知っておくだけで。
# 仮にメニューを増やしたとしても、main2は触らなくても動くこと
# 詰まったこと
# selfの意味
# 他人のコードから、つなげていくこと。.menuなど、「.」の後を辿っていくとわかりやすい。

# ======================
# OOP = Object Oriented Programming オブジェクト指向プログラミング
# classは頭文字を大文字にする。パスカルケース
# car = CarBlueprint() : Object = Class
# car.speed : Object.Attribute(属性),speed = 10
# car.stop() : Object.Method,def stop() = ~~~
# パッケージを使ってほかの人が作ったコードを使える
"""
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")

for _ in range(4):
    timmy.forward(25)
    # timmy.right(90)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squitle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)