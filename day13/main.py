# =====================
# Day13 学習メモ
# ======================
# やったこと
# デバッグ
# デバッガーの使い方
# try-expert

# 分かったこと
# デバッガーの使い方、赤丸
# 詰まったこと

# ======================
# バグの再現　バグが発生したりしなかったりする。
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# """dice_num = randint(1, 6)"""
# dice_num = randint(0, 5)
# print(dice_images[dice_num])

# try-except
# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("数字で入力してください")
#     age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# デバッガーの使い方


# import random
# import maths
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# print(is_leap(1999))
# print(is_leap(1900))

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizz_buzz(20)

