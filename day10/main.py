# =====================
# Day10 学習メモ
# ======================
# やったこと
# 関数の入力、出力
# Docstrings
# 電卓アプリ

# 分かったこと
# return文で戻り値を返す。関数の定義（今回は）の外で使うためのもの
#   printが出力と紛らわしいので、戻り値という
#   returnはその行で関数が終わる。
#   欲しい結果がこない時にアーリーリターン使って、定義を終わらせる。
# """で囲うのは本来は関数の説明書として使うべきもの。関数の定義のすぐ下に書く。

# 詰まったこと
# 辞書の中に関数を定義すること
#   "+": add　#addの後ろにカッコを書かずに定義すればよい。
#   print(functions["+"](3,4))　
# 計算機で、重複しているところを、while文で繰り返す
# ======================
"""
def format_name():
    f_name = input("What is your first name?\n").capitalize()
    l_name = input("What is your last name?\n").capitalize()
    result =  f_name + " " + l_name
    print(result)
format_name()
print(format_name()) #resultはdef定義の外では使えないため、noneが帰ってくる。
"""

def form_name(f_name, l_name):
    """コンテナ内の名前について頭文字を大文字にして表示して返す"""
    if f_name == "" or l_name == "":
        return "うまくいってないよ" #アーリーリターンでここで処理を終わらせる。
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    return f_name + " " + l_name #いつも変数に入れていたところをreturnにすればいい。
print(form_name(input("What is your first name?"), input("What is your last name?")))

print(len("format"))

