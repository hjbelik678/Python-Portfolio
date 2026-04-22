[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/1K65L_yz)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=11000057)
# Lab08

![ ](../../actions/workflows/linter.yml/badge.svg)

## Overview

From now on your programs should handle erroneous inputs. If the user enters values that are not valid,
recover from the error and ask the user to enter a valid value. If the error comes from a file, print an
error message and exit the program. In any case, your programs should not crash.

## P01 Dreaming Again (10 points)

This project is an extension of Project 05: Binary Dream from Lab 03. Now instead of just randomly writing
zeros and ones to the screen, the program will write a _stream_ of random characters down the columns
of the screen. Your program will be controlled by the constants:

* `SYMBOLS`, a list of all the symbols that can be written in a stream.
* `NEW_STREAM_PROBABILITY`, a float in the range [0.0, 1.0] that gives the probability that a new stream
  will be created on a column that does not already have a stream.
* `BASE_STREAM_LENGTH`, an integer that gives the base length of a stream.
* `MAX_STREAM_LENGTH_DELTA`, the amount a stream can differ from the base length. The actual length of a 
  new stream will be a random integer in the range [max(BASE_STREAM_LENGTH - MAX_STREAM_LENGTH_DELTA, 1), 
  BASE_STREAM_LENGTH + MAX_STREAM_LENGTH_DELTA].
* `SLEEP_TIME`, a float that is the number of seconds to sleep between each frame.

You program should:

1. Use `width = shutil.get_terminal_size()[0]` to get the width of the terminal window (you will need to import
  `shutil`).
2. Create a `width` length list of 0's to keep track of the current length of each stream. A 0 in this list means that the
  stream is not active in that column.
3. For each column in the list:
    1. If the stream is active (has a value > 0), write a random symbol from `SYMBOLS` to the screen and decrement the
       stream length.
    2. If the stream is not active (has a value of 0), print a space and see if it becomes active by generating a
       random number in the range [0.0, 1.0) and testing if it is less than `NEW_STREAM_PROBABILITY`. If it is, set the
       new stream length to be a random integer in the range [max(BASE_STREAM_LENGTH - MAX_STREAM_LENGTH_DELTA, 1), 
  BASE_STREAM_LENGTH + MAX_STREAM_LENGTH_DELTA]. Otherwise, leave the stream length 0.
4. Sleep for `SLEEP_TIME` seconds.
5. Goto Step 3.

Select reasonable values, and ones that you find pleasant, for the constants (i.e. do not just leave them as the
defaults I gave).

## P02 Dice Roller (10 points)

In this project you will be making a program that:

* Prompts the user for `number_of_dice`, the number of dice to roll in each test (an integer that is at least 1).
* Prompts the user for `number_of_sides`, the number of sides on each die (an integer that is at least 2).
* Prompts the user for `number_of_tests`, the number of tests to run (an integer that is at least 1).
* Create a list `counts`, initialized to zeros, to count the number of times each possible sum of the dice appears.
  For example, if there are 2 dice with 6 sides, the list would need to be able to count values from 2 to 12. If there
  are 3 dice with 4 sides, the list would need to be able to count values from 3 to 12.
* For `number_of_tests` times:
    1. Roll the requested number of dice with the given number of sides and total the results
    2. Add 1 to the location of `counts` that corresponds to the sum that was rolled
* Use `matplotlib` to create a bar chart of the results. The x-axis should be the possible sums and the y-axis should
  be the number of times that sum was rolled. The title of the graph should be "Rolling X dice with Y sides N times"
  where X, Y, and N are the values the user entered.

Note after the prompts for input your program will not print anything else.

## P03 Government Pie (10 points)

Create a program that visualizes the distribution of the 2021 US Federal Budget as a pie chart with `mathplotlib`. Your
program must get its data from the file [data/budget/budget2021.csv](data/budget/budget2021.csv) and use that data for
the graph's headings and values.

Data sources:
* https://www.govinfo.gov/app/collection/budget/2023/BUDGET-2023-TAB
* https://usgovernmentspending.com

### Hints

