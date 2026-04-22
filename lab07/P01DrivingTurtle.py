"""
Henry B & Fox W
For this project you will be animating some turtle graphics while handling user events. Remember to decompose your
project into functions and use good programming practices. Your program will allow the user to drive a turtle around
the screen. Your program should:

Open a window with the turtle displayed in the center of the window facing east (heading 0) and not moving.
When the user holds the up arrow down the turtle will accelerate (its velocity will increase, but can not go above some
maximum limit you set to keep the animation controllable). The user should not have to tap the up arrow key repeatedly
to accelerate the turtle, just hold it down.
When the user holds the down arrow down the turtle will decelerate (its velocity will decrease, but can not go below 0).
When the user holds the left or right arrows down the turtle will turn in that direction (at a rate you set to keep the
 animation controllable). Again, the user should not have to tap the arrow key repeatedly to turn the turtle, just hold
 it down.
When the turtle hits a wall it bounces off of it (i.e. hitting the left or right edge should negate the x velocity,
hitting the top or bottom edge should negate the y velocity, and hitting a corner should negate both the x and y
velocities).
The turtle leaves a trail behind it as it moves.
After hitting 10 walls (corners count for 2 hits) the window is cleared and the turtle moves back to its starting
state."""
import math
import random
import turtle
from time import sleep

SPEED_MAX = 30
SPEED_MIN = 0
TURN_RATE = 10
WALL_HIT_MAX = 100
SLEEP_TIME = 0.05
REPEAT_TIMER_TIME = 1
BACKGROUND_COLOR = "blue"
PEN_COLOR = "white"
PEN_SIZE = 5
MARGIN = 10
SPEED_CHANGE = 1

# global variables
jerry = turtle.Turtle()
speed = 20
heading = 0
x_velocity = 0
y_velocity = 0
speed_up = False
slow_down = False
turn_left = False
turn_right = False


def get_velocity_x():
    return math.cos(math.radians(heading))


def get_velocity_y():
    return math.sin(math.radians(heading))


def move_dot():
    jerry.pendown()
    jerry.pencolor(PEN_COLOR)
    jerry.pensize(PEN_SIZE)
    global heading
    global x_velocity
    global y_velocity
    screen = jerry.getscreen()
    bounces = 0

    # sets random heading
    heading = random.randint(0, 359)

    x_velocity = get_velocity_x()
    y_velocity = get_velocity_y()

    while bounces < WALL_HIT_MAX:
        x, y = jerry.position()

        if x < -screen.window_width() / 2 or x > screen.window_width() / 2:
            x_velocity *= -1
            bounces += 1
        if y < -screen.window_height() / 2 or y > screen.window_height() / 2:
            y_velocity *= -1
            bounces += 1

        # turtle sleeps
        sleep(SLEEP_TIME)

        # moves to next frame
        jerry.goto(x + x_velocity * speed, y + y_velocity * speed)

        increase_speed()
        decrease_speed()
        turn()

    # moves turtle to beginning
    jerry.penup()
    jerry.goto(0, 0)


def increase_speed():
    global speed
    if speed_up and SPEED_MIN <= speed < SPEED_MAX:
        speed += SPEED_CHANGE


def decrease_speed():
    global speed
    if slow_down and SPEED_MIN < speed <= SPEED_MAX:
        speed -= SPEED_CHANGE


def turn():
    global heading
    global x_velocity
    global y_velocity
    heading = math.degrees(math.atan2(y_velocity, x_velocity))
    if turn_right:
        heading -= TURN_RATE
        x_velocity = get_velocity_x()
        y_velocity = get_velocity_y()
    if turn_left:
        heading += TURN_RATE
        x_velocity = get_velocity_x()
        y_velocity = get_velocity_y()


def on_up_arrow_press():
    global speed_up
    speed_up = True


def on_up_arrow_release():
    global speed_up
    speed_up = False


def on_down_arrow_press():
    global slow_down
    slow_down = True


def on_down_arrow_release():
    global slow_down
    slow_down = False


def on_left_arrow_press():
    global turn_left
    turn_left = True


def on_left_arrow_release():
    global turn_left
    turn_left = False


def on_right_arrow_press():
    global turn_right
    turn_right = True


def on_right_arrow_release():
    global turn_right
    turn_right = False


def main():
    screen = jerry.getscreen()
    screen.bgcolor(BACKGROUND_COLOR)
    jerry.goto(0, 0)
    jerry.hideturtle()

    # Key handlers
    screen.onkeypress(on_up_arrow_press, "Up")
    screen.onkeypress(on_down_arrow_press, "Down")
    screen.onkeypress(on_right_arrow_press, "Right")
    screen.onkeypress(on_left_arrow_press, "Left")
    screen.onkeyrelease(on_up_arrow_release, "Up")
    screen.onkeyrelease(on_down_arrow_release, "Down")
    screen.onkeyrelease(on_right_arrow_release, "Right")
    screen.onkeyrelease(on_left_arrow_release, "Left")

    screen.ontimer(move_dot, REPEAT_TIMER_TIME)

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
