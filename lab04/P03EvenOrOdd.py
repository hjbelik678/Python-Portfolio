"""Henry B & Fox W"""

import random
import sys


def is_even(n):
    """Determines if number is even"""
    return n % 2 == 0


def sum_two_dice():
    """Sum of two six sided dice"""
    return random.randint(1, 6) + random.randint(1, 6)


def get_user_guess():
    """Gets a user's guess for if the dice roll will be even or odd. This function prompts the user for their guess and
    returns it as a string. The user's guess must be either "even" or "odd" and this function will continue to ask the
    user for input if they do not enter a valid guess."""
    guess = input("Guess if the sum of two fair six side dice is even: ").lower()
    while guess != "even" and guess != "odd":
        # makes sure guess is even or odd
        print("Must be even or odd.")
        guess = input("Guess if the sum of two fair six side dice is even: ").lower()
    return guess


def play_round():
    """Play one round of the dice game. This function returns True if the user wins and False otherwise."""
    user_guess = get_user_guess()

    # Roll the dice using sum_two_dice and store the result in a variable.
    rolled_sum = sum_two_dice()

    # Print the sum of dice roll
    print(f"rolled sum: {rolled_sum}")

    # Determine if the user won or lost. Print an appropriate message
    if (is_even(rolled_sum) and user_guess == "even") or (not is_even(rolled_sum) and user_guess == "odd"):
        print("You won")
        return True
    else:
        print("Sorry you lost")
        return False


def main():
    win_total = 0
    while True:
        this_round = play_round()
        if this_round:
            win_total += 1
        print(f"wins: {win_total}")
        # While the user wants to play, play a round of the game (after each round, print how many rounds have been won)
        again = input("Would you like to play again?(y or n) ")
        if again != "y":
            # Print a message thanking the user for playing
            print("Thanks for playing!")
            sys.exit(1)


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
