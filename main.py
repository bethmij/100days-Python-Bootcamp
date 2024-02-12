from turtle import Turtle, Screen
from prettytable import PrettyTable
# timmy = Turtle()
# timmy.color("red", "green")
# my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Name", ["Kamal", "Namal", "Supun"])
table.add_column("Age", [30, 21, 44])
print(table)

