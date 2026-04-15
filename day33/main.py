# =====================
# Day33 学習メモ
# ======================
# やったこと
# API

# 分かったこと
# API= Application Programming Interface プログラム専用窓口
# リクエストモジュール

# 詰まったこと

# ======================
import requests

response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
# print(response.status_code)
response.raise_for_status() #200以外なら自動で止まる

data = response.json()
data2 = response.json()["latitude"] #辞書のように使える
print(data)
print(data2)
