"""Henry B & Fox W
!wrote this program while trying not to use global variables!"""
import math
import turtle


def calculate_beta_angle(distance, outside_edge, correction_factor):
    """calculate the angle of the triangle between the second and third sides
    the "beta" angle on the read me
    correctly sized with a correction factor"""
    angle = math.atan2(math.sqrt(distance) * correction_factor, outside_edge * correction_factor)
    return math.degrees(angle)


def draw_triangle(my_turtle, distance, outside, correction_factor, inside_color, outside_color):
    """draws a triangle with the first and third legs are the inside color
    these two legs depend on the distance parameter
    second leg is the outside color
    this leg is constant throughout the spiral, only being change by the correction factor
    correction factor sizes the triangle to be visible on the screen"""
    my_turtle.pencolor(inside_color)
    my_turtle.forward(correction_factor * math.sqrt(distance))
    my_turtle.left(90)
    my_turtle.pencolor(outside_color)
    my_turtle.forward(outside * correction_factor)
    my_turtle.left(180 - calculate_beta_angle(distance, outside, correction_factor))
    my_turtle.pencolor(inside_color)
    my_turtle.forward(math.sqrt(distance + 1) * correction_factor)
    my_turtle.right(180)


def main():
    """sets up turtle and screen
    sets initial heading
    puts pen down
    gives base outside edge value"""
    my_turtle = turtle.Turtle()
    screen = turtle.Screen()

    # set speed
    my_turtle.speed(0)

    # give heading
    heading = 0.0
    my_turtle.pendown()
    outside_edge = 1

    # get input from the user
    number_of_triangles = int(screen.numinput("Spiral of Theodorus", "How many triangles? ", 5))
    inside_color = screen.textinput("color", "what color would you like the inside of the spiral to be? ")
    outside_color = screen.textinput("color", "what color would you like the outside of the spiral to be? ")

    # sized to show up on the screen and be seen easily
    size_correction_factor = 40
    for n in range(1, 1 + number_of_triangles):
        # draws the spiral and uses the heading to change angle
        my_turtle.setheading(heading)
        draw_triangle(my_turtle, n, outside_edge, size_correction_factor, inside_color, outside_color)
        # adjusts the heading based on the "read me" alpha angle
        heading += math.degrees(math.atan2(1, math.sqrt(n)))
    screen.exitonclick()


if __name__ == "__main__":
    main()
