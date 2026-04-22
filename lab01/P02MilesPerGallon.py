"""
CSM 2170: P02MilesPerGallon

A vehicle's miles-per-gallon (MPG) can be calculated with the following formula:
         Miles driven
MPG = -------------------
      Gallons of gas used

Complete this program to ask the user for the number of miles driven and the gallons of gas used. It should calculate
the  vehicle's MPG and display the result. Fractional values should be truncated. If the MPG is 42.2 then just return
and display 42. See Chapter 2 Programming Exercise 7.

Author(s): Fox Woods And Henry Belik
"""


def mpg(miles, gallons):
    """Add docstring for MPG function"""
    return miles//gallons


def main():
    # Get data from the user. Replace the following pass statements with code that
    # completes the task outlined in the comments. A pass statement is a nop
    # ("nop" is short for no operation) that does nothing.
    miles_driven = input("How many miles did you drive? ")
    gallons_of_gas_used = int(input("How many gallons of gas did you use? "))
    miles_driven = int(miles_driven)
    result = mpg(miles_driven, gallons_of_gas_used)
    print("miles per gallon %d" % result)


# ********************************************************************************************************************
# Do not edit code below this point.
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
