"""
Fox W and Henry
"""


def echo_print(message, times):
    # prints inputted message inputted amount of times
    print(message * times, end="")


def print_stars(height):
    for n in range(1, height + 1):
        # print 1 * for the first level
        if n == 1:
            print("*")
        # if last level, print all stars
        elif n == height:
            print("*" * n)
        # if any level inbetween, print * then number of spaces then *
        elif n - 2 >= 0:
            echo_print("*", 1)
            echo_print(" ", (n - 2))
            print("*")


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
PROMPT = "Enter the size of figure (negative value quits): "


def main():
    # Get the size from the user
    size = int(input(PROMPT))

    # Keep printing stars while the size is not negative
    while size >= 0:
        print_stars(size)
        size = int(input(PROMPT))


if __name__ == "__main__":
    main()
