from hart import logo, vs
from game_data import data
from replit import clear
from random import choice

score = 0
guess_is_right = True
# generate a RANDOM ACCoUNT
def celbrity(data):
    """Function to get data from the game data randomly"""
    test = choice(data)
    #test = data
    name = test["name"]
    follower = test["follower_count"]
    description = test["description"]
    country = test["country"]
    #return f" {name}, a {description}, from {country}."
    return[name,follower,description,country]

against = celbrity(data)

# IF USER GUESSED RIGHT PRINT THE SCORE AND CONTINUE THE GAME
while guess_is_right:
    print(logo)
    #  PRINT VS AND GENERATE THE SECOND ACCOUNT
    compare = against
    print(f"Compare A: {compare[0]}, a {compare[2]}, from {compare[3]}.")
    print(vs)
    against = celbrity(data)
    print(f"Against B: {against[0]}, a {against[2]}, from {against[3]}.\n")
    # ASK USER FOR A GUESS
    guess = input("Who have more followers? Type 'A' or 'B': ").lower()
    # CHECK IF USER IS CORRECT BY CONFIRMING THE FOLLOWER
    if compare[1] > against[1]:
        if guess == "a":
            score += 1
            clear()
            print(f"You're right! Current score: {score}.")
            
        else:
            clear()
            guess_is_right = False
            print(f"Sorry, that's wrong. Final score: {score}")
            
    else:
        if guess == "b":
            score += 1
            clear()
            print(f"You're right! Current score: {score}.")
        else:
            # NB CLEAR THE SCREEN
            clear()
            # ELSE PRINT THE FINAL SCORE AND GAME OVER
            guess_is_right = False
            print(f"Sorry, that's wrong. Final score: {score}")


'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''



# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

            