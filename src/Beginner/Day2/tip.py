# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 4: Tip Calculator
# Date: friday oct 21 04:07:49 PM
"""
tip calculator
"""

print("********** Tip Calculator ************")
print("Welcome To Tip Calculator")
bill = float(input("Please enter the total bill to pay:$ "))
people = int(input("How many people to split the bill: "))
tip = int(input("How much tip will you to give? example 10, 12, 15 or 20? : "))
cal = tip / 100
amount = bill * cal
total_bill = bill + amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
