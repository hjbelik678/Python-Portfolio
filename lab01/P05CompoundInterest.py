"""
CSM 2170: P05CompoundInterest

You are to make a program to calculate compound interest. Your program must ask the user to input:

* The amount of the principle originally deposited as a non-negative float (e.g. 1013.56 for $1013.56 or whatever
  currency the account is in)
* The annual interest rate as a percentage (a float) (e.g. the user would type 3.15 for 3.15% which will need to
  be converted into the decimal .0315 for the calculation)
* The number of times per year the interest is compounded as a positive integer
* The number of years the account will earn interest as a positive integer

Then the program should calculate and display the amount of money that will be in the account after the specified
number of years. See Chapter 2 Programming Exercise 14 for more details and the formula for this type of compound
interest.d

Author(s): Fox Woods and Henry B
"""


def future_value(principle, rate, times_compounded_per_year, years):
    time = times_compounded_per_year * years

    compound_interest = principle * (1 + ((rate/100)/times_compounded_per_year)) ** time

    return compound_interest


def main():
    # Replace this pass statement with code that completes this project
    principle_from_user = float(input('Enter Principle: '))
    interest_rate_from_user = float(input('Enter Interest Rate: '))
    number_of_times_per_year_from_user = int(input('Enter Times Per Year Compounding: '))
    number_of_years_from_user = int(input('Enter Number of Years In the Bank: '))

    result = future_value(principle_from_user, interest_rate_from_user, number_of_times_per_year_from_user,
                          number_of_years_from_user)

    print(f'The compound interest is ${result:.2f}')

# ********************************************************************************************************************
# Do not edit code below this point.
# ********************************************************************************************************************


if __name__ == "__main__":
    main()
