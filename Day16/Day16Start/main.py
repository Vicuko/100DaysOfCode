# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("aquamarine")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander","Bulbasaur"])
table.add_column("Type", ["Electric","Water","Fire","Grass"])
table.align["Pokemon Name"]="r"
print(table)