# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen

color_list = [(188, 74, 20), (56, 34, 13), (149, 26, 9), (237, 226, 77), (24, 31, 60), (113, 167, 210), (45, 85, 143), (217, 154, 82), (34, 50, 124), (191, 144, 25), (26, 51, 29), (201, 93, 126), (242, 214, 6), (250, 244, 249), (119, 35, 51), (120, 187, 149), (55, 129, 74), (70, 82, 17), (36, 84, 40), (142, 51, 58), (74, 128, 200), (205, 86, 62), (82, 31, 44), (104, 180, 70), (148, 204, 223), (197, 120, 162), (23, 77, 100)]


def draw_dots(row_count):
    a = -(row_count * 25)
    b = a
    for _ in range(row_count):
        tim.setpos(a, b)
        for i in range(row_count):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)
        b += 50
    tim.hideturtle()

tim = Turtle()

tim.speed(0)
turtle.colormode(255)
tim.penup()


draw_dots(10)

my_screen = Screen()
my_screen.exitonclick()

