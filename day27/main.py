# =====================
# Day27 学習メモ
# ======================
# やったこと
# Graphical User Interface = GUI
# Tkinter
# 関数の引数
# 分かったこと
# オブジェクト指向の考え方の練習
# pack,place,grid の三つを使い分ける。混ぜない
# configは上書き更新する

# 詰まったこと

# ======================
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
#　デフォルトで設定されているものがあるよという授業
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# pack,place,grid の三つを使い分ける。混ぜない
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)


my_label["text"] = "New Text"  # 辞書形式で上書き
my_label.config(text="New Text")  # コンフィグとして設定変更

# Button
def button_clicked():
    # print("I got clicked")
    new_text = input.get()# ボタンをクリックする時には、mainloopまで処理はおわっている。
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Click New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=15)
# input.pack()
print(input.get())
input.grid(column=3, row=2)


window.mainloop()# ボタンが押されるまで待機