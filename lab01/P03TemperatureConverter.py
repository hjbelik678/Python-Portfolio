"""
CSM 2170: P03TemperatureConverter

Complete this program to ask the user for the temperature in Celsius and convert it to Fahrenheit. The calculation
should be done as a float but when printing only display 2 digits after the decimal point. See Chapter 2 Programming
Exercise 9.
     9
F = --- C + 32
     5

Author(s): (Henry Belik Fox Woods)
"""


def celsius_to_fahrenheit(celsius):
    """add docstring"""
    # Replace the following return with one that completes the function
    fahrenheit = ((9.0 / 5.0) * celsius) + 32

    return fahrenheit


def main():
    # Replace the pass statements with code to complete the main function
    # Get temperature from the user
    celsius_from_user = float(input('Enter celsius you want to convert to fahrenheit? '))

    # Convert value to Fahrenheit with your celsius_to_fahrenheit function
    result = celsius_to_fahrenheit(celsius_from_user)

    print("Your input celsius has been converted to fahrenheit and is now %2d " % result)

    # Display result with only 2 digits after the decimal point


# ********************************************************************************************************************
# Do not edit code below this point.
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
