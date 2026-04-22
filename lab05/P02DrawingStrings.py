"""Henry B & Fox W"""

import CSM2170Functions
import turtle
TOTAL_DEGREES = 360
ORIGIN = 0, 0
SPEED = 0


def main():
    bob = turtle.Turtle()
    my_screen = bob.getscreen()
    # gets the info from the user
    # converts any captal letters to lowercase
    message = str(my_screen.textinput("Get message", "What would you like typed? ")).lower()
    frequency = int(my_screen.numinput("Get frequency", "How many times do you want this repeated", 2, 1))
    text_color = str(my_screen.textinput("Color", "What color do you want the message to be?"))
    bob.hideturtle()
    # determines which screendimension is the greatest and uses that as the basis for the length of the message
    if my_screen.window_width() >= my_screen.window_height():
        size = my_screen.window_width() / 2
    else:
        size = my_screen.window_height() / 2
    heading = 0
    bob.speed(SPEED)
    bob.pencolor(text_color)
    letter_size = CSM2170Functions.compute_size(message, size)
    for n in range(frequency):
        bob.setheading(heading)
        # draws the letters in the string
        CSM2170Functions.draw_string(bob, message, letter_size)
        bob.penup()
        # bob moves back to the origin and rotates to the next heading
        bob.goto(ORIGIN)
        heading = (n + 1) * (TOTAL_DEGREES / frequency)
        bob.pendown()
    turtle.exitonclick()


if __name__ == "__main__":
    main()
