# =====================
# Day09 学習メモ
# ======================
# やったこと
# 辞書、ネスティング(入れ子)
# サイレントオークションプログラム

# 分かったこと
# 辞書：{"key": "Value"}　中括弧
# リスト:[]　角括弧
# 辞書はkeyで識別、リストは番号で
# keyを取り出したい時はforが簡単

# 詰まったこと
# 辞書にappendは使えない
# ======================
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "France": ["paris", "lille", "dijon"]
}
# programming_dictionary["Bug"] = "sl;kffsfk"
print(programming_dictionary["Bug"])
# programming_dictionary[1] = 4
# print(programming_dictionary[1])
#辞書に追加したい場合
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# forでどういう動きをするか
for navi in programming_dictionary:
    print(navi)
    print(programming_dictionary[navi])

print(programming_dictionary["France"][1])

nested_list = ["A", "B", ["C", "D"]]
#Dを取り出す
print(nested_list[2][1])





