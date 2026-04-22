"""
CSM 2170: P04ArrivalTime

Assuming there are no delays the distance that a car travels is given by:
    Distance = Speed * Time

This program finds the arrival time for a given distance and speed.
Author(s): Fox Woods And Henry Belik
"""


# Add any needed constants here


def print_arrival_time(distance, speed):
    """Assuming no delays and a constant speed, print the time to arrive as:
    Arrival in h hour(s) and m minute(s)
    where h and m are non-negative integers (fractional minutes should be truncated, e.g. distance of 1 and speed of
    61 results in an arrival time of 0 minutes). Distance and speed are positive integers. Where distance is in miles,
    and speed is in MPH.
    """
    # Note this function will have no return. It just prints the result. Remove the following print statement and add
    # your own code to print the correct values for the given distance and speed. Consider using the remainder (modulus)
    # operator.
    speed_in_minutes = speed / 60
    distance_remaining = distance % speed

    print("Arrival in", distance // speed, "hour(s) and", int(distance_remaining / speed_in_minutes), "minute(s)")


# ********************************************************************************************************************
# Look at, but do not edit code below this point.
# ********************************************************************************************************************
def main():
    # Get data from user
    entered_distance = int(input("Enter distance in miles (must be positive integer)? "))
    entered_speed = int(input("Enter speed in MPH (must be positive integer)? "))

    # Print arrival time
    print_arrival_time(entered_distance, entered_speed)


if __name__ == "__main__":
    main()
