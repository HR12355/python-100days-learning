# =====================
# Day08 学習メモ
# ======================
# やったこと
# 暗号プログラム
# 関数

# 分かったこと
# 大きな問題を小さな問題に分解し、小さな問題をさらに小さな問題に分解する。
# インデックス関数はリストの要素が何番目か判別できる
# リスト名.index(探したいもの)

# 詰まったこと

# ======================

def greet(name , location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# greet("ken" , "Osaka") 好きな書き方でいい。
greet(location = "Osaka", name = "Ken")

# 「Your Life in Weeks」
# 90歳まで生きると仮定した場合、あと何週間残されているか

def life_in_weeks(age):
    print(( 90 - age ) * 365 // 7)

# life_in_weeks(89)
"""
def calculate_love_score(name1 , name2):
    score_true = 0
    for count in range(len(name1)):
        if name1[count].lower() == "t":
            score_true += 1
        if list(name1[count]) == ["r"]:
            score_true += 1
        if list(name1[count]) == ["u"]:
            score_true += 1
        if list(name1[count]) == ["e"]:
            score_true += 1

    for count in range(len(name2)):
        if list(name2[count]) == ["t"]:
            score_true += 1
        if list(name2[count]) == ["r"]:
            score_true += 1
        if list(name2[count]) == ["u"]:
            score_true += 1
        if list(name2[count]) == ["e"]:
            score_true += 1

    print(score_true)
calculate_love_score(name1 = "Kanye West", name2 = "Kim Kardashian")
"""
# 2人の名前の相性をテスト
def calculate_love_score(name1 , name2):
    count_t = name1.count("t") + name2.count("t")
    count_r = name1.count("r") + name2.count("r")
    count_u = name1.count("u") + name2.count("u")
    count_e = name1.count("e") + name2.count("e")
    count_true = (count_t + count_r + count_u + count_e)

    count_l = name1.count("l") + name2.count("l")
    count_o = name1.count("o") + name2.count("o")
    count_v = name1.count("v") + name2.count("v")
    count_e = name1.count("e") + name2.count("e")
    count_love = count_l + count_o + count_v + count_e
    love_score = str(count_true) + str(count_love)
    print(love_score)

calculate_love_score(name1 = "Kanye West", name2 = "Kim Kardashian")

