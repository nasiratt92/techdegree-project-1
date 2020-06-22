"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def quesion():
    guess = int(input("Guess a number between 1 - 10:  "))

def start_game():
    #print("hello world !")
    guess = 0
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player."""
    print("Hi there! let's play the number guessing game")
    """2. Store a random number as the answer/solution."""
    solution = random.randrange(1, 11)
    """3. Continuously prompt the player for a guess."""
    print(solution)
    guess_tally = 0

    #quesion()
    """a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher"."""

    while True:
        guess = int(input("Guess a number between 1 - 10:  "))
        if guess == solution:
            print("\nCongrats you guessed right")
            break
        elif guess < solution:
            guess_tally += 1
            print("It's higher")
            continue
        elif guess > solution:
            guess_tally += 1
            print("It's lower")
            continue


#4. Once the guess is correct, stop looping, inform the user they "Got it" and show how many attempts it took them to get the correct number.
    #5. Let the player know the game is ending, or something that indicates the game is over.
    #( You can add more features/enhancements if you'd like to. )
    print(
    """\nThis game has ended
\nYou took {} guesses to guess the right number"""
    .format(guess_tally))
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()
