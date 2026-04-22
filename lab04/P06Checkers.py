"""Henry B & Fox W"""
import math
import turtle


# Complete the following functions. You may add more functions and constants if you wish. Do not add non-constant
# global variables.
def draw_checker_square(my_turtle, size, square_color):
    """Draws a square filled with the given color with my_turtle (a turtle object). The starting edge of the square will
    be in the current direction of my_turtle. Each side of the square will have length equal to the given size. This
    function has no side effects (i.e. after this function the turtle is left in the same state as it entered)."""
    # turtle goes clockwise around the square and moves to next square start
    my_turtle.pendown()
    my_turtle.fillcolor(square_color)
    my_turtle.begin_fill()
    for n in range(4):
        my_turtle.forward(size)
        my_turtle.right(90)
    my_turtle.forward(size)
    my_turtle.penup()
    my_turtle.end_fill()


def draw_checker(my_turtle, size, checker_color):
    """Draws a checker (dot) of the given color with my_turtle (a turtle object) inside the square of the given size
    (note this function only draws the checker (dot) not the square). my_turtle must be at the starting corner of the
    square the dot is to be placed in, with the starting edge of the square in line with the current direction of
    my_turtle. This function has no side effects (i.e. after this function my_turtle is left in the same state as it
    entered)."""
    # makes the checker inside the square and returns to original position
    my_turtle.penup()
    my_turtle.back(size / 2)
    my_turtle.right(90)
    my_turtle.forward(size / 2)
    my_turtle.dot(CHECKER_SIZE * size, checker_color)
    my_turtle.left(180)
    my_turtle.forward(size / 2)
    my_turtle.right(90)
    my_turtle.forward(size / 2)


def move_to_next_row(my_turtle, distance):
    my_turtle.back(GRID_SIZE * distance)
    my_turtle.right(90)
    my_turtle.forward(distance)
    my_turtle.left(90)


def draw_checkerboard(my_turtle, size, square_color1="white", square_color2="black",
                      checker_color1="red", checker_color2="blue"):
    """Draws an GRID_SIZE by GRID_SIZE checkerboard of alternating square_color1 and square_color2 squares. The total
    side length of the board is size. If checker_color1 and checker_color2 are given (i.e. they are not None) then a
    dot of that color will be drawn in the center of squares of square_color2 on the first 3 and last 3 rows. The
    starting edge of the board will be in the current direction of my_turtle. This function has no side effects (i.e.
    after this function the turtle is left in the same state as it entered)."""
    # draw_checker_square(my_turtle, size, square_color1)
    # draw_checker(my_turtle, size, checker_color1)
    # row 1
    block_size = size / GRID_SIZE
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if (row + column) % 2 == 0:
                square_color = square_color1
            else:
                square_color = square_color2
            draw_checker_square(my_turtle, block_size, square_color)
            if (row < ROWS_WITH_CHECKERS and (column + row) % 2 == 1) or (row >= GRID_SIZE - ROWS_WITH_CHECKERS) and \
                    ((column + row) % 2 == 1):
                if row < ROWS_WITH_CHECKERS:
                    checker_color = checker_color1
                else:
                    checker_color = checker_color2
                draw_checker(my_turtle, block_size, checker_color)
        move_to_next_row(my_turtle, block_size)


# You may edit the following constants to change the look of your program.
#
# Size of window
SIZE = 600

# Window title
TITLE = "Checkerboards"

# You may want to turn animation on, adjust the speed, or show the turtles for debugging purposes. However, you should
# turn animation off, set the speed to 0, and hide the turtles before submitting your program.
ANIMATION_ON = False
SPEED = 0
HIDE = True

# The square root of 2 (the fact that I am making this a constant is a bit of a hint about finding the centers of each
# checker square)
SQRT2 = math.sqrt(2)

# How big a checker should be relative to the size of the square
CHECKER_SIZE = 0.8  # 80% of the size of the square

# The number of rows and columns in the checkerboard
GRID_SIZE = 8

ROWS_WITH_CHECKERS = 3


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
    screen.setup(SIZE, SIZE)
    screen.title(TITLE)

    # Create a turtle for each quadrant
    top_left_turtle = turtle.Turtle()
    top_right_turtle = turtle.Turtle()
    bottom_left_turtle = turtle.Turtle()
    bottom_right_turtle = turtle.Turtle()

    # Hide the turtle cursor if desired
    if HIDE:
        # top_left_turtle.hideturtle()
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
    move_turtle(top_left_turtle, -SIZE / 2, SIZE / 2)
    top_right_turtle.setheading(90)
    move_turtle(bottom_left_turtle, -SIZE / 2, -SIZE / 4)
    bottom_left_turtle.setheading(45)
    move_turtle(bottom_right_turtle, SIZE / 4, 0)
    bottom_right_turtle.right(45)

    # Draw the checkerboards
    draw_checkerboard(top_left_turtle, SIZE / 2)
    draw_checkerboard(top_right_turtle, SIZE / 2, "yellow", "green", "red", "white")
    draw_checkerboard(bottom_left_turtle, SIZE / 2 / SQRT2, "blue", "orange", "purple", "pink")
    draw_checkerboard(bottom_right_turtle, SIZE / 2 / SQRT2, "red", "white", "blue", "green")

    # update the screen
    screen.update()

    # Wait for the user to close the window
    screen.exitonclick()


if __name__ == "__main__":
    main()
