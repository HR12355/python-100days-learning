# =====================
# Day12 学習メモ
# ======================
# やったこと
# 数字あてプロジェクト
# スコープ
# 今の形は上から下に実行してるだけのコードにすぎない。関数をもっと活用する

# 分かったこと
# namespaceがどこにあるかを意識すること。
# 変数名を全て大文字にするのは、変更する予定のない変数という規則がある。

# 詰まったこと
# 関数の中の変数を外で使うこと
# かんすうを作るたびに、悩まされた。
# どこを関数にするかが難しい。
# 関数の引数をうまく使うこと。main2の14行目参照
# ======================
# スコープ　変数や関数がどこまで使えるか
# ローカルスコープ　関数の中
# グローバルスコープ　どこでも使える
# namespace名前空間 変数だけでなく、名前をあげたもの全ての箱

# 素数判定　アルゴリズム
# def is_prime(num):
#     if num <= 1:
#         return False
#     elif num == 2:
#         return True
#     for split_num in range(2, num):
#         if num % split_num == 0:
#             return False
#     else:
#         return True
#
# print(is_prime(75))
import art
import random
print(art.logo)

print("ようこそ数当てゲームへ\n1 ~ 100までの数字を推測してください")
difficulty = input("難易度選択 'easy' or 'hard': ").lower()

answer = random.randint(1, 100) #randintはa,bも含む
# print(answer)
times = 0
guess_clear = True
if difficulty == "easy":
    times = 10
elif difficulty == "hard":
    times = 5
else:
    guess_clear = False
    print("'easy' or 'hard'か選んで")

while guess_clear:
    guess_num = int(input(f"残り{times}回\n推測する数字を入力してください: "))
    if guess_num > answer:
        print("高すぎます")
    elif guess_num < answer:
        print("低すぎます")
    else:
        print("推測成功‼")
        guess_clear = False
    times -= 1
    if times <= 1:
        print("失敗しました")
        guess_clear = False