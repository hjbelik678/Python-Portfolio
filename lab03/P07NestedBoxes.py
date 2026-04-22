import turtle

# Henry B & Fox W

# Window size and margin (change the sizes to something that works well for your system). Your code
# should work for any size that would be visible.
WINDOW_SIZE = 800
MARGIN = 25
MAX_SIDE_LENGTH = 750
bob = turtle.Turtle()
bob.speed(0)
# Keep speed 0 or draw off-screen for fast rendering
screen = turtle.Screen()
screen.setup(width=WINDOW_SIZE, height=WINDOW_SIZE)


def make_a_box(side_length):
    # makes a box
    i = 1
    while i in range(5):
        bob.forward(side_length)
        bob.left(90)
        i += 1


def main():
    # Move the turtle to the bottom left of the window
    bob.penup()
    bob.setposition(-(WINDOW_SIZE - MARGIN) / 2, -(WINDOW_SIZE - 2 * MARGIN) / 2)
    bob.pendown()
    bob.hideturtle()
    # sets initial side length to 1% of the max side length
    side = MAX_SIDE_LENGTH // 100
    bob.pendown()
    # draws squares with increasing side length
    while side in range(MAX_SIDE_LENGTH + 1):
        make_a_box(side)
        # adds 1% of the max side length each time
        side += MAX_SIDE_LENGTH // 100
    # Set the window size
    screen.setup(width=WINDOW_SIZE, height=WINDOW_SIZE)
    # Keep the screen open
    screen.exitonclick()


if __name__ == "__main__":
    main()
