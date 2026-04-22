"""Henry B & Fox W"""
import turtle
MARGIN = 5


# Complete the following functions to draw our line pattern. You may add more functions and constants if you wish.
# Do not add non-constant global variables.
def draw_line(my_turtle, starting_x, starting_y, ending_x, ending_y):
    """Draws a line from (starting_x, starting_y) to (ending_x, ending_y) without drawing anything else. my_turtle is a
    turtle object."""
    my_turtle.penup()
    my_turtle.goto(starting_x, starting_y)
    my_turtle.pendown()
    my_turtle.goto(ending_x, ending_y)
    my_turtle.penup()


def draw_pattern(my_turtle, number_of_lines):
    """Draws our line pattern with the given number of lines. my_turtle is a turtle object and number_of_lines is an
    int >= 2"""
    # bottom left pattern
    my_turtle.penup()
    my_turtle.goto(-((WIDTH / 2) - MARGIN), (HEIGHT / 2) - MARGIN)
    end_x = -((WIDTH / 2) - MARGIN)
    end_y = -((HEIGHT / 2) - MARGIN)
    for _ in range(number_of_lines):
        current_x = my_turtle.xcor()
        current_y = my_turtle.ycor()
        draw_line(my_turtle, current_x, current_y, end_x, end_y)
        end_x += (WIDTH - 2 * MARGIN) / (number_of_lines - 1)
        current_y -= (HEIGHT - 2 * MARGIN) / (number_of_lines - 1)
        my_turtle.goto(current_x, current_y)
    # top right pattern
    my_turtle.penup()
    my_turtle.goto((WIDTH / 2) - MARGIN, -((HEIGHT / 2) - MARGIN))
    end_x = (WIDTH / 2) - MARGIN
    end_y = (HEIGHT / 2) - MARGIN
    for _ in range(number_of_lines):
        current_x = my_turtle.xcor()
        current_y = my_turtle.ycor()
        draw_line(my_turtle, current_x, current_y, end_x, end_y)
        end_x -= (WIDTH - 2 * MARGIN) / (number_of_lines - 1)
        current_y += (HEIGHT - 2 * MARGIN) / (number_of_lines - 1)
        my_turtle.goto(current_x, current_y)


# You may edit the following constants to change the look of your program. Note I will test your program with various
# window sizes. You may pick colors you like as long as they are visible.
#
# Size of window
WIDTH = 800
HEIGHT = 600

# Window title
TITLE = "Line Pattern"

# Background color
BG_COLOR = "black"

# Pen color
PEN_COLOR = "green"

# Turtle speed
SPEED = 0


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
def main():
    # Ask the user for the number of lines
    lines = int(input("How many lines: "))

    # Set up the window
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title(TITLE)

    # Make a turtle
    bob = turtle.Turtle()

    # Set the colors and speed, and hide the turtle
    screen.bgcolor(BG_COLOR)
    bob.color(PEN_COLOR)
    bob.speed(SPEED)
    bob.hideturtle()

    # Draw the line
    draw_pattern(bob, lines)

    # Wait for user to close window
    screen.exitonclick()


if __name__ == "__main__":
    main()
