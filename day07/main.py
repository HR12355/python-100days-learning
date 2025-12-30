# =====================
# Day07 学習メモ
# ======================
# やったこと
# 単語当てゲーム　hangman
# UXについて
# import文

# 分かったこと
# import文
#   import hangman_words
# 　　hangman_words.word_list
# 　from {module} import {class/function}内容が少ないとき便利
#    from hangman_words inport word_list , logo


# 詰まったこと
# for 【取り出したものの名前】 in 【データの塊】:
#     【ものを使ってやりたいこと】
# ======================

#Step 1
import random
import hangman_words
#from hangman_words inport word_list ファイルの中が少ないときより軽くできる。
import hangman_art

print(hangman_art.logo)

# word_display = ["aardvark", "baboon", "camel"]
word_display = hangman_words.word_list
chosen_word = random.choice(word_display)
print(chosen_word)

display = ""
for count in range(len(chosen_word)):
    display += "_"
# display = "_" * len(chosen_word)
print(display)

display3 = []
for count in range(len(chosen_word)):
    display3 += "_"
# print(display3)

lives = 6
guess_words = []
# before_count = display3.count("_") #【数えたいリスト】.count(【探したいもの】)
game_over = False

while not game_over: #not False はTrue　なので、ループ実行。
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Please enter one letter of the alphabet.\n").lower()
    guess_words.append(guess)
    # point = 0
    for num in range(len(chosen_word)): #range(5) = 0,1,2,3,4
        letter = chosen_word[num]
        if letter == guess:          #一致
            display3[num] = guess
            # point += 1
        else:
            if display3[num] == "_": #不一致の時、リストが空白
                display3[num] = "_"
            else:                    #不一致の時、リストに何か入っている。
                pass
    # if point == 0:  #pointを作ったけど、下がスマート
    #     lives -= 1
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")


    count_guess = guess_words.count(guess)
    if count_guess >= 2:            #既に推測したものの表示
        print(f"You guessed the word : {guess}")


    # print(point)
    # print(lives)
    print(hangman_art.stages[lives])
    print("".join(display3))


    if "".join(display3) == chosen_word:
        game_over = True
        print("clear")

    if lives == 0:
        game_over = True
        print("Game Over")

