import random
import turtle

from colorgram import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)


def generate_rgb():
    color_list = []

    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        rgb = (red, green, blue)
        color_list.append(rgb)

    return color_list


colors = colorgram.extract('20_001.jpg', 20)
colour_list = generate_rgb()

timmy = Turtle()
timmy.penup()
timmy.goto(-200, -200)
timmy.hideturtle()

for i in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(colour_list))
        timmy.penup()
        timmy.forward(50)

    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180) if i % 2 == 0 else timmy.setheading(0)
    timmy.forward(50)


screen = Screen()
screen.exitonclick()
