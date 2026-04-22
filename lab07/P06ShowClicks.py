"""Henry B & Fox W"""
import turtle

"""For this project you will be writing a program that display the results of file created by P05SaveClicks. 
Your program should ask the user for the name of the file to read with an input command or dialog box. 
Your program should then read the file line by line and draw the lines (no dots) as specified in P05SaveClicks. 
That is, it should read the first two lines to get the width and height of the window. 
Then it should read the rest of the file two lines at a time to get the points of the lines to be drawn.

You can test your program on the example file clicks.txt. 
You must make your own test file and add it to your repository."""

INPUT_QUESTION = "What is ths name of the file? "
INPUT_TITLE = "File name?"


def main():
    jerry = turtle.Turtle()
    screen = turtle.Screen()
    file_name = screen.textinput(INPUT_TITLE, INPUT_QUESTION)
    location_file = open(file_name, "r")

    window_width = int(location_file.readline().strip())
    window_height = int(location_file.readline().strip())

    # sets screen dimensions
    screen.screensize(window_width, window_height)

    x = location_file.readline().strip()
    y = location_file.readline().strip()
    jerry.up()

    while x != "" and y != "":
        jerry.goto(float(x), float(y))
        jerry.pendown()

        x = location_file.readline().strip()
        y = location_file.readline().strip()

    screen.exitonclick()


if __name__ == "__main__":
    main()
