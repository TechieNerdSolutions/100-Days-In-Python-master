# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 17: FizzBuzz
# Date: wed oct 26 10:55:00 AM
"""
fizzBuzz
"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # Divisble by both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
