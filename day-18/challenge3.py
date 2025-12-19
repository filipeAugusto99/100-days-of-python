from turtle import Turtle, Screen
import random

t = Turtle()

colours = [
    "gainsboro",
    "cornflower blue",
    "orange red",
    "red",
    "blue",
    "black",
    "yellow",
    "dark slate blue",
]


def draw_shape(num_slides):
    angle = 360 / num_slides
    for _ in range(num_slides):
        t.forward(100)
        t.right(angle)


for shape_side_n in range(3, 11):
    t.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
