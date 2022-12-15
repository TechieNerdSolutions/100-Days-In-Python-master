# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 14: The Rock Paper Scissors game
# Date: wed oct 24 11:41:44 PM
"""
The Rock Paper Scissors game
"""
import random

print("******** The Rock Paper Scissors game *********")
print("Welcome to the Rock Paper and Scissors game")

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER= """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
MOG = [ROCK, PAPER, SCISSORS]
while True:
#     options = ["ROCK", "PAPER", "SCISSORS"]
    choices = ["rock", "paper", "scissors"]
# help the compter choose randomly with th help of random.choice
    COMPUTER = random.choice(choices)
    PLAYER = None

    while PLAYER not in choices:
        print("Please make a choice") # get the user choice
        PLAYER = input("rock, paper, or scissors?: ").lower()

    if PLAYER == COMPUTER:
        print("Computer choose: ", COMPUTER)
        print("You choose:  ", PLAYER)
        print("Tie!")

    elif PLAYER == "rock":
        if COMPUTER == "paper":
            print(f"Computer choose: {PAPER} ", COMPUTER)
            print(f"You choose: {ROCK} ", PLAYER)
            print(" Oh ... Sorry Paper Covers Rock, So You Lose!")
        if COMPUTER == "scissors":
            print(f"Computer choose:{SCISSORS}  ", COMPUTER)
            print(f"You choose: {ROCK} ", PLAYER)
            print("Congratulations Rocks Crushes Scissors, You Win!")

    elif PLAYER == "scissors":
        if COMPUTER == "rock":
            print(f"Computer choose: {ROCK} ", COMPUTER)
            print(f"You choose: {SCISSORS} ", PLAYER)
            print("Oh ... Sorry Rocks Crushes Scissors, So You Lose!")
        if COMPUTER == "paper":
            print(f"Computer choose: {PAPER}", COMPUTER)
            print(f"You choose: {SCISSORS} ", PLAYER)
            print("Congratulations Scissors Cuts Paper, You Win!")

    elif PLAYER == "paper":
        if COMPUTER == "scissors":
            print(f"Computer choose: {SCISSORS} ", COMPUTER)
            print(f"You choose: {PAPER} ", PLAYER)
            print("Oh ... Sorry Scissors Cuts Paper, So You Lose!")
        if COMPUTER == "rock":
            print(f"Computer choose: {ROCK} ", COMPUTER)
            print(f"You choose: {PAPER} ", PLAYER)
            print("Congratulations Paper Covers Rock, You Win")

    play_again = input("Play again? (YES/NO): ").upper()

    if play_again != "YES":
        break

print("Bye!")
