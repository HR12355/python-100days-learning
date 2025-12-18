## =====================
# Day03 学習メモ
# ======================
# やったこと
# 条件文、if/else/elif、論理演算子
# 選択式アドベンチャーゲーム

# 分かったこと
# 細分化して考える
# ここでもスペーシングは大事
# SyntaxError,IndentationErrorなど
# 比較演算子　
# ==値が等しい =は代入　を意味する
#　!=ノットイコール
# モジュロ演算子　％余り
# ifを使うときはインデントの場所を意識する
# not 5==5 5と5は等しい　TrueのnotでFalse
#文字列に”や’を使いたい時は、別々に使えばよい。
#you're と、’で挟む必要がある時、\は次の文字をエスケープしてくれる。
# .lower()	小文字化 input("---").lower()
# .upper()	大文字化
#文字列の中でEnterをおすとその場所で改行できる。
# 詰まったこと

# ======================

# 奇数か偶数かの判定
# number = int(input("確認したい数字は？\n"))
# if number % 2 == 0:
#     print("偶数です。")
# else:
#     print("奇数です。")

#bmi計算機と判定結果
# BMIが18.5未満（18.5を含まない）の場合、「低体重」と表示する
# BMIが18.5以上（18.5を含む）かつ25未満（25を含まない）の場合、「標準体重」と表示する
# BMIが25以上（25を含む）の場合、「過体重」と表示する
# weight = int(input("体重は？\n"))
# height = int(input("身長は？\n"))
# BMI = weight / (height ** 2)
# print(BMI)

# bmiにおける判別
weight = 85
height = 1.85
bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
print(bmi)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")


# ジェットコースターの料金
print("ジェットコースターへようこそ")
height = int(input("身長は何cmですか？"))
bill = 0
if height >= 120:
    print("ジェットコースターに乗ることができます。")
    age = int(input("年齢は？"))
    if age <= 12:
        print("100円です。")
        bill = 100
    elif age <= 18:
        print("200円です。")
        bill = 200
    elif 45 <= age <= 55:
    # elif age >= 45 and age <= 55:
        print("無料です。")
    else:
        print("300円です。")
        bill = 300
    photo = input("1枚50円で写真を取りますか？はいならばy。いいえならばnと答えてください。")
    if photo == "y":
        bill += 50
    print(f"値段は{bill}円です。")
else:
    print("乗ることはできません。")
