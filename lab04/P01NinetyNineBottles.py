"""Henry B & Fox W"""


def bottle_text(bottles_left):
    """Returns the string "bottle" if bottles_left == 1 and "bottles" otherwise. Bottles_left must be an int >= 0"""
    if bottles_left == 1:
        return "bottle"
    else:
        return "bottles"


def verse(bottles_left, bottles_of_what):
    """Returns a verse of the infamous 99 bottles song as a string when given an integer bottles_left (>0) and string
    bottles_of_what. Each Verse has the form:

    99 bottles of milk on the wall,
    99 bottles of milk,
    Take one down, pass it around,
    98 bottles of milk on the wall!

    In the above example, bottles_left = 99 and bottles_of_what = "milk". Note that there are no leading spaces in
    each verse and the string ends with a newline. Also, the text has to change to the singular bottle when talking
    about 1 bottle.
    """
    result = f"{bottles_left} {bottle_text(bottles_left)} of {bottles_of_what} on the wall,\n"
    result += f"{bottles_left} {bottle_text(bottles_left)} of {bottles_of_what},\n"
    result += "Take one down, pass it around,\n"
    bottles_left -= 1
    result += f"{bottles_left} {bottle_text(bottles_left)} of {bottles_of_what} on the wall!\n"
    return result


def print_song(starting_bottles, bottles_of_what):
    """This is a void function that prints the bottles song starting with the given number of bottles and
    ending with the verse that starts with 1 bottle left. Each verse has a blank line between them, but the last
    verse has no extra blank line i.e. the song ends with a line of the form.
    0 bottles of milk on the wall!
    With a new line after the exclamation point, but no extra blank line. starting_bottles must be an int > 0 and
    bottles_of_what is a string.
    """
    for n in range(starting_bottles, 1, -1):
        print(verse(n, bottles_of_what))
    print(verse(1, bottles_of_what), end="")


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************

# To limit the scope of any variables (i.e. to avoid global variables) we will often we will make a function that holds
# the code to start our program. Some languages this entry point has a special name. In Python, it is traditionally
# named main(). However, we can call it whatever we want.
def main():
    # Get the number of bottles from the user
    starting_bottles = int(input("How many bottles are there: "))

    # Get what is in the bottles
    bottles_of_what = input("What is in the bottles: ")

    # Print the song
    print_song(starting_bottles, bottles_of_what)


# Then we call the main function inside an if statement so that it is only called when this file is run directly.
if __name__ == "__main__":
    main()
