from turtle import Turtle, Screen


def square():
    for _ in range(4):
        tim.forward(50)
        tim.right(90)
        tim.forward(50)


tim = Turtle()

square()

screen = Screen()
screen.exitonclick()
