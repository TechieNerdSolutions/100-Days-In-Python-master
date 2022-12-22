# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 22: Painter calculator Project
# Date: mon oct 31 11:06:04 AM
"""
for painter
"""
import math

def paint_calc(height, width, cover):
    area = height * width
    num_cans = area / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

# Define a function called paint_calc() so that the code below works.   

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)