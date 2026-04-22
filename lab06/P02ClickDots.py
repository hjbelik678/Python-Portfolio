"""Henry B & Fox W"""

import random
import turtle

# Create a turtle as global variable, so it can be used in callback functions
my_turtle = turtle.Turtle()
WIDTH = 800
HEIGHT = 600
TITLE = "Click Dots"


def random_color():
    # returns random color in three RGB color values
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_size():
    """determines needed size of the dot so that the edge will be in contact with the nearest edge of the screen
    return an integer"""
    x = my_turtle.xcor()
    y = my_turtle.ycor()
    my_screen = my_turtle.getscreen()
    return int(2 * min((my_screen.window_width() / 2) - abs(x), (my_screen.window_height() / 2) - abs(y)))


def draw_dot(x, y):
    """draws a dot of:
    determined size
    random color
    in x, y arguments' position"""
    my_turtle.goto(x, y)
    my_turtle.dot(get_size(), random_color())


def main():
    """sets up the screen
        sets up the turtle
        activates click handler
        turns over to main loop"""
    # Setup window with a hidden turtle
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title(TITLE)
    screen.colormode(255)

    # hide turtle
    my_turtle.hideturtle()
    my_turtle.up()

    # Set the turtle speed
    screen.tracer(0)

    # bind click event to draw_dot function
    screen.onclick(draw_dot)

    # Start event loop (must be last line of main)
    screen.mainloop()


if __name__ == "__main__":
    main()
