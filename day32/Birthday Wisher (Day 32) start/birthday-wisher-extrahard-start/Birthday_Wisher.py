##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas
import os
from dotenv import load_dotenv
import datetime
import random

load_dotenv()

# ログイン情報
user_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

# 誕生日の人
now = datetime.datetime.now()
birthday_month = now.month
birthday_day = now.day

# 誕生日情報をdfに
birthday_df = pandas.read_csv("birthdays.csv")
# print(birthday_df)

# 今日誕生日の人　
birthday_index = birthday_df.index[(birthday_df["month"] == birthday_month) & (birthday_df["day"] == birthday_day)]
# print(birthday_index)
# Index([1], dtype='int64') [1]はリストのような箱とみてよい

# 手紙のフォーマットの選択
def letter_choice():
    letter_template_list = []
    with open("letter_templates/letter_1.txt") as file:
        text1 = file.read()
    with open("letter_templates/letter_2.txt") as file:
        text2 = file.read()
    with open("letter_templates/letter_3.txt") as file:
        text3 = file.read()
        letter_template_list.extend([text1, text2, text3])
# 三つのテンプレートから一つを選び、文字置換
    choice_template = random.choice(letter_template_list)
    letter_template1 = choice_template.replace("[NAME]", birthday_df.at[birthday_num, "name"]).replace("Angela", "Ken")
    return letter_template1

try:
    birthday_num = birthday_index[0]

except IndexError: # 誕生日の人がいない時
    print("今日誕生日の人はいないよ")

else:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(user=user_email, password=password)
        smtp.sendmail(
            from_addr=user_email,
            to_addrs=birthday_df.at[birthday_num, "email"],
            msg=f"Subject:Happy BirthDay!\n\n{letter_choice()}"

        )

# print(type(letter_choice()))