from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.forward(10)
    tim.color("white")
    tim.forward(10)
    tim.color("black")

screen = Screen()
screen.exitonclick()
