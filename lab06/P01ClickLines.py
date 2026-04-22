"""Henry B & Fox W"""

import turtle

TITLE = "Click Lines"
DOT_SIZE = 5

# Create a turtle as global variable, so it can be used in callback functions
my_turtle = turtle.Turtle()


def on_click_one(x, y):
    """turtle moves to first click and makes a dot
    activates second click handler to go to next dot
    begins with pen up
    ends with pen down"""
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.dot(DOT_SIZE)
    my_screen = my_turtle.getscreen()
    my_screen.onclick(on_click_two, add=False)


def on_click_two(x, y):
    """draws a line on its path from the first dot and another dot at the finishing point
    begins with pen down
    ends with the pen up
    activates first click handler"""
    my_turtle.goto(x, y)
    my_turtle.dot(DOT_SIZE)
    my_turtle.penup()
    my_screen = my_turtle.getscreen()
    my_screen.onclick(on_click_one, add=False)


def main():
    """sets up the screen
    sets up the turtle
    activates first click handler
    turns over to main loop"""
    # Setup window with a hidden turtle
    my_screen = turtle.Screen()
    my_screen.window_width()
    my_screen.setup(my_screen.window_width(), my_screen.window_height())
    my_screen.title(TITLE)
    my_screen.bgcolor("black")

    # Turn off animation
    my_turtle.speed(0)
    my_screen.tracer(0)

    # Set the turtle color and size
    my_turtle.color("green")

    # get the turtle to the right pen state
    my_turtle.penup()

    # Bind click event to on_click function
    my_screen.onclick(on_click_one, add=False)

    # Start event loop (must be last line of main)
    my_screen.mainloop()


if __name__ == "__main__":
    main()
