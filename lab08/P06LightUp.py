# Authors Fox W and Henry B
import turtle

# Constants
GRID_SIZE = 25
CELL_SIZE = 20
WINDOW_WIDTH = GRID_SIZE * CELL_SIZE
WINDOW_HEIGHT = GRID_SIZE * CELL_SIZE

# Create the 2D list to store the state of each cell
grid = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


# Function to toggle the state of a cell and draw it
def toggle_cell(x, y):
    # Calculate the grid indices of the clicked cell
    row = int(y // CELL_SIZE)
    col = int(x // CELL_SIZE)

    # Toggle the state of the clicked cell
    grid[row][col] = not grid[row][col]

    # Move the turtle to the center of the clicked cell
    turtle.penup()
    turtle.goto(col * CELL_SIZE + CELL_SIZE/2, row * CELL_SIZE + CELL_SIZE/2)
    turtle.pendown()

    # Draw the cell according to its state
    if grid[row][col]:
        turtle.fillcolor('black')
    else:
        turtle.fillcolor('white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(CELL_SIZE)
        turtle.right(90)
    turtle.end_fill()


# Set up the turtle
turtle.speed(0)
turtle.penup()
turtle.setposition(-WINDOW_WIDTH/2, -WINDOW_HEIGHT/2)

# Draw the grid
for i in range(GRID_SIZE + 1):
    turtle.setposition(-WINDOW_WIDTH/2, -WINDOW_HEIGHT/2 + i*CELL_SIZE)
    turtle.pendown()
    turtle.forward(WINDOW_WIDTH)
    turtle.penup()

for i in range(GRID_SIZE + 1):
    turtle.setposition(-WINDOW_WIDTH/2 + i*CELL_SIZE, -WINDOW_HEIGHT/2)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(WINDOW_HEIGHT)
    turtle.right(90)
    turtle.penup()

# Set up the event handler
turtle.onscreenclick(toggle_cell)

# Start the main loop
turtle.mainloop()
