# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 11: The coin flip
# Date: wed oct 24 04:56:57 PM
"""
This program is a cool game built out of random module in python
"""
import random

print(
    "Hello user you are welcome to the coin flip game\n"
    "you are to guess the side of the coin flip output\n"
    "N.B:You are competing with the computer!!!"
)

play = True
while play:
    coin = random.choice(["head", "tail"])
    user_guess = input("What side are you choosing {Head or Tail}: ").lower()
    if coin == user_guess:
        print("Hooray!!!.\nYou guessed right.")
    else:
        print("Sorry that was wrong!")
    opt = input("\nWould you like to PLAY again{yes/no}: ").lower()
    if opt == "yes":
        play = True
    else:
        play = False
