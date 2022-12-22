# @ Author Adewunmi Oladele A.K.A Rachamv
# testing: Prime checker
# Date: sat oct 30 09:52:00 PM
"""
Prime
"""

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)