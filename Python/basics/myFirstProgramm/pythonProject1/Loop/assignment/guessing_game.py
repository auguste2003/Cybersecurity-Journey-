"""
Exercise 3: Guessing Game

Write a simple number guessing game where the user has to guess a number between 1 and 10.
Use a while loop to keep asking the user for a guess until they get it right.
If the user wants to give up, they can type "exit" to end the game.
Use break to exit the loop if the user guesses correctly.
"""
from random import randint

number = randint(1, 10)  # Generate a random number between 1 and 10
guess = input("Guess a number between 1 and 10 (or type 'exit' to quit): ")

while True: # the loop runs continuelly until the user wins or tipps exit
    if guess.lower() == "exit":
        print("Thanks for playing!")
        break
    try:
        if int(guess) == number:
            print("You got it!")
            break
        else:
           guess = input("Try again, guess a number between 1 and 10 (or type 'exit' to quit): ")
    except ValueError:
        #  if the guess is not a number and not 'exit', handle the error
        guess =input("Please enter a valid number between 1 and 10 (or type 'exit' to quit): ")





