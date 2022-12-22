# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 1: Band Name Generator
# Date: wed oct 19 11:20:57 AM
"""
Band Name Generator
"""
# Function for mixing string LINE 20
print("********* BAND NAME GENERATOR ************")
check_name = True
while check_name:
    opt = input("Will you like to generate a name for your band? 1. Yes 2. No ")
    yes = ["Yes", "y", "Y", "1"]
    no = ["No", "N", "n", "2"]
    if opt in yes:
        print("Thanks, you have choose to generate a name for your band")
        firstname = input("What is your Firstname? ")
        lastname = input("What is your Lastname? ")
        nickname = input("What is your Nickname? ")
        city = input("Where do you live? ")
        print(city + " " + firstname[-2:] + lastname[:2] + nickname[2:6])
        check_name = False
    elif opt in no:
        print("Oh Thanks anyway we will be expecting you another day")
        check_name = True
    else:
        print("Invalid input ")
        check_name = True
