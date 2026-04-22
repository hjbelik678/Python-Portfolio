# Henry B & Fox W

import random


def main():
    """probabilities
    " " = 20%
    0 = 40%
    1 = 40%
    """
    n = 1
    while n > 0:
        # generates random integer 1-5
        number = random.randint(1, 5)
        # number is 1, prints space
        if number == 1:
            print(" ", end="")
        # if number is 2 or 3, prints 0
        if number == 2 or number == 3:
            print("0", end="")
        # if number is 4 or 5, prints 1
        if number == 4 or number == 5:
            print("1", end="")


if __name__ == "__main__":
    main()
