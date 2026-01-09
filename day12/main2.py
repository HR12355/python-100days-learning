# 関数にすることを習慣づける
# 部分的なチェックができない。
# 再利用できない。
# 中身が見えづらい。
# 今の形は上から下に実行してるだけのコードにすぎない。

import art
import random

# グローバル変数
EASY_TURN = 10
HARD_TURN = 5

def guess_number(player_guess, num_answer, times):
    """数字の大小判別"""
    if player_guess > num_answer:
        print("高すぎます")
        return times - 1
    elif player_guess < num_answer:
        print("低すぎます")
        return times - 1
    else:
        print("推測成功‼")
# モード選択
def set_difficulty():
    choice_flag = input("難易度選択 'easy' or 'hard': ").lower()
    if choice_flag == "easy":
        return EASY_TURN
    else:
        return HARD_TURN
def game():
    print(art.logo)
    print("ようこそ数当てゲームへ\n1 ~ 100までの数字を推測してください")
    answer = random.randint(1, 100) #randintはa,bも含む
    print(answer)
    # choice_flag = input( 難易度選択 'easy' or 'hard': ").lower()
    times = set_difficulty()
    guess_num = 0
    while guess_num != answer:
        guess_num = int(input(f"残り{times}回\n推測する数字を入力してください: "))
        times = guess_number(guess_num, answer, times)
        if times == 0:
            print(f"失敗しました:答え{answer}")
            return
        elif guess_num != answer:
            print("もう一度推測を始める")

game()