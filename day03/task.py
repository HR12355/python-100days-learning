# ピザ宅配プログラム
# 請求書を出す。

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S , M , L: ")


bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please enter S, M, or L")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" and size == "S": #andを調べて持ってきた、下記に別の方法
    bill += 2
if pepperoni == "Y" and size == "M":
    bill += 3
if pepperoni == "Y" and size == "L":
    bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

# 条件文において　かつand またはor　を使わない方法。
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# 論理演算子　and,or,not