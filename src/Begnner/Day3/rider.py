# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 5: Ticket
# Date: sat oct 22 05:38:26 PM
"""
Ticket for Rollercoster
"""

print("\t \t ************* Ticket **************")
print("\t \t Welcome to the Rollercoster!")
print("\t \t We are happy to have you ride with us!")

rider = True
while rider:
    height = int(input("Please enter your height in cm: "))
    age = int(input("please enter your age: "))
    under_12 = 5
    under_18 = 10
    adult = 15
    photo = input("Do you want a photo taken? 1. Yes 2. No :  ")
    want_photo = 3
    yes = ["Yes", "y", "Y", "1"]
    no = ["No", "N", "n", "2"]
    if height >= 120:
        rider = False
        if age <= 12:
            if photo in yes:
                bill = want_photo + under_12
                print(f"Your total bill is {bill}")
                rider = False
            elif photo in no:
                print(f"child tickets are ${under_12}")
                rider = False
            else:
                print("Invalid input please try again")
                rider = True
        elif age <= 18:
            if photo in yes:
                bill = want_photo + under_18
                print(f"Your total bill is {bill}")
                rider = False
            elif photo in no:
                print(f"Youth tickets are ${under_18}")
                rider = False
            else:
                print("Invalid input please try again")
                rider = True
        else:
            if photo in yes:
                bill = want_photo + adult
                print(f"Your total bill is {bill}")
                rider = False
            elif photo in no:
                print(f"Adult tickets are ${adult}")
                rider = False
            else:
                print("Invalid input please try again")
                rider = True
    else:
        print("Sorry, you have to grow taller before you can ride.")
        rider = True
