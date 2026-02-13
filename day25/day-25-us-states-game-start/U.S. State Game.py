import turtle
import pandas
from jinja2.utils import missing

FONT = ("Arial Black", 5, "normal")
FONT_CLEAR = ("Arial Black", 30, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
# 正解した州に亀(地名)を配置する関数
def state_place(states, x, y):
    pen.goto(int(x), int(y))
    pen.write(states, align="center", font=FONT)

# 現在のスコア
score_count = 0
answer_box = []

on_game = True
while on_game:
    answer_state = screen.textinput(title=f"{score_count}/50 Guess the state", prompt="What's another state's name?").title()
    answer_row = data[data["state"] == answer_state]

    # exitで答えられなかった州をcsvとして保存
    if answer_state == "Exit":
        # missing_states = []
        # for state in data.state.to_list():
        #     if state not in answer_box:
        #         missing_states.append(state)
        missing_states = [state for state in data.state.to_list() if state not in answer_box]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing states.csv")
        break
    # 正解の場合
    if not answer_row.empty and answer_state not in answer_box:
        # answer_row = data[data["state"] == answer_state]
        # state_place(answer_row.iloc[0, 0], answer_row.iloc[0, 1], answer_row.iloc[0, 2])
        state_place(answer_row.state.item(), answer_row.x.item(), answer_row.y.item())
        answer_box.append(answer_state)
        score_count += 1

    # 不正解の場合,入力が空白の場合
    else:
        pass

    # 全問正解
    if score_count == 50:
        pen.color("orange")
        pen.goto(0, 270)
        pen.write("Game Clear", align="center", font=FONT_CLEAR)
        on_game = False

screen.exitonclick()