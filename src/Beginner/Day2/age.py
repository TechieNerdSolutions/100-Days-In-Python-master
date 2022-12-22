# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 2: Age Calculator
# Date: friday oct 21 04:00:26 PM
"""
Age calculator
"""

print("********* Age Calculator ************")
present_age = input("What is your present age? ")
age = int(present_age)
years_remaining = 90 - age
days_remaining = years_remaining * 356
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f":{years_remaining}, Months:{months_remaining},"
message1 = f"Weeks is: {weeks_remaining}, and Days remaining is: {days_remaining}"
print(f"Your remaining years if you are to live up to 90 is {message} {message1}")
if years_remaining <= 10:
    print("You still have time to correct your mistake and help others use it wisely")
else:
    print("You still have a long life to live please use it wisely")
