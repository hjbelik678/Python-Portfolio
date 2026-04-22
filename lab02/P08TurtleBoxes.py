"""
Henry B & Fox W
"""
import turtle

# establishes and names the turtle
bob = turtle.Turtle()
# turtle.setworldcoordinates(-1000, -1000, 1000, 1000)


def make_a_square():
    bob.forward(125)
    bob.left(90)
    bob.forward(125)
    bob.left(90)
    bob.forward(125)
    bob.left(90)
    bob.forward(125)


def main():
    my_screen = turtle.Screen()
    bob.left(45)
    bob.pendown()
    bob.pencolor("red")
    bob.fillcolor("red")
    bob.begin_fill()
    make_a_square()
    bob.end_fill()
    bob.pencolor("green")
    bob.fillcolor("Green")
    bob.begin_fill()
    make_a_square()
    bob.end_fill()
    bob.pencolor("yellow")
    bob.fillcolor("yellow")
    bob.begin_fill()
    make_a_square()
    bob.end_fill()
    bob.pencolor("blue")
    bob.fillcolor("blue")
    bob.begin_fill()
    make_a_square()
    bob.end_fill()
    my_screen.exitonclick()


# ********************************************************************************************************************
# Do not edit code below this point.
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
