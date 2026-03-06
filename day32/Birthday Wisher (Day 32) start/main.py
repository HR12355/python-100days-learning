# =====================
# Day32 学習メモ
# ======================
# やったこと
# メール送信の自動化、smtplib　module
# smtplib, pandas, osで.envからデータの取得, try関数
# 分かったこと
# 調べるときはまず、pythonのドキュメントから調べる癖をつける。再現性を重要視

# 詰まったこと

# ======================
# import smtplib
# import os
# from dotenv import load_dotenv
# load_dotenv()
#
# my_email = os.getenv("MY_EMAIL")
# password = os.getenv("PASSWORD")
#
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls() # 接続と暗号化
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg="Subject:Hello!\n\nThis the body of my email",
#     )

#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# date_of_birth =dt.datetime(year=1995, month=1, day=1, hour=12)
# print(date_of_birth)

import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
import random

load_dotenv()

# login info
my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

# get text_data
with open("quotes.txt") as file:
    text_list = file.readlines()
    quote = random.choice(text_list)
    new_quote = quote.replace('"', '')
print(new_quote)

# send time
now = dt.datetime.now()

if now.weekday() == 4:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Today's Quote\n\n{new_quote}"
        )


