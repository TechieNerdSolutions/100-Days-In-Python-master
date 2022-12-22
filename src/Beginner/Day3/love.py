# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 7: Love Calculator
# Date: Sunday oct 23 07:57:10 pM
"""
Love Calculator
"""
print("Welcome to the Love Calculator!")
name = input("Enter your name? \n")
name1 = input("Enter his/her name? \n")
combined_string = name + name1
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

LOVE_SCORE = int(str(true) + str(love))

if (LOVE_SCORE < 10) or (LOVE_SCORE > 90):
    print(f"Your love score is {LOVE_SCORE}, you are gue together")
elif (LOVE_SCORE >= 40) or (LOVE_SCORE <= 50):
    print(f"Your love score is {LOVE_SCORE}, you are good together")
else:
    print(f"Your love score is {LOVE_SCORE}")
