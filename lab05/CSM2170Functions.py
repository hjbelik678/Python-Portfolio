"""Henry B & Fox W
A collection of functions for use in our CSM 2170 class.
"""
import math


# *************************************************************************************************
# Module variables and constants
# *************************************************************************************************

# Here are some module level (global) variables for remembering the turtle's location and heading. We
# normally do not want to use global variables if we can help it, and we will see "better" ways of
# doing this later. However, for now this will work for saving and restoring the turtle's location.
# we could save more information about the turtle's state, but we will not do that for now.
saved_turtle_x = 0.0
saved_turtle_y = 0.0
saved_turtle_heading = 0.0
saved_pen_state = True


# *************************************************************************************************
# Turtle state saving and restoring functions
# *************************************************************************************************
def save_turtle_state(my_turtle):
    """
    Saves the given turtle's state (location, heading, pen state).

    Args:
        my_turtle: the turtle whose state should be saved.

    Return:
        None
    """
    # Let Python know that we want to use the module variables (i.e. global
    # variables). Without the use of the global keyword Python would make
    # new local variables that are just visible inside this function. The
    # use of global variables is often considered bad style. Later we will
    # see better ways of achieving effects like this without having to use
    # global variables.
    global saved_turtle_x, saved_turtle_y, saved_turtle_heading, saved_pen_state

    # Store the values in the module level variables.
    saved_turtle_x = my_turtle.xcor()
    saved_turtle_y = my_turtle.ycor()
    saved_turtle_heading = my_turtle.heading()
    saved_pen_state = my_turtle.isdown()


def restore_turtle_state(my_turtle):
    """
    Restores the given turtle to the last saved state.

    Args:
        my_turtle: the turtle whose state should be restored.

    Return:
        None
    """
    my_turtle.up()
    my_turtle.goto(saved_turtle_x, saved_turtle_y)
    my_turtle.setheading(saved_turtle_heading)
    if saved_pen_state:
        my_turtle.down()


# *************************************************************************************************
# Letter drawing functions
#
# Each of these functions draws a letter that fits inside a square of the given size (my_turtle
# starts on the baseline of the letter, facing the direction the letter is to be drawn). When the
# function ends the turtle is in the same state it was in when the function was called (you can
# use the save and restore functions to help with this or move the turtle back there yourself).
# *************************************************************************************************
SQRT2 = math.sqrt(2)
LETTER_SIZE_FACTOR = 10 / 11
SPACE_CORRECTION_FACTOR = 1.1


def draw_a(my_turtle, size):
    """Draws an 'A' composed of the specified size with the given turtle."""

    # Save the turtle's state
    save_turtle_state(my_turtle)

    # Compute the angle to turn for the legs of the A. It is computed from the
    # slope of the line rise = 10, run = 5.
    angle = math.degrees(math.atan2(10, 5))

    # Compute the length of the leg from the Pythagorean Theorem
    leg_length = math.sqrt(size ** 2 + (0.5 * size) ** 2)

    # Compute the length to the crossbar of the A
    bottom_length = math.sqrt((0.4 * size) ** 2 + (0.2 * size) ** 2)

    # Size of the crossbar
    cross_length = size * 0.6

    # Draw first leg
    my_turtle.left(angle)
    my_turtle.forward(leg_length)

    # Draw second leg
    my_turtle.right(2 * angle)
    my_turtle.forward(leg_length)

    # Backup and draw crossbar
    my_turtle.backward(bottom_length)
    my_turtle.left(angle)
    my_turtle.backward(cross_length)

    # Restore the turtle's state
    restore_turtle_state(my_turtle)
    # my_turtle.left(angle)
    # my_turtle.backward(bottom_length)
    #
    # # Turn back to initial
    # my_turtle.right(angle)


