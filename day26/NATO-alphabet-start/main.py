import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {value.letter: value.code for (key,value) in data.iterrows()}
user_inputs = input("Enter a word: ").upper()
phonetic_code = [new_dict[key] for key in user_inputs]
print(phonetic_code)