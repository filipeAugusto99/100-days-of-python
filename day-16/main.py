# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.color("DarkSlateBlue")
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.left(50)
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()  
table.field_names = ["Pokemon Name", "Types"]
table.add_row(["Pikachu", "Eletric"])
table.add_row(["Squirtle", "Aquatic"])
table.add_row(["Charmander", "Fire"])

table.align = "l"

print(table)