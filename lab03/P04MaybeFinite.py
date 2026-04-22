"""Henry Belik & Fox woods
Complete P04MaybeFinite so that prompts the user for a starting n. and then prints the sequence generated this way with
 a comma space between each term of the sequence. The sequence should end with one new line after the last number."""


def print_sequence(n):
    print(f"{n}", end="")
    while n != 1 and n > 0:
        # if n is even, n is halved
        if n % 2 == 0:
            n = n // 2
            print(f", {n}", end="")
        # if n is odd, it gets tripled and 1 added to it
        elif n % 2 == 1 and n != 1:
            n = n * 3 + 1
            print(f", {n}", end="")
        # if n is 1, prints 1/n
        elif n == 1:
            print(f", {n}", end="")
    print()


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
PROMPT = "Enter the starting value for n (positive integer): "


def main():
    # Ask user for n
    entered_n = int(input(PROMPT))
    while entered_n <= 0:
        print(f"The entered value {entered_n} is not a positive integer.")
        entered_n = int(input(PROMPT))

    # Print the sequence
    print_sequence(entered_n)


if __name__ == "__main__":
    main()
