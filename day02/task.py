#計算機の作成
#チップも含めて一人当たりいくら払うか
#小数点第2位で四捨五入

# print("Welcome to the tip calculator.")
# bill = input("What was total bill? $")
# tip = input("How much tip would you like to give? 10,12 or 15?")
# people = input("How many people to split the bill?")
# pay = (float(bill) * (int(tip) / 100 + 1) / int(people))
# print(f"Each person should pay: ${round(pay, 2)}")

#$を表示させて、追加で入力させないようにする。
#同じように、10、12と、％をか書かせないようにしている
#関数使って消す方法もある
#floatでも同じ結果だが、選んだ理由まで明確に

#intの位置を見直す

print("Welcome to the tip calculator.")
bill = float(input("What was total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
people = int(input("How many people to split the bill?"))
pay = ((bill * tip / 100 + bill) / people)
print(f"Each person should pay: ${round(pay, 2)}")
