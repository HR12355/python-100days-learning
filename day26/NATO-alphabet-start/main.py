import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {value.letter: value.code for (key,value) in data.iterrows()}
print(new_dict)

def generate_phonetic():
    user_inputs = input("Enter a word: ").upper()
    try:
        phonetic_code = [new_dict[key] for key in user_inputs]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic() # 関数内でもう一度関数を呼び出す
    else:
        print(phonetic_code)

generate_phonetic()