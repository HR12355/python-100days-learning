# =====================
# Day25 学習メモ
# ======================
# やったこと
# csvファイルの扱い
# pandasの使い方
# アメリカ州のクイズゲーム

# 分かったこと
# CSV = Comma Separated Values
# C:/...: ドライブの根っこから探す（絶対パス）
# ./...: 今のフォルダから探す（相対パス）
# pandasというライブラリの中のクラスであるSeries,DataFrame
# DataFrame（表全体）にできること data.to_dict()：表全体を辞書に
# Series（1列）にできること data["temp"].mean()：その列の平均。

# 詰まったこと
# 行の抜き出し Pandasの[]は、
# 中に 「名前（文字列）」 が入ってきたら → 列を探す
# 中に 「True/Falseのリスト」 が入ってきたら → Trueの行だけ残す
# データフレームから値を抽出すること。いろんな方法あり、at,loc,iloc,item
# itemは一つを取り出せて、今どの行の何列目かを判別する必要がない

# ======================
# with open("weather_data.csv") as weather_data:
#     data = weather_data.read lines()
#     strip_data = [weather.strip() for weather in data]

"""
一列抽出に時間がかかりすぎる
import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    # data_list = list(data)
    # temperatures = [row[1] for row in data_list[1:]] #リスト内包表記
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)
"""

"""
import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()

#平均気温
temp_list = data["temp"].to_list()
# print(data["temp"].mean())

print(data["temp"])
print(data["temp"].max())

# 列データを取得
# print(data["condition"])
# print(data.condition)

# 行データの取得
# print(data[data.day == "Monday"])

# 最高温度をもつ行
print(data[data.temp == data.temp.max()])

# 月曜日の気候
monday = data[data.day == "Monday"]
print(monday.condition)


# 月曜日の気温、華氏
def conversion(value):
    return value * 1.8 + 32
print(conversion(monday.temp))
print(monday.temp[0])

#pythonで生成したデータをDataFrameを作成
data2_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data2 = pandas.DataFrame(data2_dict)
# print(data2)
data2.to_csv("new_data.csv")"""

#リスの毛色別個体数の集計
import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# print(data)

new_data = []
colors = ["Gray", "Cinnamon", "Black"]
for color in colors:
    fur_colors = data["Primary Fur Color"].value_counts()[color]
    item = [color, int(fur_colors)]
    new_data.append(item)
# リストからdataframeを作成
columns = ["Fur_Color", "Count"]
df = pandas.DataFrame(new_data, columns=columns)
# df.to_csv("squirrel_count.csv")


