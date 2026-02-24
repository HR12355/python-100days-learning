from tkinter import *
from tkinter import messagebox # サブモジュールらしい
from random import choice, randint, shuffle
import pyperclip
import json
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
    new_data = {
        website_data: {
            "email": info_data,
            "password": pass_data
        }
    }

    if len(website_data) == 0 or len(pass_data) == 0:
        messagebox.showwarning(title="oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("save_password.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                data = json.load(data_file) # 古いデータの読み込み
        except FileNotFoundError:
            with open("save_password.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data) # 古いデータの更新

            with open("save_password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # 更新されたデータの保存
        finally:
            data_clear()

def data_clear():
    website_entry.delete(0, END)
    pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_search = website_entry.get()
    try:
        with open("save_password.json", "r") as data_file:
            data_search = json.load(data_file)

        messagebox.showinfo(website_search, f"Email: {data_search[website_search]['email']}\n"
                                        f"Password: {data_search[website_search]['password']}")
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found!")
    except KeyError:
        messagebox.showerror("Error", "No details for the website exists!")
    finally:
        website_entry.delete(0, END)

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
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
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

search_button = Button(text="Search", bg="white", width=14, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()