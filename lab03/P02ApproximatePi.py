"""Henry B & Fox W"""


def product_of_terms(n):
    """Returns the product of the first n terms of 2/1 * 2/3 * 4/3 * 4/5 * 6/5 * 6/7 * 8/7 * 8/9 * ..."""
    # sets initial values
    total = 1
    numerator = 0
    denominator = 1
    # print(f"{numerator}/{denominator} * ", end="")
    for n in range(1, n + 1):
        if (n + 2) % 2 == 1:
            # if n is odd add 2 to the numerator
            numerator += 2
            # print(f"{numerator}/{denominator} * ", end="")
        elif (n + 2) % 2 == 0:
            # if n is even add 2 to the denominator
            denominator += 2
            # print(f"{numerator}/{denominator} * ", end="")
        # updates total after change to numerator or denominator
        total *= numerator / denominator
    return total


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
PROMPT = "Enter the number of terms to use (0 or less quits): "


def main():
    # Get the size from the user
    number_of_terms = int(input(PROMPT))

    # Keep running while number of terms is >= 1
    while number_of_terms >= 1:
        approximation = 2.0 * product_of_terms(number_of_terms)
        print(f"With {number_of_terms} term(s) pi is approximately {approximation}")
        number_of_terms = int(input(PROMPT))


if __name__ == "__main__":
    main()
