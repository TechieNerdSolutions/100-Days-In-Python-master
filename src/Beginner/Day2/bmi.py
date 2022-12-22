# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 3: Body Mass Index
# Date: friday oct 21 08:00:26 AM
"""
Body Mass Index Calculator
"""

print("********* Body Mass Index Calculator ************")
MASS = True
while MASS:
    opt = input("Will you like to check your Body Mass Index? 1. Yes 2. No ")
    yes = ["Yes", "y", "Y", "1"]
    no = ["No", "N", "n", "2"]
    if opt in yes:
        print("Thanks, It's time to check your height and weight.")
        body_height = float(input("Dear friend, kindly enter your height in m: "))
        body_weight = int(input("Dear friend kindly enter your weight in kg: "))
        body_mass_check = body_weight // body_height ** 2
        print(f"Your BMI is : {body_mass_check}")  # , + int(body_mass_check))

        if body_mass_check < 18.5:
            print("You are Underweight and at risk of Possible ")
            print("nutritional deficiency and osteoporosis.")
        elif 18.5 < body_mass_check < 25:
            print("You are at Normal and have low health risk, Please maintain it.")
        elif 25 < body_mass_check <= 30:
            print("You are Mild to moderate weight and Moderate risk of developing ")
            print("heart disease, high blood pressure, stroke, diabetes mellitus..")
        else:
            print("You are Overweight and at High risk of developing heart disease, ")
            print("high blood pressure, stroke, diabetes mellitus. Metabolic Syndrome.")
        MASS = True
    elif opt in no:
        print("Oh Thanks anyway we will be expecting you another day")
        MASS = True
    else:
        print("Invalid input ")
        MASS = True
