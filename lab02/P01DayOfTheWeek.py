"""
Authors Fox Woods And Henry B
"""


def day_of_week(day_number):
    """converts corresponding number into day of the week"""
    if day_number == 1:
        return str("Monday")
    elif day_number == 2:
        return str("Tuesday")
    elif day_number == 3:
        return str("Wednesday")
    elif day_number == 4:
        return str("Thursday")
    elif day_number == 5:
        return str("Friday")
    elif day_number == 6:
        return str("Saturday")
    elif day_number == 7:
        return str("Sunday")
    else:
        return str("Error")


# ********************************************************************************************************************
# Look at, but do not edit code below this point.
# ********************************************************************************************************************
def main():
    # Get day number from user
    entered_day = int(input("Enter the number of a day (1-7): "))

    # Note we could check that the day number is valid here. This time we are going to let the function check the
    # number is valid
    #
    # Convert day number into string
    day_name = day_of_week(entered_day)

    # Was there an error?
    if day_name == "Error":
        print("The number entered is not in the range 1 to 7.")
    else:
        print(f"The day entered is {day_name}")


if __name__ == "__main__":
    main()
