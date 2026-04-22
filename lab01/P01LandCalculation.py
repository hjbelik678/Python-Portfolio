"""
This is a documentation string (or docstring). Docstrings are a convenient way of associating documentation with
Python modules, functions, classes, and methods. As this docstring is at the start of our file it is documentation for
the entire module. All of your files (modules) should have a docstring that gives a high level overview of what the
module does.

CSM 2170: P01LandCalculation

One acre of land is equivalent to 43,560 square feet. Complete this program so that it asks the user to enter the
total square feet in a tract of land and calculates the number of acres in the tract. Fractional acres are truncated
i.e. only output the number of whole acres. You may assume the input is a non-negative number. See Chapter 2
Programming Exercise 3.

Author(s): Fox Woods and Henry Belik
"""

# A constant for the number of square feet in an acre
SQUARE_FEET_PER_ACRE = 43560


def land_calculation(square_feet):
    """This doc string is at the start of a function, so it documents the function.
    Computes the number of whole acres in a given number of square feet. Assumes square_feet is a non-negative
    number."""
    acres = square_feet // SQUARE_FEET_PER_ACRE
    return acres


# ********************************************************************************************************************
# Look at, but do not edit code below this point.
# Note there are ways to do this in less code. However, the focus is on readability while also showing that types can
# change.
# ********************************************************************************************************************
# To limit the scope of any variables (i.e. to avoid global variables) we will often we will make a function that holds
# the code to start our program. Some languages this entry point has a special name. In Python, it is traditionally
# named main(). However, we can call it whatever we want.
def main():
    # Get data from the user
    size_of_tract = input('Enter tract size in square feet? ')

    # Covert into an int
    size_of_tract = int(size_of_tract)

    # Compute number of acres
    size_of_tract = land_calculation(size_of_tract)

    # Print result (%d is a placeholder for an int, while the % after the string gives the replacement)
    print("The tract is %d whole acre(s)." % size_of_tract)


# This if statement makes sure that the code does not run when the module is imported. We will talk about if statements
# in detail later.
if __name__ == "__main__":
    main()
