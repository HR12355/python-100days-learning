from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    DF = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    DF = pandas.read_csv("data/french_words.csv")

CURRENT_NUM = 0
def change_card():
    global CURRENT_NUM
    root.after_cancel(root.after(3000, change_window))
    canvas.itemconfig(canvas_image, image=my_img)
    CURRENT_NUM = random.randint(0, len(DF) - 1)
    random_word = DF.at[CURRENT_NUM, "French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word, fill="black")
    root.after(3000, change_window)


def change_window():
    global CURRENT_NUM
    canvas.itemconfig(canvas_image, image=my_img2)
    random_word_en = DF.at[CURRENT_NUM, "English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word_en, fill="white")

def removed_word():
    global DF, CURRENT_NUM

    DF = DF.drop(index=CURRENT_NUM).reset_index(drop=True)
    print(len(DF))
    DF.to_csv("data/words_to_learn.csv", index=False)


# window
root = Tk()
root.title("Flash Card")
root.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(root, width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
my_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 265, image=my_img)
canvas.grid(column=0, row=0, columnspan=2)

# change picture
my_img2 = PhotoImage(file="images/card_back.png")

# text
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))# tagなしで変数でも可能
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), tags="French_text") # タグあり

# button
cross_mark_img = PhotoImage(file="images/wrong.png")
cross_button=Button(root, image=cross_mark_img, highlightthickness=0, command=change_card)
cross_button.grid(column=0, row=1)

check_mark_img = PhotoImage(file="images/right.png")
check_button=Button(root, image=check_mark_img, highlightthickness=0, command=lambda:[removed_word(), change_card()])
check_button.grid(column=1, row=1)








change_card()

root.mainloop()