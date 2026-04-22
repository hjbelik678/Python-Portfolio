"""
Add docstring here (do not forget authors)
"""


def is_leap_year(year):
    """Add docstring here"""
    # If the year is less than 1 then the result is `Year must be positive.`

    # * Determine whether the year is divisible by 100. If it is, then it is a leap year
    #   if and only if it is also divisible by 400. For example, 2000 is a leap year, but
    #   2100 is not.
    # * If the year is not divisible by 100, then it is a leap year if and only if it
    #   is divisible by 4. For example, 2008 is a leap year, but 2009 is not.
    if year < 1:
        return "Year must be positive."
    if (year % 100) == 0 and (year % 400) == 0:
        return "That year is a leap year."
    if (year % 100) != 0 and (year % 4) == 0:
        return "That year is a leap year."
    else:
        return "That year is not a leap year."


# ********************************************************************************************************************
# Look at, but do not edit code below this point.
# ********************************************************************************************************************
def main():
    # Get the year from the user
    entered_year = int(input("Enter the year: "))

    # Print the result
    print(is_leap_year(entered_year))


if __name__ == "__main__":
    main()
