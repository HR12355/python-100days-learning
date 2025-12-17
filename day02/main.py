## =====================
# Day02 学習メモ
# ======================
# やったこと
# データ型、数値、演算、型変換、ｆ文字列
# チップ計算機

# 分かったこと
#

# 詰まったこと
#booleanは大文字　True　False
#エラーの文章を理解
#input関数で受け取ったデータはstrとして扱われる。
#関数を定義する段階で、intなどを定義しておく必要がある
# ======================

print("hello"[4])
print("hello"[-1])

#常に０から数え始める
#str 文字列　　strings
#int　整数  integer
#float 浮動小数点
#boolean True or False

street_name = "Abbey Road"
print(street_name[4] + street_name[7])
#スペースを数えることを忘れない

print(len("name"))
#特定の関数に入るデータ型は決まっている
print(type(False))
print(type(123))
print(type(123.32))
print(type("False"))

# print("Number of letters in your name: " + str(len(input("Enter your name"))))

print(6//3) #切り捨て
print(6/3) #float

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height ** 2
print(bmi)
print(int(bmi))
print(round(bmi)) #四捨五入
print(round(bmi, 2))

score = 0
# score = score + 1
score += 1

#f文字列　様々なタイプが混同して使える
print(f"あなたのスコアは{score}です。身長は{height}。")


