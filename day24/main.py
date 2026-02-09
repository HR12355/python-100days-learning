# =====================
# Day24 学習メモ
# ======================
# やったこと
# ファイルシステムについて、読み込み、書き込み、閉じる
# 誕生日会のメッセージ
# snake gameの改善 day21
# スコアを別のファイルに自動保存

# 分かったこと
# 絶対pathと相対path
# その場で見つけた情報の活用方法や状況を素早く理解するために情報を得るための作業をすることの大切さ

# 詰まったこと
# openの書くタイミング→最初に並べていい

# 先生の教え　コードの最適解
# 時期尚早の最適化は大したことではない。自分のコードをできるだけ最適化しようとしないこと。
# 目指すべきは「読みやすさ」
# ======================

# ファイルの読み取り
with open(r"C:..\..\..\..\..\Desktop\my_file.txt") as file:
#r　Raw String（生の文字列）で\nとかも無視する
# C:..\..\..\..\..\Desktop\my_file.txt   相対path 今いるところからの移動
# C:\Users\自分のユーザー名\Desktop   絶対path　根幹から移動
    contents = file.read()
    print(contents)
    # file.close() # with で直接ファイルを管理しているため、このコードは不要：終われば閉じられる

# appendで文章の追加
with open("new_file.txt", mode="a") as file:
    file.write("\nNew text.")

# writeで書き込み
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")