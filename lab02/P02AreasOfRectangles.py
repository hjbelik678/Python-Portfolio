"""
Authors Henry Belik & Fox Woods
the program compares the size of two imputed rectangles and determines which rectangle, if either, is larger
"""
import sys


def area_of_rectangle(width, height):
    """computes area of a rectangle"""
    area = width * height
    return area


def result(area1, area2):
    """compares the areas of the two rectangles"""
    if area1 > area2:
        return "The first rectangle is larger."
    elif area1 < area2:
        return "The second rectangle is larger."
    elif area1 == area2:
        return "The rectangles have the same area."


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
def prompt_for_positive_int(prompt):
    """Asks the user for a positive int with the given prompt. If the number is not positive the program is
    terminated."""
    # Get the value from the user
    value = int(input(prompt))

    # Halt the program if we were given a bad value.
    if value <= 0:
        print(f"The given number {value} is not positive. Halting.")
        # We exit with a non-zero value to indicate an error. What the error codes mean is up to us.
        sys.exit(1)

    # If the value is good return it
    return value


def main():
    # Get first rectangle from the user
    entered_width = prompt_for_positive_int("Enter the width of the first rectangle: ")
    entered_height = prompt_for_positive_int("Enter the height of the first rectangle: ")

    # Compute the first area
    first_area = area_of_rectangle(entered_width, entered_height)

    # Note we have some repeated code here. When you see that it normally means we should make a function to do the task
    # We will talk about such functions later. For now this type of repeated code is acceptable, just not ideal.
    #
    # Get second rectangle from the user
    entered_width = prompt_for_positive_int("Enter the width of the second rectangle: ")
    entered_height = prompt_for_positive_int("Enter the height of the second rectangle: ")

    # Compute the first area
    second_area = area_of_rectangle(entered_width, entered_height)

    # Print the result
    print(result(first_area, second_area))


if __name__ == "__main__":
    main()
