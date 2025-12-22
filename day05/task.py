# パスワード作成
# イージーバージョン 順番に並べる
# ハードバージョン　ランダムで並べる

import random
# アルファベット（大文字）のリスト
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 数字のリスト
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 記号のリスト
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like?\n"))
number = int(input("How many numbers would you like?\n"))

# イージーバージョン
password = ""
# for count in range(symbol): 別の書き方↓
for count in range(1 , symbol + 1 ):
    choice_symbols = random.choice(symbols)
    password += choice_symbols
for count in range(number):
    choice_numbers = random.choice(numbers)
    password += choice_numbers
for count in range(letter - symbol - number):
    choice_letters = random.choice(letters)
    password += choice_letters
print(password)

# ハードバージョン　ランダムで並べる
next_password = list(password)
print(next_password)
random.shuffle(next_password) # next_passwordの中身を入れ替えてくれている。新しく代入する必要なし。
print(next_password)
# next = "".join(next_password)
#"".join()リストを文字列に変換する。
# print(f"your password is : {next}")
passw = ""
for count in next_password: #シャッフルで作ったリストをforでループ
    passw += count          #空白に一つずつ足していく
print(f"your password is : {passw}")





