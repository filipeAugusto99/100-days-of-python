# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.color("DarkSlateBlue")
timmy.shape("turtle")
timmy.forward(100)
timmy.left(50)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()