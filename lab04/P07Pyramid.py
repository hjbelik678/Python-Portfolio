""" Fox W and Henry B"""

import math
import turtle
# Uncomment the following import when you add code that needs it. (hint: you should be using this module)
import random


# Complete the following functions. You may add more functions and constants if you wish. Do not add non-constant
# global variables.
def random_color():
    """Returns a random color as three integers in the range 0-255 (inclusive). The first integer is the red value,
    the second is the green value, and the third is the blue value.
    Returns:
        r, g, b where r, g, and b are integers in the range 0-255 (inclusive)"""
    red_value = random.randrange(0, 255)
    green_value = random.randrange(0, 255)
    blue_value = random.randrange(0, 255)
    color = red_value, green_value, blue_value
    return color


def fill_rectangle(my_turtle, width, height, border_color="black", fill_color="random"):
    """Draw a filled rectangle of the given size. The starting edge will be in the current direction of my_turtle. This
    function has no side effects (i.e. after this function the turtle is left in the same state as it entered).

    Parameters:
        my_turtle (Turtle): the turtle object to draw with
        width (float): the width of the rectangle
        height (float): the height of the rectangle
        border_color: the color of the lines making the border of the rectangle
        fill_color: the color to fill the rectangle with. If block_color is "random" then each block will be filled with
            a random color.

    Returns:
        None """
    if fill_color == "random":
        fill_color = random_color()
    my_turtle.pencolor(border_color)
    my_turtle.pendown()
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    for n in range(2):
        my_turtle.forward(width)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)
    my_turtle.penup()
    my_turtle.end_fill()
    my_turtle.forward(width)


def draw_pyramid(my_turtle, width, height, blocks_in_base, border_color="black", block_color="random"):
    """Draws a pyramid of filled rectangles with my_turtle. my_turtle must be at the starting corner
    of the base of the pyramid facing the direction the base will be drawn. If the pyramid base in on the bottom of
    the window with the pyramid pointing up then my_turtle must be at the bottom left corner of the base with a
    heading of 0. This function has no side effects (i.e. after this function my_turtle is left in the same state as it
    entered).
    Parameters:
        my_turtle (Turtle): the turtle object to draw with
        width (float): the width of the base of the pyramid
        height (flat): the height of the pyramid
        blocks_in_base (int): the number of blocks in the base of the pyramid
        border_color: the color of the lines making the border of the blocks
        block_color: the color to fill the blocks with. If block_color is "random" then each block will be filled with
            a random color.
    """
    # This starter code just draws a single rectangle. This is to help you test
    # your other functions before moving on to finish this function.
    # fill_rectangle(my_turtle, width, height, border_color, block_color)
    width = width / blocks_in_base
    height = height / blocks_in_base
    for n in range(blocks_in_base, 0, -1):
        for _ in range(n):
            fill_rectangle(my_turtle, width, height, border_color, block_color)
        # moves to start of next row
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.right(90)
        my_turtle.back(((n - 1) * width) + width / 2)


# You may edit the following constants to change the look of your program.
#
# Size of window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 618

# Window title
TITLE = "Pyramids"

# You may want to turn animation on, adjust the speed, or show the turtles for debugging purposes. However, you should
# turn animation off, set the speed to 0, and hide the turtles before submitting your program.
ANIMATION_ON = True
SPEED = 0
HIDE = True


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
def move_turtle(my_turtle, x, y):
    """Moves the turtle to the specified position. Without drawing a line."""
    # Save the current pen state
    old_pen_state = my_turtle.isdown()

    # Move the turtle without drawing a line
    my_turtle.penup()
    my_turtle.goto(x, y)

    # Restore the pen state
    if old_pen_state:
        my_turtle.pendown()


def main():
    # Create a turtle window
    screen = turtle.Screen()
    screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    screen.title(TITLE)

    # Set the color mode to RGB, so we can use RGB triples to specify colors
    screen.colormode(255)

    # Create a turtle for each quadrant
    top_left_turtle = turtle.Turtle()
    top_right_turtle = turtle.Turtle()
    bottom_left_turtle = turtle.Turtle()
    bottom_right_turtle = turtle.Turtle()

    # Hide the turtle cursor if desired
    if HIDE:
        top_left_turtle.hideturtle()
        top_right_turtle.hideturtle()
        bottom_left_turtle.hideturtle()
        bottom_right_turtle.hideturtle()

    # Set the turtle speed
    top_left_turtle.speed(SPEED)
    top_right_turtle.speed(SPEED)
    bottom_left_turtle.speed(SPEED)
    bottom_right_turtle.speed(SPEED)

    # Turn animation off if not desired
    if not ANIMATION_ON:
        screen.tracer(0)

    # Move the turtles to the correct starting positions
    move_turtle(top_left_turtle, -WINDOW_WIDTH / 2, 0)
    move_turtle(top_right_turtle, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    top_right_turtle.right(180)
    move_turtle(bottom_left_turtle, -WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 4)
    bottom_left_turtle.right(math.degrees(math.atan(WINDOW_HEIGHT / WINDOW_WIDTH)))
    bottom_right_turtle.right(90)

    # Draw the pyramids
    draw_pyramid(top_left_turtle, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 10, "black", "random")
    draw_pyramid(top_right_turtle, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 8, "tan", "yellow")
    draw_pyramid(bottom_left_turtle, math.sqrt((WINDOW_WIDTH / 4) ** 2 + (WINDOW_HEIGHT / 4) ** 2),
                 WINDOW_HEIGHT / 4, 12, "forestgreen", "pink")
    draw_pyramid(bottom_right_turtle, WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2, 16, "red", "blue")

    # update the screen
    screen.update()

    # Wait for the user to close the window
    screen.exitonclick()


if __name__ == "__main__":
    main()
