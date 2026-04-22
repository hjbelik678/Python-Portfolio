import sys
"""Henry B
Fox W
"""


def digit_sum(number):
    """When given an integer this function returns the sum of its digits. Sign is ignored. """
    # determines length of number
    number_length = len(str(number))
    total = 0
    for i in range(1, number_length + 1):
        if number < 0:
            number = number * -1
        digit = number // 10 ** (number_length - i)
        number = number % 10 ** (number_length - i)
        # keeps running total
        total = digit + total
    return total


# As long as the user enters a non-zero integer n, keep printing the sum of the digits of n.
def main():
    entered_number = int(input("Enter number(zero quits): "))
    while entered_number != 0:
        if entered_number == 0:
            return sys.exit(1)
        total = digit_sum(entered_number)
        print(f"Total= {total}")
        entered_number = int(input("Enter number(zero quits): "))


# ********************************************************************************************************************
# Do not edit the code below this point
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