def draw_b(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    # draw top hump
    my_turtle.forward(size * 0.8)
    my_turtle.right(45)
    my_turtle.forward(size * 0.1 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.1 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.8)
    # draw bottom hump
    my_turtle.backward(size * 0.8)
    my_turtle.left(135)
    my_turtle.forward(size * 0.2 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.2 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.8)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_c(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(0.3 * size)
    my_turtle.pendown()
    my_turtle.forward(size * 0.4)
    my_turtle.right(45)
    my_turtle.forward(size * 0.3 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.4)
    my_turtle.right(45)
    my_turtle.forward(size * 0.2 * SQRT2)
    my_turtle.penup()
    my_turtle.forward(size * 0.1 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.4)
    my_turtle.right(45)
    my_turtle.pendown()
    my_turtle.forward(size * 0.3 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.4)
    my_turtle.right(45)
    my_turtle.pendown()
    my_turtle.forward(size * 0.3 * SQRT2)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_d(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(size * .7)
    my_turtle.right(45)
    my_turtle.forward(size * .3 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * .4)
    my_turtle.right(45)
    my_turtle.forward(size * .3 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * .7)
    restore_turtle_state(my_turtle)


def draw_e(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size * .6)
    my_turtle.right(90)
    my_turtle.forward(size * .6)
    my_turtle.right(180)
    my_turtle.forward(size * .6)
    my_turtle.right(90)
    my_turtle.forward(size * .4)
    my_turtle.right(90)
    my_turtle.forward(size * .8)
    my_turtle.penup()
    my_turtle.goto(saved_turtle_x, saved_turtle_y)
    my_turtle.pendown()
    my_turtle.forward(size)
    restore_turtle_state(my_turtle)


def draw_f(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size * .6)
    my_turtle.right(90)
    my_turtle.forward(size*.6)
    my_turtle.right(180)
    my_turtle.forward(size*.6)
    my_turtle.right(90)
    my_turtle.forward(size * .4)
    my_turtle.right(90)
    my_turtle.forward(size)
    restore_turtle_state(my_turtle)


def draw_g(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size * .3)
    my_turtle.pendown()
    my_turtle.forward(size * .4)
    my_turtle.right(45)
    my_turtle.forward(size * SQRT2 * .3)
    my_turtle.right(45)
    my_turtle.forward(size * .4)
    my_turtle.right(45)
    my_turtle.forward(size * SQRT2 * .2)
    my_turtle.penup()
    my_turtle.goto(saved_turtle_x, saved_turtle_y)
    my_turtle.left(45)
    my_turtle.forward(size * .3)
    my_turtle.pendown()
    my_turtle.left(135)
    my_turtle.forward(size * .3 * SQRT2)
    my_turtle.backward(size * .3 * SQRT2)
    my_turtle.right(135)
    my_turtle.forward(size*.4)
    my_turtle.left(45)
    my_turtle.forward(size * SQRT2 * .3)
    my_turtle.right(135)
    my_turtle.forward(size*.3)
    my_turtle.backward(size*.6)
    my_turtle.right(90)
    my_turtle.forward(size*.5)
    restore_turtle_state(my_turtle)


def draw_h(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size * .6)
    my_turtle.right(90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(size * .4)
    my_turtle.right(180)
    my_turtle.forward(size)
    my_turtle.penup()
    my_turtle.goto(saved_turtle_x, saved_turtle_y)
    my_turtle.pendown()
    my_turtle.left(180)
    my_turtle.forward(size)
    restore_turtle_state(my_turtle)


def draw_i(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.forward(size * .5)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(size * .4)
    my_turtle.backward(size * .8)
    my_turtle.forward(size*.4)
    my_turtle.penup()
    my_turtle.goto(saved_turtle_x, saved_turtle_y)
    my_turtle.pendown()
    my_turtle.forward(size)
    restore_turtle_state(my_turtle)


def draw_j(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.penup()
    my_turtle.forward(size * .2)
    my_turtle.right(135)
    my_turtle.pendown()
    my_turtle.forward(size * .2 * SQRT2)
    my_turtle.left(45)
    my_turtle.forward(size * .2)
    my_turtle.left(45)
    my_turtle.forward(size * .2 * SQRT2)
    my_turtle.left(45)
    my_turtle.forward(size * .8)
    my_turtle.right(90)
    my_turtle.forward(size * .4)
    my_turtle.backward(size * .8)
    restore_turtle_state(my_turtle)


def draw_k(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size * .3)
    my_turtle.right(45)
    my_turtle.forward(size * .7 * SQRT2)
    my_turtle.backward(size * .4 * SQRT2)
    my_turtle.right(90)
    my_turtle.forward(size * .6 * SQRT2)
    my_turtle.penup()
    my_turtle.goto(saved_turtle_x, saved_turtle_y)
    my_turtle.pendown()
    my_turtle.left(135)
    my_turtle.forward(size)
    restore_turtle_state(my_turtle)


def draw_l(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.forward(size)
    my_turtle.penup()
    my_turtle.goto(saved_turtle_x, saved_turtle_y)
    my_turtle.pendown()
    my_turtle.left(90)
    my_turtle.forward(size)
    restore_turtle_state(my_turtle)


def draw_m(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(135)
    my_turtle.forward(size * .5 * SQRT2)
    my_turtle.left(90)
    my_turtle.forward(size * .5 * SQRT2)
    my_turtle.right(135)
    my_turtle.forward(size)
    restore_turtle_state(my_turtle)


def draw_n(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(135)
    my_turtle.forward(size * SQRT2)
    my_turtle.left(135)
    my_turtle.forward(size)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_o(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.forward(0.3 * size)
    my_turtle.pendown()
    for _ in range(4):
        my_turtle.forward(size * 0.4)
        my_turtle.left(45)
        my_turtle.forward(size * 0.3 * SQRT2)
        my_turtle.left(45)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_p(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(size * 0.8)
    my_turtle.right(45)
    my_turtle.forward(size * 0.2 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.2 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.8)
    my_turtle.left(90)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_q(my_turtle, size):
    save_turtle_state(my_turtle)
    draw_o(my_turtle, size)
    my_turtle.penup()
    my_turtle.forward(size)
    my_turtle.left(135)
    my_turtle.pendown()
    my_turtle.forward(size * 0.4 * SQRT2)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_r(my_turtle, size):
    save_turtle_state(my_turtle)
    draw_p(my_turtle, size)
    my_turtle.penup()
    my_turtle.forward(size)
    my_turtle.left(135)
    my_turtle.pendown()
    my_turtle.forward(size * 0.4 * SQRT2)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_s(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.right(90)
    my_turtle.back(size * 0.3)
    my_turtle.pendown()
    my_turtle.forward(size * 0.1)
    my_turtle.left(45)
    my_turtle.forward(size * 0.2 * SQRT2)
    my_turtle.left(45)
    my_turtle.forward(size * 0.6)
    my_turtle.left(45)
    my_turtle.forward(size * 0.2 * SQRT2)
    my_turtle.left(45)
    my_turtle.forward(size * 0.2)
    my_turtle.left(45)
    my_turtle.forward(size * 0.2 * SQRT2)
    my_turtle.left(45)
    my_turtle.forward(size * 0.6)
    my_turtle.right(45)
    my_turtle.forward(size * 0.1 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.1 * SQRT2)
    my_turtle.right(45)
    my_turtle.forward(size * 0.6)
    my_turtle.right(45)
    my_turtle.forward(size * 0.1 * SQRT2)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_t(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.pendown()
    my_turtle.right(90)
    my_turtle.forward(size)
    my_turtle.back(size / 2)
    my_turtle.right(90)
    my_turtle.forward(size)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_u(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.right(90)
    my_turtle.back(size)
    my_turtle.pendown()
    my_turtle.forward(size * 0.7)
    my_turtle.left(45)
    my_turtle.forward(size * 0.3 * SQRT2)
    my_turtle.left(45)
    my_turtle.forward(size * 0.3)
    my_turtle.left(45)
    my_turtle.forward(size * 0.3 * SQRT2)
    my_turtle.left(45)
    my_turtle.forward(size * 0.7)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_v(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.right(90)
    my_turtle.back(size)
    my_turtle.pendown()
    my_turtle.forward(size * 0.5)
    my_turtle.left(45)
    my_turtle.forward(size * 0.5 * SQRT2)
    my_turtle.left(90)
    my_turtle.forward(size * 0.5 * SQRT2)
    my_turtle.left(45)
    my_turtle.forward(size * 0.5)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_w(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.right(90)
    my_turtle.back(size)
    my_turtle.pendown()
    my_turtle.forward(size)
    my_turtle.left(135)
    my_turtle.forward(size * 0.5 * SQRT2)
    my_turtle.right(90)
    my_turtle.forward(size * 0.5 * SQRT2)
    my_turtle.left(135)
    my_turtle.forward(size)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_x(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.forward(size)
    my_turtle.left(135)
    my_turtle.pendown()
    my_turtle.forward(size * SQRT2)
    my_turtle.penup()
    my_turtle.left(135)
    my_turtle.forward(size)
    my_turtle.left(135)
    my_turtle.pendown()
    my_turtle.forward(size * SQRT2)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_y(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.right(90)
    my_turtle.back(size)
    my_turtle.pendown()
    my_turtle.left(45)
    my_turtle.forward(size * 0.5 * SQRT2)
    my_turtle.left(90)
    my_turtle.forward(size * 0.5 * SQRT2)
    my_turtle.back(size * 0.5 * SQRT2)
    my_turtle.right(135)
    my_turtle.forward(size * 0.5)
    my_turtle.penup()
    restore_turtle_state(my_turtle)


def draw_z(my_turtle, size):
    save_turtle_state(my_turtle)
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.pendown()
    my_turtle.forward(size)
    my_turtle.right(135)
    my_turtle.forward(size * SQRT2)
    my_turtle.left(135)
    my_turtle.forward(size)
    my_turtle.penup()
    my_turtle.backward(size)
    restore_turtle_state(my_turtle)


def draw_space(my_turtle, size):
    my_turtle.penup()
    my_turtle.forward(size)


# *************************************************************************************************
# Other drawing functions
# *************************************************************************************************
def draw_square(my_turtle, size):
    """
    Causes a turtle to draw a square with side length size

    Args:
        my_turtle: the turtle which is to do the drawing
        size: the length of each side of the square

    Returns:
        None
    """
    for _ in range(4):
        my_turtle.forward(size)
        my_turtle.left(90)


def draw_letter(my_turtle, letter, size):
    """
    Draws the given letter.

    Args:
        my_turtle: the turtle to be used for drawing
        letter: the letter to be drawn
        size: the size of the square to draw the letter in

    Returns:
        None
    """
    if letter == "a":
        draw_a(my_turtle, size)
    elif letter == "b":
        draw_b(my_turtle, size)
    elif letter == "c":
        draw_c(my_turtle, size)
    elif letter == "d":
        draw_d(my_turtle, size)
    elif letter == "e":
        draw_e(my_turtle, size)
    elif letter == "f":
        draw_f(my_turtle, size)
    elif letter == "g":
        draw_g(my_turtle, size)
    elif letter == "h":
        draw_h(my_turtle, size)
    elif letter == "i":
        draw_i(my_turtle, size)
    elif letter == "j":
        draw_j(my_turtle, size)
    elif letter == "k":
        draw_k(my_turtle, size)
    elif letter == "l":
        draw_l(my_turtle, size)
    elif letter == "m":
        draw_m(my_turtle, size)
    elif letter == "n":
        draw_n(my_turtle, size)
    elif letter == "o":
        draw_o(my_turtle, size)
    elif letter == "p":
        draw_p(my_turtle, size)
    elif letter == "q":
        draw_q(my_turtle, size)
    elif letter == "r":
        draw_r(my_turtle, size)
    elif letter == "s":
        draw_s(my_turtle, size)
    elif letter == "t":
        draw_t(my_turtle, size)
    elif letter == "u":
        draw_u(my_turtle, size)
    elif letter == "v":
        draw_v(my_turtle, size)
    elif letter == "w":
        draw_w(my_turtle, size)
    elif letter == "x":
        draw_x(my_turtle, size)
    elif letter == "y":
        draw_y(my_turtle, size)
    elif letter == "z":
        draw_z(my_turtle, size)
    elif letter == " ":
        pass
    else:
        draw_square(my_turtle, size)


def draw_string(my_turtle, s, size):
    """
    Causes a turtle to draw a string of letters

    Args:
        my_turtle: the turtle which is to do the drawing
        s: the string of letters to be drawn
        size: the size of each letter

    Returns:
        None
    """
    for letter in s:
        draw_letter(my_turtle, letter, size)
        my_turtle.penup()
        my_turtle.forward(1.1 * size)
        my_turtle.pendown()


def compute_size(text, width):
    """returns the size needed for draw_string(my_turtle, text, size) to fit exactly in the given
    width"""
    word_length = len(text)
    character_size = width / word_length
    letter_size = LETTER_SIZE_FACTOR * character_size
    return letter_size
