from tkinter import *
from tkinter import messagebox # サブモジュールらしい
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password) # 文字を挿入
    pyperclip.copy(password) # 自動でコピー
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website_data = website_entry.get()
    info_data = info_entry.get()
    pass_data = pass_entry.get()

    if len(website_data) == 0 or len(pass_data) == 0:
        messagebox.showwarning(title="oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"There are the details entered: \n"
                                                        f"Email: {info_data} \nPassword: {pass_data} \n"
                                                        f"Is it ok to save?")
        if is_ok:
            with open("save_password.txt", "a") as data:
                data.write(f"{website_data} | {info_data} | {pass_data} \n")
            data_clear()

def data_clear():
    website_entry.delete(0, END)
    pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

info_label = Label(text="Email/Username:")
info_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)



# entry
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


info_entry = Entry(width=51)
info_entry.grid(column=1, row=2, columnspan=2)
info_entry.insert(0, "ken@gmail.com")


pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)



# button
generate_pass_button = Button(text="Generate Password", bg="white", width=14, command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, bg="white", command=add_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()