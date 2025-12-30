import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))



# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

def encrypt(original_text, shift_amount):
    box = []
    shift_amount %= len(alphabet)
    for number in range(len(original_text)):
        result = alphabet.index(original_text[number])
        # print(result)
        if result + shift_amount <= 25:
            letter = alphabet[result + shift_amount]
        else:
            letter = alphabet[result + shift_amount - 26]
        box.append(letter)
    print(f"Here your encode result: {"".join(box)}")

# encrypt(original_text = text, shift_amount = shift)

# リスト化しなくても可能　講座
"""
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet) 再定義必要ないため、良い
        cipher_text += alphabet[shifted_position]
        print(cipher_text)
    print(f"Here is the encoded result: {cipher_text}")


encrypt(original_text=text, shift_amount=shift)
"""

def decrypt(original_text, shift_amount):
    output_text = ""
    shift_amount %= len(alphabet)
    for letter in original_text:
        position = alphabet.index(letter) - shift_amount
        output_text += alphabet[position]
    print(f"Here your decoded result: {output_text}")

# decrypt(original_text=text, shift_amount=shift)

# 一つだけで完結するように作るので、あってるけど違う
"""
def caesar(original_text, shift_amount):
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        pass

caesar(text, shift)
"""


def caesar(original_text, shift_amount, direction_point):
    output_text = ""
    if direction_point == 'decode':
        shift_amount *= -1
    for letter in original_text:


        if letter not in alphabet:
            output_text += letter
        else:
            position = alphabet.index(letter) + shift_amount
            position %= len(alphabet)
            output_text += alphabet[position]
    print(f"Here your {direction_point}d result: {output_text}")

# caesar(text, shift, direction)


# question = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
# if question == 'no':
#     stop_caesar = False
#     print("This concludes it.")
# else:
stop_caesar = True
while stop_caesar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    question = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if question == 'no':
        stop_caesar = False
    else:
        pass
print("This concludes it.")




