"""
Henry B & Fox W
For this project you will be writing a program that saves the locations of mouse clicks in a file.
Your program should open a turtle graphics window and ask the user for the name of the file to save via a pop-up.
Then it should wait for the user to start clicking. Note the user may resize the window before they start clicking.
When the user first left-clicks the mouse:

Save the width and height of the window in the file (one value per line).
Save the x and y coordinates of the click in the file (one value per line).
Draw a dot at the location of the click.
On all subsequent left-clicks:

Save the x and y coordinates of the click in the file.
Draw a line from the previous click to the current click.
If the user right-clicks the mouse then your program close the file and exit."""
import turtle
import sys

DOT_SIZE = 10
WINDOW_TITLE = "Click Recorder File Name"
POP_UP_WINDOW_PROMPT = "What would you like to name the recorder file? "
NOT_A_LEFT_CLICK = 1
jerry = turtle.Turtle()


# global variables
previous_position = None
file_name = "text"


def record_click(x, y):
    screen = jerry.getscreen()
    global previous_position
    with open(file_name, "a") as file:
        # on the first click
        if previous_position is None:
            file.write(f"{screen.window_width()}" + "\n")
            file.write(f"{screen.window_height()}" + "\n")
            file.write(f"{x}" + "\n")
            file.write(f"{y}" + "\n")
            jerry.penup()
            jerry.goto(x, y)
            jerry.pendown()
            previous_position = "something"
        elif previous_position is not None:
            # on all subsequent clicks after the first
            file.write(f"{x}" + "\n")
            file.write(f"{y}" + "\n")
            jerry.goto(x, y)


def close_window(x, y):
    print(f"fail position:{x} {y} ")
    sys.exit(NOT_A_LEFT_CLICK)


def main():
    global file_name
    screen = jerry.getscreen()
    jerry.hideturtle()
    file_name = screen.textinput(WINDOW_TITLE, POP_UP_WINDOW_PROMPT)

    screen.onclick(record_click, btn=1)
    screen.onclick(close_window, btn=2)
    screen.onclick(close_window, btn=3)

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
