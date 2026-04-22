"""Henry B & Fox W"""
import turtle
import random
from time import sleep
SLEEP_TIME = 0.1


def random_color():
    # generate random colors
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_position(my_turtle):
    # generates random position within the window
    my_screen = my_turtle.getscreen()
    width = my_screen.window_width()
    height = my_screen.window_height()
    return random.randint(-1 * (width / 2), width / 2), random.randint(-1 * (height / 2), height / 2)


def draw_lines(my_turtle, my_screen, color):
    # draws lines of varying length and random color
    my_turtle.pencolor(color)
    my_screen.tracer(0)
    x, y = random_position(my_turtle)
    my_turtle.goto(x, y)
    my_turtle.pendown()
    x, y = random_position(my_turtle)
    my_turtle.goto(x, y)
    my_turtle.penup()
    my_screen.update()
    sleep(SLEEP_TIME)


def main():
    # continues to draw lines of random length, color and position  until the window is closed
    bob = turtle.Turtle()
    my_screen = bob.getscreen()
    my_screen.colormode(255)
    while True:
        bob.hideturtle()
        draw_lines(bob, my_screen, random_color())


if __name__ == "__main__":
    main()
