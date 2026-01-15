# =====================
# Day15 学習メモ
# ======================
# やったこと
# コーヒーマシーンプログラム

# 分かったこと
# returnとprintを組み合わせると、returnがないときにNoneを返す
# 5時間はかかったが、関数にするのも、核の部分も自分で考えて作れた↓以外
# 詰まったこと
# if文に関数を書くと、その度に実行されてしまうため、変数に入れる
# 別の辞書をつくって同じキーにして、forで回す

# ======================
from data import MENU
from data import resources
def start():
    choice = input("何になさいますか？(espresso/latte/cappuccino): ").lower()
    return choice

def order(choice):
    # 別の辞書をつくって同じキーにする。
    if choice == "report":
        units = {"water": "ml", "milk": "ml", "coffee": "g", "money": "$"}
        for key, value in resources.items():
            unit = units[key]
            if key == "money":#$は前にする
                print(f"{key} {unit}{value}")
            else:
                print(f"{key} {value}{unit}")
        return False
    elif choice == "off":
        print("電源を切る")
        return True
    else:
        return resource_calc(choice)

def resource_calc(menu):
    for calc in MENU[menu]["ingredients"]:
        resources[calc] = resources[calc] - MENU[menu]["ingredients"][calc]
        # print(resources[navi])
    # return resources[navi]

def check():
    """材料余剰"""
    flag = 0
    for item in resources:
        if resources[item] < 0:
            print(f"{item}が不足しています。")
            flag -= 1
    return flag

def coin():
    coin1 = float(input(f"quarter: "))
    coin2 = float(input(f"dimes: "))
    coin3 = float(input(f"nickel: "))
    coin4 = float(input(f"pennies: "))
    return round((coin1 * 0.25) + (coin2 * 0.1) + (coin3 * 0.05) + (coin4 * 0.01), 3)
# print(coin())

def sales(drink, dollar):
    if MENU[drink]["cost"] > dollar:
        print("金額不足です。")
        return False
    else:
        resources["money"] = MENU[drink]["cost"]
        return None

coffee_order = True
while coffee_order:
    choice_drink = start()
    restart = order(choice_drink)
    if restart == False:#report
        continue
    elif restart:#off
        break
        # coffee_order = False
        # continue
    if check() < 0:
        continue
    else:
        amount = coin()#清算する

        print(amount)
        if sales(choice_drink, amount) == False:#金額不足
            # 減らした材料を元に戻す
            for navi in MENU[choice_drink]["ingredients"]:
                resources[navi] = resources[navi] + MENU[choice_drink]["ingredients"][navi]
            continue
        else:
            change = round(amount - MENU[choice_drink]["cost"], 3)
            print(f"お釣りは${change}になります。{choice_drink}をどうぞ")
