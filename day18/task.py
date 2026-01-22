import colorgram
import random
from turtle import Turtle, Screen, colormode

kameo = Turtle()
colormode(255)
kameo.pensize(20)
kameo.speed("fast")


colors = colorgram.extract('picture/image1.png', 20)
# print(colors)
# first_color = colors[0]
# print(first_color)
# rgb = first_color.rgb
# red = rgb.r
# print(red)


def random_color():
    color_choice = random.choice(colors)
    rgb = color_choice.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    kameo.color(red, green, blue)

def side_move(width):
    for _ in range(width):
        random_color()
        kameo.dot(20)
        kameo.penup()
        kameo.forward(40)
        kameo.pendown()
# side_move(6)

def spot_painting(width, height, position):
    y_axis = 0
    kameo.penup()
    kameo.hideturtle()
    kameo.goto(- position, - position)
    kameo.pendown()
    for _ in range(height):
        side_move(width)
        kameo.penup()
        kameo.hideturtle()
        y_axis += 40
        kameo.goto(- position, - position + y_axis)
        kameo.pendown()

spot_painting(10, 10, 200)


screen = Screen()
screen.exitonclick()