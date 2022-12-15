# @ Author Adewunmi Oladele A.K.A Rachamv
# Project 21: Hangman Project
# Date: sat oct 29 01:29:00 PM
"""
Hangman
"""
import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

player = input("What should we call you?:\n ")
# rule of the game
print(f"Hello {player}, welcome to Hangman game.\n")
print("You are to guess the hidden word by guessing each of its leters\n") 
print("NB:You have ❤ ❤ ❤ ❤ ❤ ❤ lives. For each incorrect guess you make you lose a live\n")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks "_"
display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input(f"{player}, Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") #for testing
        if letter == guess:
            display[position] = letter
            #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("Oh sorry You lose.")

    #Check if user has got all letters.
    if not "_" in display:
        game_is_finished = True
        print(f"{player},Congratulation You win.")
    # print the ASCII art from 'stages'
    print(stages[lives])

    
