"""Henry B & Fox W"""
import turtle
import random
from time import sleep


def random_color():
    # generate random colors
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_position(my_turtle):
    # generates random position within the window
    my_screen = my_turtle.getscreen()
    width = my_screen.window_width()
    height = my_screen.window_height()
    return random.randint(-1 * (width / 2), width / 2), random.randint(-1 * (height / 2), height / 2)


def random_dot_size(my_turtle):
    # generates random dot sizes
    my_screen = my_turtle.getscreen()
    width = my_screen.window_width()
    height = my_screen.window_height()
    if width / 2 >= height / 2:
        maximum_dot_size = width / 2
    else:
        maximum_dot_size = height / 2
    return random.randint(1, maximum_dot_size)


def draw_dots(my_turtle):
    # draws dots of random size and color
    x, y = random_position(my_turtle)
    my_turtle.goto(x, y)
    my_turtle.dot(random_dot_size(my_turtle), random_color())
    sleep(.2)


def main():
    bob = turtle.Turtle()
    my_screen = bob.getscreen()
    my_screen.colormode(255)
    bob.penup()
    bob.hideturtle()
    while True:
        # continues to draw dots af random sizes and colors until the window is closed
        my_screen.tracer(0)
        draw_dots(bob)
        my_screen.update()


if __name__ == "__main__":
    main()
