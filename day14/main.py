# =====================
# Day14 学習メモ
# ======================
# やったこと
# higher lower game
# 分かったこと
# from game_data import dataという書き方をすると、ファイルの名前を省略
# 詰まったこと
# どこまでを定義するのか

# ======================
from game_data import data #game_dataの中のdata
import art #art全体
import random

# A vs Bでフォロワー数の多い方、ランダム

lottery = []
def redraw():
    draw = True
    choice = ""
    while draw:
        choice = random.choice(data)
        if choice not in lottery:
            lottery.append(choice)
            draw = False
        elif lottery == data:#プールの中全部使い果たしたとき
            draw = False
    return choice

def counter(dictionary):
    """どちらのフォロワー数が多いか"""
    if dictionary[-1]["follower_count"] < dictionary[-2]["follower_count"]:
        return "A"
    elif dictionary[-1]["follower_count"] > dictionary[-2]["follower_count"]:
        return "B"
    return None


print(art.logo)
redraw()
game_over = True
score = 0
while game_over:
    print(f"A: {lottery[-1]["name"]}とは{lottery[-1]["description"]}であり、生まれは{lottery[-1]["country"]}である。")
    print(art.vs)
    redraw()
    print(f"B: {lottery[-1]["name"]}とは{lottery[-1]["description"]}であり、生まれは{lottery[-1]["country"]}である。")
    # print(counter(lottery))#確認専用
    two_options = input("フォロワー数が多いのは'A'or'B': ").upper()
    if counter(lottery) == two_options: #success
        print("\n" * 20)
        print(art.logo)
        score += 1
        print(f"正解!!連続{score}回成功中")
        # print(f"正解!!連続{len(lottery) - 1}回成功中")
        if len(lottery) == 50:
            print("おめでとう")
            game_over = False
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"ゲームオーバー 最大成功回数{score}回")
        # print(f"ゲームオーバー 最大成功回数{len(lottery) - 2}回")
        game_over = False




