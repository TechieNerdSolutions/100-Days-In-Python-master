# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 8: Leap Year Calculator
# Date: sat oct 22 04:45:20 PM
"""
leap year calculator
"""

print("********* Leap Year Calculator ************")
checker = True
while checker:
    try:
        year = int(input("Which year do you want to check?: "))
        YEAR = str(year)
        if len(YEAR) == 4:
            YEAR = int(YEAR)
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print(f"{year} it's leap year")
                    else:
                        print(f"{year} it's not leap year")
                else:
                    print(f"{year} it's leap year")
            else:
                print(f"{year} it's not leap year")
            opt = input("Would you like to check other years?: ")
            yes = ["Yes", "y", "Y", "1"]
            no = ["No", "N", "n", "2"]
            if opt in yes:
                checker = True
            elif opt in no:
                print("thanks, hope to see you another time ")
                checker = False
            else:
                break
        else:
            print("Please enter a vaild year example 2020")
            checker = True
    except ValueError:
        print("You should input only numbers")
        checker = True
