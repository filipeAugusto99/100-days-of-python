from turtle import Turtle, Screen


def triangle():
    t.color("CadetBlue")
    for _ in range(3):
        t.forward(50)
        t.right(120)


def square():
    t.color("brown")
    for _ in range(4):
        t.forward(50)
        t.right(90)


def pentagon():
    t.color("chocolate")
    for _ in range(5):
        t.forward(50)
        t.right(72)


def hexagon():
    t.color("navy")
    for _ in range(6):
        t.forward(50)
        t.right(60)


def heptagon():
    t.color("OrangeRed")
    for _ in range(7):
        t.forward(50)
        t.right(51.42857142857143)


def octagon():
    t.color("RoyalBlue")
    for _ in range(8):
        t.forward(50)
        t.right(45)


def nonagon():
    t.color("green")
    for _ in range(9):
        t.forward(50)
        t.right(40)


def decagon():
    t.color("blue")
    for _ in range(10):
        t.forward(50)
        t.right(36)


t = Turtle()

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = Screen()
screen.exitonclick()
