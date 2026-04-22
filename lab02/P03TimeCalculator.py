"""
authors: Henry Belik, Fox Woods
"""

# Add constants and functions as needed (in later labs I will not remind you to do this).
SECONDS_IN_A_DAY = 86400
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_MINUTE = 60


def seconds_to_time(seconds):
    """calculates the number of day, hours, minutes, and seconds in a given number of seconds"""
    # Replace the following return with your code to complete this function
    days_remaining = seconds // SECONDS_IN_A_DAY
    hours_remaining = (seconds % SECONDS_IN_A_DAY) // SECONDS_IN_AN_HOUR
    minutes_remaining = (((seconds % SECONDS_IN_A_DAY) % SECONDS_IN_AN_HOUR) // SECONDS_IN_A_MINUTE)
    seconds_remaining = (((seconds % SECONDS_IN_A_DAY) % SECONDS_IN_AN_HOUR) % SECONDS_IN_A_MINUTE)
    if days_remaining != 0:
        return f"{days_remaining} day(s), {hours_remaining} hour(s), {minutes_remaining} minute(s), " \
               f"and {seconds_remaining} second(s)"
    elif hours_remaining != 0:
        return f"{hours_remaining} hour(s), {minutes_remaining} minute(s), " \
               f"and {seconds_remaining} second(s)"
    elif minutes_remaining != 0:
        return f"{minutes_remaining} minute(s) and {seconds_remaining} second(s)"
    elif seconds_remaining != 0 or seconds_remaining == 0:
        return f"{seconds_remaining} second(s)"


# ********************************************************************************************************************
# Look at, but do not edit code below this point.
# ********************************************************************************************************************
def main():
    # Get number of seconds from the user
    entered_seconds = int(input("Enter the number of seconds: "))

    # Print the result
    print(seconds_to_time(entered_seconds))


if __name__ == "__main__":
    main()
