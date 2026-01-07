# =====================
# Day11 学習メモ
# ======================
# やったこと
# ブラックジャック

# 分かったこと
# 大きな問題は小さな問題に分解する
# if文は上から下に実行されるのを利用して、条件を考えていた
# 0はブラックジャックで、ほかの数より小さいけど、先に書けば問題ない
# 11に1を代入したけど、remove関数で11をリスト内から取り除けた
# 思ったより自分で書けてうれしい。難易度もエキスパートでヒント見ずにできた！

# 詰まったこと
# どこまでを関数にすべきか迷った。重複でいい
# 自分のコードがみにくい
# 弱い警告でも、無視せずに消すこと。
# 関数の引数をつかって、ほかにも使えるようにできた。32行目change11とその下比べる。
# ======================
# ブラックジャック
# ルール：J,Q,Kは10とする。Aは1or11とする。
# ディーラーが17点まで引くというルール忘れていた。
# →while文の条件を　total_c < 17
# 代わりに、負けてたら引くようにしたけど、公平性に欠けるため、17を適用
import random
import art
# cards = ["11", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = {"A":11, "two":2} Aの変更に使うと思う 3, 4, 5, 6, 7, 8, 9, 10, 10, 10

#添削みてつくった。関数の有効な使い方だと思った。
def change11(bj_player):
    if 11 in bj_player and sum(bj_player) > 21:
        a_po2 = bj_player.index(11)
        bj_player[a_po2] = 1

#上のchange11の関数使えば不要やけど、比較のためにおいておく。
def draw_card():
    player.append(random.choice(cards))
    if 11 in player and sum(player) > 21:
        position1 = player.index(11)
        player[position1] = 1
    computer.append(random.choice(cards))
    if 11 in computer and sum(computer) > 21:
        a_po2 = computer.index(11)
        computer[a_po2] = 1

def total_score():
    total_player = sum(player)
    # total_c = sum(computer)
    return f"あなた：{player} 合計：{total_player}\nCPU：{computer[0]}"



# restart = input("ブラックジャックをプレイしますか？はい：y　いいえ：n\n").lower()
BJ = True
while BJ:
    restart = input("ブラックジャックをプレイしますか？はい：y　いいえ：n\n").lower()
    if restart == "n":
        print("ゲームを終了します")
        break
    print(art.logo)
    player = []
    computer = []
    for play in range(2):
        player.append(random.choice(cards))
        computer.append(random.choice(cards))

    # if 11 in player and sum(player) > 21:
    #     ace_po1 = player.index(11)
    #     player[ace_po1] = 1
    # if 11 in computer and sum(computer) > 21:
    #     ace_po2 = computer.index(11)
    #     computer[ace_po2] = 1
    change11(player)
    change11(computer)
    print(total_score())

    draw_loop = True
    while draw_loop:
        draw = input("もう一枚カードを引きますか？はい：y いいえ：n\n").lower()
        if draw == "y":
            draw_card()
            print(total_score())
            if sum(player) > 21:
                draw_loop = False
        else:
            draw_loop = False

    total_p = sum(player)
    total_c = sum(computer)
    #CPUが負けているとき→17以上になるまで引く
    # while total_c < total_p:
    while total_c < 17:
        computer.append(random.choice(cards))
        total_c = sum(computer)
        if 11 in computer and sum(computer) > 21:
            a_po1 = computer.index(11)
            computer[a_po1] = 1
        # if sum(computer) >= sum(player):
        #     break

    print("---結果---")
    print(f"あなた：{player} 合計：{total_p}\nCPU：{computer} 合計：{total_c}")
    if 21 >= total_p > total_c:
        print("あなたの勝ち！")
    elif total_c > 21 >= total_p:
        print("あなたの勝ち！")
    elif total_p == total_c:
        print("引き分け")
    else:
        print("あなたの負け")



