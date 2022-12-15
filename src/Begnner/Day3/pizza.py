# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 6: Pizza Deliveries
# Date: Sunday oct 23 07:30:30 pM
"""
Pizza Deliveries
"""
print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza = 15
medium_pizza = 25
large_pizza = 40
pepperoni = 5
pepperoni_small = 2
cheese = 4

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 25
elif size == "L":
    bill += 40
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 5

if cheese == "Y":
    bill += 4
print(f"Your final bill is ${bill}")
