# =====================
# Day17 学習メモ
# ======================
# やったこと
# class作成
# クイズゲーム
# 分かったこと
# pass
# Constructor　コンストラクタについて
# class Car:
#     def __init__(self):
        #initialise attributes(属性を初期化)
# データ指向オブジェクトを使うことで、dataの中身（今回は問題文）が変わっても
# コードをあまり書き直さなくていいということ
# 詰まったこと
# 上から順にコードを考えてしまうこと。別の見方も考える回数を増やす。
# ======================

class User:
    # 属性の追加の仕方
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0 #初期設定
        self.following = 0

    # メソッドの追加の仕方
    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "ken")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_2.followers)


