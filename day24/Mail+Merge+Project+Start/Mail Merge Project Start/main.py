#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
#[]ごと置き換えることで、偶然nameがはいってしまう場合をのぞける。

#名前の読み取り
with open("C:Input/Names/invited_names.txt", "r") as n_data:
    # name = n_data.read() # 最後まで到達してしまう
    # readlines()でファイル内の行をリストに
    # strip()は文字列の最初と最後のスペースを削除
    name_list = n_data.readlines()
    new_list = [names.strip() for names in name_list]#リスト内包表記
    """    
    new_list = []
    for _ in name_list:
        new_name = _.strip()
        new_list.append(new_name)
    """

# 手紙の読み取り
with open("C:Input/Letters/starting_letter.txt", "r") as l_data:
    letter = l_data.read()

# listから各人の手紙を作成
for name in new_list:
    with open(f"C:Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        letters = letter.replace(PLACEHOLDER, name)
        file.write(letters)

