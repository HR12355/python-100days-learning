# =====================
# Day07 学習メモ
# ======================
# やったこと
# 単語当てゲーム　hangman

# 分かったこと

# 詰まったこと
# for 【取り出したものの名前】 in 【データの塊】:
#     【ものを使ってやりたいこと】
# ======================

#Step 1
import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_display = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_display)
print(chosen_word)

display = ""
for count in range(len(chosen_word)):
    display += "_"
# display = "_" * len(chosen_word)
print(display)


"""
display2 = ""
while chosen_word != display2:
    guess = input("Please enter one letter of the alphabet.\n").lower()
    for letter in chosen_word:
        if letter == guess:
            # print("Correct")
            display2 += guess
            display.append(guess)
        elif letter in display:
            display2 += letter
        else:
            # print("Incorrect")
            display2 += "_"
    print(display2)
"""

display3 = []
for count in range(len(chosen_word)):
    display3 += "_"
# print(display3)


lives = 6
# before_count = display3.count("_") #【数えたいリスト】.count(【探したいもの】)
game_over = False
while not game_over: #not False はTrue　なので、ループ実行。
    guess = input("Please enter one letter of the alphabet.\n").lower()
    point = 0
    for num in range(len(chosen_word)): #range(5) = 0,1,2,3,4
        letter = chosen_word[num]
        if letter == guess:          #一致
            display3[num] = guess
            point += 1
        else:
            if display3[num] == "_": #不一致の時、リストが空白
                display3[num] = "_"
            else:                    #不一致の時、リストに何か入っている。
                pass
    # if point == 0:  #pointを作ったけど、下の方がスマート
    #     lives -= 1
    if guess not in chosen_word:
        lives -= 1

    # print(point)
    # print(lives)
    print(stages[lives])
    print("".join(display3))


    if "".join(display3) == chosen_word:
        game_over = True
        print("clear")

    if lives == 0:
        game_over = True
        print("Game Over")

