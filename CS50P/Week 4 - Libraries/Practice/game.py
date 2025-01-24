"""
In a file called game.py, implement a program that:

Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random

def main():
    guess_game()

def guess_game():
    level = 0
    while(level == 0):
        try:
            level = int(input("Level: "))
        except:
            continue
    number = random.randint(1, level)
    user_guess = 0
    while(user_guess != number):
        try:
            user_guess = int(input("Guess: "))
            if(user_guess > number):
                print("Too large!")
            elif(user_guess < number):
                print("Too small!")
            else:
                print("Just right!")
        except EOFError:
            return
        except:
            continue

main()
