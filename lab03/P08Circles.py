import turtle

# Henry B & Fox W

# Window size (change the size to something that works well for your system). Your code should work
# for any size that would be visible.
WINDOW_SIZE = 800
INITIAL_DIAMETER = 700


def main():
    # Make a turtle
    bob = turtle.Turtle()
    bob.speed(0)  # Keep speed 0 or draw off-screen for fast rendering
    bob.hideturtle()
    # Set the window size
    screen = turtle.Screen()
    screen.setup(width=WINDOW_SIZE, height=WINDOW_SIZE)
    initial_diameter = INITIAL_DIAMETER // 2
    color_value = 0
    diameter = WINDOW_SIZE

    while diameter > 1:
        # alternates colors
        if color_value % 2 == 0:
            color = "blue"
        else:
            color = "green"
        bob.dot(diameter, color)
        diameter -= initial_diameter * 0.1
        color_value = color_value + 1
    # Keep the screen open
    screen.exitonclick()


if __name__ == "__main__":
    main()
