from turtle import Screen
import turtle as t
import random

tim = t.Turtle()

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


directions = [0, 90, 180, 270]

t.pensize(10)
t.speed(10)

for _ in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
