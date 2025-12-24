from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
t.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def darw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(75)
        current_heading = t.heading()
        t.setheading(current_heading + size_of_gap)


darw_spirograph(1)

screen = Screen()
screen.exitonclick()
