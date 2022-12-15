# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 10: The bill Payer
# Date: wed oct 24 04:56:57 PM
"""
The bill payer
"""
from random import randint

# receive the names of all participant
names = input("names: ")

# filter through the name and pick a random name
names = names.split(" ")
index = randint(0, len(names) - 1)

# return the chosen name
print(f"Hey {names[index]} you have been chosen to pay the bill")