* You can use `line.split(',')` to split a line of a CSV file into a list of strings.
* You can also use the `csv` module to read a CSV file. See the 
  [documentation](https://docs.python.org/3/library/csv.html)
  for more information. While this is overkill for this project, it is a good module to know about and will be useful 
  in future projects.

## P04 Gas (10 points)

Create a program for visualizing the price of gas in the US over time. Your program must get its data from the file
[data/gas/gas.csv](data/gas/gas.csv). Prompt the user for the starting and ending years (ending year can be the same as
the starting year) to display and use `matplotlib` to create a graph of the data. It is up to you to design the graph,
but it should be clear, easy to read, and to show how prices have changed over time (i.e. be careful in how you pick the
range for your plot and pick good labels).

Data source: [U.S. Energy Information Administration](https://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_nus_w.htm)

### Hints

* See the hints for Project 03 for how to read a CSV file.
* Note the first line of the file is heading information.
* You can use date.split('/') to split a date string of the form "month/day/year" (this way of writing dates never made
  sense to me) into a list of strings. You can also
  use `datetime.strptime` to convert such strings into datetime objects. See the
  [datetime documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime)
  for more information.
* See this Stack Overflow 
  [post](https://stackoverflow.com/questions/14946371/editing-the-date-formatting-of-x-axis-tick-labels)
  for an example (one was adapted for a class example as well) of plotting datatime values.

## P05 Popularity (20 points)

Create a program that visualizes the popularity of baby names in the US over time. Your program must get its data from
the files in [data/names](data/names). Prompt the user for a name and gender then display 3 plots:

* A plot showing the number of babies of the given gender with that name for each year in the data set.
* A plot showing the percentage of babies of the given gender with that name for each year in the data set.
* A plot showing the rank of that name for babies of the given gender for each year in the data set.

In each case, you should design the graph to be clear, easy to read, and to show how the popularity of the name has
changed over time (i.e. be careful in how you pick the ranges and other parameters for your plots).

Be sure to read [NationalReadMe](data/names/NationalReadMe.pdf) to understand how the data files are arranged.

Data source: [Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html)

## P06 Light Up (10 points)

Create a program that divides a window into a 25 by 25 grid. Each cell of the grid starts off. If the user clicks on a
cell it toggles from off to on or on to off. Draw lines between each cell.

### Hints

* Uses a 2D list to keep track of the state of each cell.
* Use the `turtle` module to draw the grid and the cells.
* Use an event handler to handle mouse clicks.
* Do not draw all of the cells after each click, just draw the cell that has been toggled.

## P07 Particles (20 points)

There are a lot of neat effects that can be created by simulating particles. In this project you will create a program
that generates a number of particles and then animates them. Each particle has:

* position (x, y)
* velocity (dx, dy)
* color
* time to live (ttl)

In object-oriented programming we would make an object to encapsulate all of these values. However, for this project you
will use the older (but still useful) technique of using a list to store all the values for a particle. For example,
the list `p = [0.0, 1.0, 2.5, -3.5, "red", 100]` would represent a particle with position (0.0, 1.0), velocity
(2.5, -3.5), color "red", and ttl 100. We can then use named constants to refer to the values in the list. For example,

```python
X = 0
Y = 1
DX = 2
DY = 3
COLOR = 4
TTL = 5
p = [0.0, 1.0, 2.5, -3.5, "red", 100]
print(f"location: ({p[X]}, {p[Y]}), velocity: ({p[DX]}, {p[DY]}), color: {p[COLOR]}, ttl: {p[TTL]}")
```

Note the color could be an RGB tuple instead of a string.

Your program will be controlled by the constants (set to values you choose that keeps the program interesting and
responsive):

* `NUMBER_OF_NEW_PARTICLES`, the number of new particles to create each time the user clicks the mouse
* `DEFAULT_TTL`, the default time to live for a particle
* `MAX_STARTING_SPEED`, the maximum starting speed for a particle
* `SLEEP_TIME`, the amount of time to sleep between frames (in milliseconds for an `ontimer` call)
* `GRAVITY`, the amount of gravity to apply to the particles
* `PARTICLE_SIZE`, the size of the particles (this should be small around 1 or 2)

Your program should start with an empty list of particles (note this will be a list of lists as each particle is a
lists of values). Each time the user clicks the mouse `NUMBER_OF_NEW_PARTICLES` particles should be created and added
to the list. Each particle should have a starting position of the click point, a random velocity (with magnitude
between 0 and `MAX_STARTING_SPEED`), random color, and either a random or fixed TTL based on `DEFAULT_TTL`. You can
pick if you want to randomize the TTL or not. If it is random, the particles will disappear at different times. If it
is fixed, all particles will disappear at the same time. It just depends on the effect you want to create. 

Each time the program updates, it should move each particle by its velocity, apply gravity to the y component
of the velocity, draw the particle as a dot, decrease the TTL by 1, and remove any particles that have a TTL of 0.
If a particle hits the edge of the window, it should bounce off the edge. Program should repeatedly update every
`SLEEP_TIME` milliseconds.

## Hints

Removing particles from the middle of a list with repeated use of `del` is slow. If your TTL is fixed then you can
remove all the dead particles at once by using a slice. If your TTL is random you can use a list comprehension to
keep only the particles that are alive or use a loop to make a copy of the list with just the particles that are alive.


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
