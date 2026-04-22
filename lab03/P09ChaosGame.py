"""Henry B & Fox W"""
import turtle
import random

X_COORDINATE_GREEN = 0
Y_COORDINATE_GREEN = 200
X_COORDINATE_BLUE = -300
Y_COORDINATE_BLUE = -200
X_COORDINATE_RED = 300
Y_COORDINATE_RED = -200
REFERENCE_DOT_SIZE = 5
GREEN = 1
BLUE = 2
RED = 3


screen = turtle.Screen()
bob = turtle.Turtle()
screen.setup(800, 600)
screen.title("Chaos Game")


def make_dot(x_position, y_position, size, color):
    # makes dot of inputted position, size and color
    bob.penup()
    bob.setposition(x_position, y_position)
    bob.pendown()
    bob.dot(size, color)


def midpoint(dimension_1, dimension_2):
    # finds the midpoint
    return (dimension_1 + dimension_2) / 2


def next_dot():
    # picks random point for reference
    dot = random.randint(1, 3)
    # gets coordinates of current position
    x_coordinate = bob.xcor()
    y_coordinate = bob.ycor()
    # moves to the midpoint of current location and randomly selected point
    if dot == GREEN:
        new_x_coordinate = midpoint(x_coordinate, X_COORDINATE_GREEN)
        new_y_coordinate = midpoint(y_coordinate, Y_COORDINATE_GREEN)
        make_dot(new_x_coordinate, new_y_coordinate, 2, "green")
    if dot == BLUE:
        new_x_coordinate = midpoint(x_coordinate, X_COORDINATE_BLUE)
        new_y_coordinate = midpoint(y_coordinate, Y_COORDINATE_BLUE)
        make_dot(new_x_coordinate, new_y_coordinate, 2, "blue")
    if dot == RED:
        new_x_coordinate = midpoint(x_coordinate, X_COORDINATE_RED)
        new_y_coordinate = midpoint(y_coordinate, Y_COORDINATE_RED)
        make_dot(new_x_coordinate, new_y_coordinate, 2, "red")


def main():
    n = int(input("How many points do you want? "))
    # makes three initial points
    make_dot(X_COORDINATE_GREEN, Y_COORDINATE_GREEN, REFERENCE_DOT_SIZE, "green")
    make_dot(X_COORDINATE_RED, Y_COORDINATE_BLUE, REFERENCE_DOT_SIZE, "blue")
    make_dot(X_COORDINATE_RED, Y_COORDINATE_RED, REFERENCE_DOT_SIZE, "red")
    # stops animation
    screen.tracer(0, 0)
    # makes a dot at random starting point
    make_dot(random.randint(-400, 400), random.randint(-300, 300), 2, "black")
    for _ in range(n):
        next_dot()
    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
