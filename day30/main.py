# =====================
# Day30 学習メモ
# ======================
# やったこと
# エラー、例外、JSONデータ
# JavaScriptObjectNotation という、データの書き方のルール
# password managerのsearchボタン機能の追加

# 分かったこと
# try,exceptをセットで使う

# 詰まったこと
# try:の位置どこまで含めるのか　→エラーを引き起こすその一文のみでよい
# ======================
# 例外の拾い方
# FileNotFound
# try: # エラーが発生する可能性があるコード
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
#
# except FileNotFoundError: # エラーが発生した時の処理
#     print("error")
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist .")
#
# else:
#     context = file.read()
#     print(context)
# finally: # コードが成功していても失敗していても
#     file.close()
#     print("File was closed")
#     raise TypeError("This is an error that I made up.")

# 例外の生成
# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("身長が高すぎる")
#
# bmi = weight / height ** 2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
#
# def make_pie(index):
#     try: # defの中でtry
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass
    return total_likes


print(count_likes(facebook_posts))