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

directions = [0, 90, 180, 270]

t.pensize(10)
t.speed(10)

for _ in range(200):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
