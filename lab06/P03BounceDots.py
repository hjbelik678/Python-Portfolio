"""Henry B & Fox W"""

from time import sleep
import random
import turtle
import math

DOT_SPEED = 10
DOT_SIZE = 40
SLEEP_TIME = 0.03
WIDTH = 800
HEIGHT = 600
TITLE = "Bounce Dots"


def is_in_window(my_turtle):
    # Get the screen from the turtle
    my_screen = my_turtle.getscreen()

    # Get the screen limits
    left_bound = -my_screen.window_width() / 2
    right_bound = my_screen.window_width() / 2
    top_bound = my_screen.window_height() / 2
    bottom_bound = -my_screen.window_height() / 2

    # Get the turtle's position
    x = my_turtle.xcor()
    y = my_turtle.ycor()

    if x > 0 and y > 0:
        # for quad 1
        return x + DOT_SIZE / 2 <= right_bound and y + DOT_SIZE / 2 <= top_bound
    elif y < 0 < x:
        # for quad 4
        return x + DOT_SIZE / 2 <= right_bound and bottom_bound <= y - DOT_SIZE / 2
    elif x < 0 < y:
        # for quad 2
        return left_bound <= x - DOT_SIZE / 2 and y + DOT_SIZE / 2 <= top_bound
    else:
        # for quad 3
        return left_bound <= x - DOT_SIZE / 2 and bottom_bound <= y - DOT_SIZE / 2


def dot_color(my_screen, x_coordinate, y_coordinate):
    if (x_coordinate - (DOT_SIZE / 2)) <= -my_screen.window_width() / 2 and (y_coordinate - (DOT_SIZE / 2)) < \
            y_coordinate < (y_coordinate + (DOT_SIZE / 2)):
        # hits left edge only, turns red
        return "red"
    elif (x_coordinate + (DOT_SIZE / 2)) >= my_screen.window_width() / 2 and (y_coordinate - (DOT_SIZE / 2)) < \
            y_coordinate < (y_coordinate + (DOT_SIZE / 2)):
        # hits right edge only, turns green
        return "green"
    elif (y_coordinate + (DOT_SIZE / 2)) >= my_screen.window_height() / 2 and (x_coordinate - (DOT_SIZE / 2)) < \
            x_coordinate < (x_coordinate + (DOT_SIZE / 2)):
        # hits top edge only, turn blue
        return "blue"
    elif (y_coordinate - (DOT_SIZE / 2)) <= -my_screen.window_height() / 2 and (x_coordinate - (DOT_SIZE / 2)) < \
            x_coordinate < (x_coordinate + (DOT_SIZE / 2)):
        # hits bottom edge only, turn yellow
        return "yellow"
    else:
        return "purple"


def direction(color):
    """purpose of this function is to determine how the velocity vector will change based on which side or if it hits
    a corner"""
    if color == "red" or color == "green":
        # if dot hits right or left edge
        # multiply x velocity by -1
        return 0
    if color == "blue" or color == "yellow":
        # if dot hits top or bottom edge
        # multiply y velocity by -1
        return 1
    if color == "purple":
        # if dot hits a corner
        # multiply x and y velocity by -1
        return 2


def animation(my_turtle, velocity_x, velocity_y):
    """uses velocity to animate the turtle"""
    # Get the screen from the turtle
    my_screen = my_turtle.getscreen()

    # Pick the pen up, so we can move the turtle around with no drawing (going to use dots for actual drawing)
    my_turtle.penup()
    while is_in_window(my_turtle):

        # Move the turtle by the velocity
        my_turtle.goto(my_turtle.xcor() + velocity_x, my_turtle.ycor() + velocity_y)

        # Draw new frame
        my_turtle.dot(DOT_SIZE)

        # Display the frame
        my_screen.update()

        # Sleep for a bit
        sleep(SLEEP_TIME)

        # Clear old frame
        my_turtle.clear()


def main():
    # Create a turtle window
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title(TITLE)

    # Create a turtle
    bob = turtle.Turtle()
    bob.hideturtle()

    # set color
    bob.pencolor("black")

    # Set the turtle speed
    bob.speed(0)

    # Turn animation off (we are going to do it manually)
    screen.tracer(0)
    while True:
        # assigns random direction
        angle = random.randint(0, 359)

        # assigns the velocities
        velocity_x = DOT_SPEED * math.cos(math.radians(angle))
        velocity_y = DOT_SPEED * math.sin(math.radians(angle))
        bounces = 0
        while bounces < 200:
            animation(bob, velocity_x, velocity_y)
            x_coordinate = bob.xcor()
            y_coordinate = bob.ycor()
            bob.pencolor(dot_color(screen, x_coordinate, y_coordinate))
            if direction(bob.pencolor()) == 0:
                velocity_x *= -1
                bounces += 1
            elif direction(bob.pencolor()) == 1:
                velocity_y *= -1
                bounces += 1
            elif direction(bob.pencolor()) == 2:
                velocity_x *= -1
                velocity_y *= -1
                bounces += 2
            # make a move using the nex velocities
            bob.goto(bob.xcor() + velocity_x, bob.ycor() + velocity_y)
        bob.goto(0, 0)


if __name__ == "__main__":
    main()
