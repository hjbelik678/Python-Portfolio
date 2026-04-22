"""Henry B & Fox W"""
# For testing we only import turtle when running this module (not when importing)
import random
import math


if __name__ == "__main__":
    import turtle


def is_home(my_turtle):
    """Returns True if my_turtle is close to the home position (i.e. the distance to (0, 0) is less than half of
    STEP_SIZE). We do not test to see if the distance is exactly 0 or if each coordinates is exactly 0 as turtles use
    floats for their x and y coordinates and floats are approximate values. my_turtle is a turtle object."""
    # determines whether turtle has returned to home
    if math.sqrt((my_turtle.xcor() ** 2) + (my_turtle.ycor() ** 2)) < STEP_SIZE / 2:
        return True
    else:
        return False


def is_inside_window(my_turtle):
    """Returns True if my_turtle is currently inside the window. You may assume the window is still WIDTH by HEIGHT
    i.e. the window has not been resized with the mouse. my_turtle is a turtle object."""
    # determines whether of not turtle is outside of screen
    x_coordinate = my_turtle.xcor()
    y_coordinate = my_turtle.ycor()
    if abs(x_coordinate) > (WIDTH / 2):
        return False
    if abs(y_coordinate) > (HEIGHT / 2):
        return False
    return True


def take_step(my_turtle):
    """The given turtle takes a single step. At each step the turtle randomly decides to either go up, down, left, or
    right STEP_SIZE unit(s). my_turtle is a turtle object."""
    number = random.randint(0, 3)
    if number == 0:
        my_turtle.setheading(0.0)
    elif number == 1:
        my_turtle.setheading(90.0)
    elif number == 2:
        my_turtle.setheading(180.0)
    else:
        my_turtle.setheading(270.0)
    # Use the turtle's forward method to move the turtle forward STEP_SIZE units
    my_turtle.forward(STEP_SIZE)


def walk(my_turtle):
    """The given turtle goes on a random walk. At each step the turtle randomly decides to either go up, down, left, or
    right STEP_SIZE unit(s). The walk start at the home position (0,0) and stops if the turtle ever returns home or
    moves outside the window area. my_turtle is a turtle object."""
    take_step(my_turtle)
    while is_inside_window(my_turtle) and not is_home(my_turtle):
        take_step(my_turtle)


# You may edit the following constants to change the look of your program. Note I will test your program with various
# window sizes. You may pick colors you like as long as they are visible.
#
# Size of window
WIDTH = 800
HEIGHT = 600

# Window title
TITLE = "Random Walk"

# Background color
BG_COLOR = "black"

# Pen color
PEN_COLOR = "green"

# Turtle speed (you can change this for testing but set it to 0 for the final program)
SPEED = 0

# The size of each step in the walk (you can change this for testing but set it to 10 for the final program)
STEP_SIZE = 10


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
def main():
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

    # Go for a walk
    walk(bob)

    # Where did the turtle end up?
    if is_home(bob):
        print("The turtle made it home!")
    elif not is_inside_window(bob):
        print("The turtle went outside the area!")
    else:
        print("Something went wrong!")

    # Wait for user to close window
    screen.exitonclick()


if __name__ == "__main__":
    main()
