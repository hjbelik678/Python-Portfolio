"""Henry B & Fox W"""
import random
import turtle
from time import sleep
SLEEP_TIME = 0.1


def random_color():
    # generate random colors
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_rectangle(my_turtle, width, height, color):
    # draws a rectangle of width and height of a color with a border of the same color it is filled with
    # pen ends up
    # rectangle starts at top left and goes clockwise
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.pencolor(color)
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height)
        my_turtle.right(90)
    my_turtle.end_fill()
    my_turtle.penup()
    sleep(SLEEP_TIME)


def main():
    # hides the turtle and determines dimensions of the screen
    bob = turtle.Turtle()
    my_screen = bob.getscreen()
    bob.hideturtle()
    my_screen.colormode(255)
    width = my_screen.window_width()
    height = my_screen.window_height()
    # asks the user how big the grid should be
    grid_size = int(my_screen.numinput("Grid", "what size of grid do you want?", 10, 1))
    bob.penup()
    bob.goto(-width / 2, height / 2)
    while True:
        # endlessly makes the grid until the window is closed
        for row in range(grid_size):
            # makes all the rows
            for _ in range(grid_size):
                # completes each row
                my_screen.tracer(0)
                draw_rectangle(bob, width / grid_size, height / grid_size, random_color())
                bob.forward(width / grid_size)
                my_screen.update()
            # redetermines the dimensions of the screen
            width = my_screen.window_width()
            height = my_screen.window_height()
            # moves to next row
            bob.goto(-width / 2, (height / 2) - ((row + 1) * height / grid_size))
        bob.goto(-width / 2, height / 2)


if __name__ == "__main__":
    main()
