"""
Determines the number of real roots of a second degree polynomial expression
Henry B & Fox Woods
"""

import sys


def number_of_roots(a, b, c):
    """calculates the discriminant then determines how many real roots it has"""
    # Complete the program [P05NumberOfRoots](P05NumberOfRoots.py) so that it prompts
    # the user to enter the coefficients (as floats) of a quadratic polynomial and then
    # prints how many real roots the quadratic has. If the user enters 0 for $a$ then
    # print an error message and stop (i.e. do not print anything more than the error
    # message). You must complete the function `number_of_roots` so that it returns the
    # number of roots for the given quadratic polynomial.
    # calculates the discriminant
    discriminant = (b ** 2) - (4 * a * c)
    # determines how many roots it has
    if discriminant == 0:
        return 1
    elif discriminant > 0:
        return 2
    elif discriminant < 0:
        return 0


def main():
    # Asks the user for the value of a
    a_value = float(input("first coefficient(a value): "))
    # determines if the user entry is valid (e.g. positive and non-zero) and exits if not true
    if a_value == 0 or a_value < 0:
        print("invalid entry, must be non-zero and positive")
        sys.exit(0)
    # Asks the user for the value of b and c
    b_value = float(input("second coefficient(b value): "))
    c_value = float(input("third coefficient(c value): "))

    # Uses the function described above to find the discriminant and determine the number of real roots
    calculated_discriminant = number_of_roots(a_value, b_value, c_value)
    print(f"{calculated_discriminant}")


# ********************************************************************************************************************
# Do not edit code below this point.
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
