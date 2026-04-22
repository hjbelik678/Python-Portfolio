[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/gk90xnY6)
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/gk90xnY6)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10766270)
# Lab07

![ ](../../actions/workflows/linter.yml/badge.svg)

## Overview

From now on your programs should handle erroneous inputs. If the user enters values that are not valid,
recover from the error and ask the user to enter a valid value. If the error comes from a file, print
an error message and exit the program. In any case, your programs should not crash.

## P01: Driving Turtle (15 points)

For this project you will be animating some turtle graphics while handling user events. Remember to
decompose your project into functions and use good programming practices. Your program will allow the
user to drive a turtle around the screen. Your program should:

* Open a window with the turtle displayed in the center of the window facing east (heading 0) and not
  moving.
* When the user holds the up arrow down the turtle will accelerate (its velocity will increase, but can
  not go above some maximum limit you set to keep the animation controllable). The user should not have 
  to tap the up arrow key repeatedly to accelerate the turtle, just hold it down. 
* When the user holds the down arrow down the turtle will decelerate (its velocity will decrease, but
  can not go below 0).
* When the user holds the left or right arrows down the turtle will turn in that direction (at a rate
  you set to keep the animation controllable). Again, the user should not have to tap the arrow key
  repeatedly to turn the turtle, just hold it down.
* When the turtle hits a wall it bounces off of it (i.e. hitting the left or right edge should negate
  the x velocity, hitting the top or bottom edge should negate the y velocity, and hitting a corner
  should negate both the x and y velocities).
* The turtle leaves a trail behind it as it moves.
* After hitting 10 walls (corners count for 2 hits) the window is cleared and the turtle moves back to
  its starting state.

## Hints

* Use `screen.ontimer` to schedule animation updates.
* Use `screen.onkeypress` to set a boolean variable when the user holds down an arrow key.
* Use `screen.onkeyrelease` to clear a boolean variable when the user releases an arrow key.
* Check to see if a key is currently pressed in your animation update function by checking the boolean
  variables you set in the key press and release functions.

## P02: Dice Game (20 points)

For this project your will be extending either P04Craps from Lab06 or P03EvenOrOdd from Lab04.
Your program should now start by asking the user for their name. If the user is baned then your program
should print a message to that effect and exit. If the user is not banned then your program should play
the game as normal. A user is baned if their total number of losses is greater than 3 and the number of
losses is greater than 2 times the number of wins. Your program should store the total number of wins
and losses in a file named `dice_game.txt` in the same directory as your program. The file contain
records of the form:

```
USERNAME
WINS
LOSSES
```

For example, if the file contains:

```
Alice
3
4
Bob
2
7
```

Then Alice has won 3 games and lost 4 games and Bob has won 2 games and lost 7 games (and is baned).

Your program should update `dicegame.txt` when the user says they do not want to play anymore. Note the
ban check only done at the start of the game, not after each round, and saving is only done at the end
of the game when the user says they do not want to play anymore.

### Hints

* You can use the `os.path.exists` function to check if a file exists.
* You can use the `os.remove` function to delete a file.
* You can use the `os.rename` function to rename a file.
* See the `modify_coffee_records.py` program from our text for an example of this type of file
  manipulation.
* Use relative paths for your files i.e. `dicegame.txt` will be in the same location as your program.
Absolute paths can change from machine to machine. So unless you know the absolute path will be valid 
for all of your users, we almost always want to use relative paths.

## P03: Random File Generator (10 points)

For this project you will be writing a program that generates files that contain random numbers. Your
program should ask the user for the name of the file to create, the minimum and maximum values for the
random numbers, and the number of random numbers to generate. Your program should then generate the
file with the specified number of random numbers in the specified range with one number per line.

## P04: File Statistics (10 points)

For this project you will be writing a program that reads a file containing numbers and prints out
some statistics about the numbers. Your program should ask the user for the name of the file to read.
Your program should then read the file a line at a time and print out the following statistics in a
nice format:
* The number of lines that were numbers in the file.
* The number of lines that were not numbers in the file. 
* The sum of the lines that were numbers in the file.
* The average of the lines that were numbers in the file.
* The minimum value in the file.
* The maximum value in the file.
* The number of even numbers in the file.

## Hints

* Use files made by Project 03 to test your program.
* See the input example from class on ways to check if a string is a number.
* Remember a file could have no numbers in it.

## P05: Save Clicks (10 points)

For this project you will be writing a program that saves the locations of mouse clicks in a file. Your
program should open a turtle graphics window and ask the user for the name of the file to save via a
pop-up. Then it should wait for the user to start clicking. Note the user may resize the window before
they start clicking. When the user first left-clicks the mouse:

* Save the width and height of the window in the file (one value per line).
* Save the x and y coordinates of the click in the file (one value per line).
* Draw a dot at the location of the click.

On all subsequent left-clicks:

* Save the x and y coordinates of the click in the file.
* Draw a line from the previous click to the current click.

If the user right-clicks the mouse then your program close the file and exit.

## Hints

* `turtle.onclick(fun, btn=1)` will call the function `fun` when the user left-clicks the mouse.
* `turtle.onclick(fun, btn=2)` will call the function `fun` when the user middle-clicks the mouse.
* `turtle.onclick(fun, btn=3)` will call the function `fun` when the user right-clicks the mouse.
* However, right clicks on some track pads are `btn=2`. So bind your closing code to both
  `btn=2` and `btn=3`. 

## P06: Show Clicks (10 points)

For this project you will be writing a program that display the results of file created by
`P05SaveClicks`. Your program should ask the user for the name of the file to read with an input
command or dialog box. Your program should then read the file line by line and draw the lines (no dots) as specified in
`P05SaveClicks`. That is, it should read the first two lines to get the width and height of the window.
Then it should read the rest of the file two lines at a time to get the points of the lines to be drawn.

You can test your program on the example file `clicks.txt`. You must make your own test file and add it
to your repository.

## Coding Style

Your code is not only graded by the automated tests. I will run more tests on
your code and review your code and commits. You are expected to follow good
programming conventions (see [Lab01](https://github.com/EIU-Computer-Science/CSM2170-Lab01)
for more details). Failure to do so will
impact your grade for an assignment. In particular, your code should pass the
linter checks, files should start with a docstring summarizing the project and
giving the names of the team members, and all functions should have a docstring
detailing their behavior.

## Submit your work by pushing it to GitHub

Commit your changes often (at least once per program, but likely many more
times for larger programs). Push when you are done with your work for the
day or have code that you want your partner or me to see. Until you push
your commits, they will only be on your local machine. Note that the
automated tests will run when you push as well. I will grade the last push
to the main branch that is done before the deadline. Commits or pushes done
after the deadline will receive no credit. Check that you can see your code
on GitHub before the deadline.
