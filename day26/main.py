# =====================
# Day26 学習メモ
# ======================
# やったこと
# list and dict comprehensions
# 分かったこと
# new_list = [new_item for item in list] リスト内包表記
# new_list = [new_item for item in list　if test] 条件付きリスト
# new_dict = {new_key: new_value for (key,value) in dict.items()}
# 詰まったこと
# Row = 行　Column = 列
# 文字列も一文字ずつ並んだリストのようなもの
# code = [new_dict[key] for key in "ABCD"]
# ======================
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

import pandas

student_df = pandas.DataFrame(student_dict)
#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98

#データフレームの各列をループ
# for (key, value) in student_df.items():
#     print(value)
# 0    Angela
# 1     James
# 2      Lily
# Name: student, dtype: object
# 0    56
# 1    76
# 2    98
# Name: score, dtype: int64

#データフレームの各行をループ
for (index, row) in student_df.iterrows():
    # print(row)
# student    Angela
# score          56
# Name: 0, dtype: object
# student    James
# score         76
# Name: 1, dtype: object
# student    Lily
# score        98
# Name: 2, dtype: object
#     print(row.student)
# Angela
# James
# Lily
    if row.student == "Angela":
        print(row.score)