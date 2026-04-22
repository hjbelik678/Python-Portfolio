import random
import sys

"""Henry B & Fox W
random number guessing game
"""

MIN_NUMBER = 100
MAX_NUMBER = 999
POSSIBLE_NUMBER_LENGTH = 3


def has_digit_in_correct_place(guess, target):
    """Returns True if guess and target have at least one digit that is the same and in the same location. Returns
    False otherwise. Both guess and target are assumed to be integers between 100 and 999."""
    # determines digits in guess
    hundreds_place_guess = guess // 100
    guess = guess % 100
    tens_place_guess = guess // 10
    guess = guess % 10
    ones_place_guess = guess
    # determines digits in target
    hundreds_place_target = target // 100
    target = target % 100
    tens_place_target = target // 10
    target = target % 10
    ones_place_target = target
    if hundreds_place_target == hundreds_place_guess or tens_place_target == tens_place_guess or \
            ones_place_target == ones_place_guess:
        return True
    else:
        return False


def has_same_digit(guess, target):
    """Returns True if and only if guess and target have at least one digit in common no matter the location. Otherwise,
    False is returned. Both guess and target are assumed to be integers between 100 and 999."""
    # determines digits in guess
    hundreds_place_guess = guess // 100
    guess = guess % 100
    tens_place_guess = guess // 10
    guess = guess % 10
    ones_place_guess = guess
    # determines digits in target
    hundreds_place_target = target // 100
    target = target % 100
    tens_place_target = target // 10
    target = target % 10
    ones_place_target = target
    # determines if any of the digits are the same as each other
    if hundreds_place_guess == hundreds_place_target or hundreds_place_guess == tens_place_target \
        or hundreds_place_guess == ones_place_target or tens_place_guess == hundreds_place_target or \
        tens_place_guess == tens_place_target or tens_place_guess == ones_place_target or \
        ones_place_guess == hundreds_place_target or ones_place_guess == tens_place_target or ones_place_guess == \
            ones_place_target:
        return True
    else:
        return False


# Edit the program as you wish to complete the project. Remember to follow good programming practices.
def main():
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    for n in range(10):
        guess = int(input("Enter integer guess (100-999): "))
        correct_place = has_digit_in_correct_place(guess, answer)
        correct_digit = has_digit_in_correct_place(guess, answer)
        if guess == answer:
            print("Congrats, you guessed correctly, would you like to play again?")
            sys.exit(0)
        if correct_place:
            print("You have at least one digit that is correct and in the correct location.")
        if correct_digit:
            print("You have at least one digit correct, but not in the correct location.")
        else:
            print("You have no correct digits.")
    print(f"Correct answer: {answer}")


if __name__ == "__main__":
    main()
