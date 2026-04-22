"""Henry B & Fox W"""
import math
import turtle
import CSM2170Functions
import string
from time import sleep
SAVE_TURTLE_STATE = turtle.pendown
SAVE_TURTLE_HEADING = 90
SAVE_TURTLE_POSITION = turtle.position()
SQRT2 = math.sqrt(2)

# *************************************************************************************************
# You may edit this file for testing but revert it back to the original code for your
# final submission.
# *************************************************************************************************


def letter_tests():
    # You may edit the following constants to change the look of your program.
    # Size of window
    window_width = 1100
    window_height = 800
    letter_size = 70

    # Amount of each rotation
    rotation_amount = 360 / 100

    # Window title
    title = "CSM2170FunctionTests"

    # You may want to turn animation on, adjust the speed, or show the turtles for debugging purposes.
    animation_on = False
    speed = 0
    hide = True
    rotation_on = True

    # Create a turtle window
    screen = turtle.Screen()
    screen.setup(window_width, window_height)
    screen.title(title)

    # Create a turtle
    bob = turtle.Turtle()

    # Hide the turtle cursor if desired
    if hide:
        bob.hideturtle()

    # Set the turtle speed
    bob.speed(speed)

    # Turn animation off if not desired
    if not animation_on:
        screen.tracer(0)

    # the linter does not understand that we are using metaprogramming to access the functions so here is function call
    # to make it happy. Normally I would just turn off the erroneous warning, but I want to make sure you see all of the
    # linter messages for your own code.
    CSM2170Functions.compute_size("A", window_width)

    while True:
        # Move the turtle to the correct starting position
        bob.up()
        bob.backward(14 * 1.1 * letter_size / 2)
        bob.down()

        # Draw all the letters
        for letter in string.ascii_lowercase + 'ab':
            # Draw the letter with some metaprogramming. Note using exec can be very dangerous (especially if you are
            # using user input).
            exec("CSM2170Functions.draw_" + letter + "(bob, letter_size)")

            # Move the turtle to the correct starting position for the next letter
            bob.up()
            bob.forward(1.1 * letter_size)
            bob.down()

            if letter == "n":
                bob.up()
                bob.backward(14 * 1.1 * letter_size)
                bob.right(90)
                bob.forward(1.1 * letter_size)
                bob.left(90)
                bob.down()

        # Update the screen
        screen.update()
        sleep(.05)
        bob.clear()
        bob.up()
        bob.setposition(0, 0)
        bob.down()
        if rotation_on:
            bob.left(rotation_amount)


if __name__ == "__main__":
    letter_tests()
