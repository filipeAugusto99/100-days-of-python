from turtle import Turtle, Screen


def print_key(key):
    print(f"key pressed: {key}")


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def counter_clockwise():
    t.left(10)


def clockwise():
    t.right(10)


def clear_drawing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


t = Turtle()
scr = Screen()

scr.listen()
scr.onkeypress(key="w", fun=move_forwards)
scr.onkeypress(key="s", fun=move_backwards)
scr.onkey(key="a", fun=counter_clockwise)
scr.onkey(key="d", fun=clockwise)
scr.onkey(key="c", fun=clear_drawing)


scr.exitonclick()
