# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 5: Ticket
# Date: sat oct 22 05:38:26 PM
# rider 2 is a simpler code
"""
Ticket for Rollercoster
"""

print("\t \t ************* Ticket **************")
print("\t \t Welcome To The Rollercoster!")
print("\t \t We are happy to have you ride with us!")
height = int(input("Please enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("please enter your age: "))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 10
        print("Youth tickets are $10")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us")
    else:
        bill = 15
        print("Adult tickets are $15")

    photo = input("Do you want a photo taken? Y or N. ")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
