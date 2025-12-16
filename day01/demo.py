# やったこと
# gitignoreへの入れ方

# 分かったこと
# 語尾に/nで改行はinput関数にも適用できる

# 詰まったこと
# input関数で質問文を改行したところに入力させること

#バンド名作成ツール
#ペットの名前と育った町に基づいて作成
#input関数において、入力すべき箇所を改行する

print("Welcome to the Band Name Generator.")
city_name = input("What is the name of the city you grew up in?\n")
# print(city_name)
pets_name = input("What is your pet's name?\n")
# print(pets_name)
print("your band name could be: " + city_name + " " + pets_name )
