## =====================
# Day04 学習メモ
# ======================
# やったこと
# ランダムモジュール、リスト
# じゃんけんゲーム


# 分かったこと
# moduleとは、複雑な機能を簡単にし、別々に作業することに優れている部品
# 作ったモジュールを借りて使える
# import random　使われてなかったら、白くなる
#リストで使えるメソッドappendなどは覚える必要はない。
#楽しんでゲームやアプリを作ろうとすべきであること
# randintは"random integer"（ランダムな整数）の略称です

# 詰まったこと
# fruits[-1] = "Melons"　最後の項目に'代入'している
# ======================
# import random
# import my_module
# number = random.randint(1,10)
# print(number)
# print(my_module.favorite_number)
#
# random_number = random.random() #ランダムモジュールのランダム関数
# print(random_number)
# random_number10 = random.random() * 10
# print(random_number10)
# random_float = random.uniform(0,100)
# print(random_float)

# import random
# import my_module
# print(my_module.)
# import random
# # Selection = random.choice(['heads', 'tails']) #random.choiceランダムに一つの要素を選択
# # print(Selection)

#教えられたモノだけで↑と同じ処理をする。
import random
number = random.randint(0,1)
if number == 0:
    print("heads")
else:
    print("tails")

# リストはデータ構造のこと
states_of_america = ["Delaware", "Pennsylvania","Georgia"]
print(states_of_america[0])#リストを作るのに[]をつかったので、取り出すときも同じようにする。
print(states_of_america[-1])
states_of_america[1] = "pencilvania"
states_of_america.append("Angelalnd")
print(states_of_america)
#リストで使えるメソッドappendなどは覚える必要はない。
# 組み込み型pythonドキュメントで調べて、どんなことができるか確認しておくこと。

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# # fruits.append("Lemons")
# print(fruits)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1]) #[外側の角括弧で挟まれたリストの数字][左で選んだリストの中の数字]