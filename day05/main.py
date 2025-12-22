## =====================
# Day05 学習メモ
# ======================
# やったこと
# パスワードジェネレーター
# forループ
# range関数　ループする数値の範囲を設定する

# 分かったこと
# range関数　for文と組み合わせて使う
# 目的のために、必要なものを細分化して考える必要がある。

# 詰まったこと

# ======================
student_scores = [150, 142, 185, 120 ,171, 184, 149]
# 最大値を探す
# A = max(student_scores)
# print(A)
Maximum = student_scores[0]
for score in student_scores:
    if Maximum <= score:
        Maximum = score
print(Maximum)

# range関数
number_sum = 0
for number in range(1, 101):
    number_sum += number
print(number_sum)

# 課題FizzBuzz
for total in range(1, 20):
    if total % 15 == 0:
        print("FizzBuzz")
    elif total % 3 == 0:
        print("Fizz")
    elif total % 5 == 0:
        print("Buzz")
    else:
        print(total)

# import random
# passcode = ""
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# for i in range(1 , 6):
#     char = random.choice(symbols)
#     passcode += char
#     print(passcode)

# A = "akdaaadk"
# lakd = list(A)
# print(lakd)