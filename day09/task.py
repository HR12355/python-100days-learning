# サイレントオークションプログラム
import art
print(art.logo)

print("Welcome to the secret auction program!")

dict_data = {}
auction = True
while auction:
    name_data = input("What is your name?: ")
    bid_data= input("What is your bid?: $")
    bidder_data = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    dict_data[name_data] = bid_data

    if bidder_data == "no":
        auction = False
        print("\n" * 20)
    elif bidder_data == "yes":
        print("\n" * 20)
    else:
        print("Due to an error, from the beginning.")

max_score = max(dict_data.values()) #辞書内の最大の値
#last_bidder = max(dict_data.keys()) #辞書内の”最大”のkey。ローマ字の順番で決めている
last_bidder = max(dict_data, key=dict_data.get) #辞書内の”最大の値”のkey
print(f"Bidder: {last_bidder}, Amount: ${max_score}")






