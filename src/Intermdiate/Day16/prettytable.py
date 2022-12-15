# OOPS
from turtle import Turtle, Screen
from prettytable import PrettyTable

car = Turtle()
print(car)

my_screen = Screen()
print(my_screen.canvheight)
car.shape("turtle")
car.color("coral")
car.forward(50)

print("*********************************")

# pretty table usage
table = PrettyTable()

table.add_column(fieldname="Pokemon", column=["Pikachu", "Charizard", "Bulbasor"])
table.add_column(fieldname="Type", column=["electric", "fire", "water"])
table.align = 'l'  # left alignment
print(table)