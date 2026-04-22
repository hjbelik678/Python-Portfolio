[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=9736034)
# CSM2170-Lab01

![ ](../../actions/workflows/linter.yml/badge.svg) ![ ](../../actions/workflows/classroom.yml/badge.svg)

## Project Files

Read and complete the implementations of:
* [P01LandCalculation](P01LandCalculation.py)
* [P02MilesPerGallon](P02MilesPerGallon.py)
* [P03TemperatureConverter](P03TemperatureConverter.py)
* [P04ArrivalTime](P04ArrivalTime.py)
* [P05CompoundInterest](P05CompoundInterest.py)

For this lab you may assume the user will only enter correctly formatted values.

## Testing

You can run the automated tests with the command:
```
python3 -m unittest UnitTests
```
Unit tests will also be run by GitHub when you push your code. If your
machine has multiple versions of Python on it, you may have to adjust the
command, e.g. use `python` or `python3.10` rather than `python3`. Most
IDEs, including PyCharm, will also run the test file for you. The
automated tests are not meant to be exhaustive, but to give you some
confidence that your code is correct. You should also manually test your
code with your own test cases.

## Coding Style

Your code is not only graded by the automated tests. I will run more tests on your code and review your code and
commits. You are expected to follow good programming conventions. Failure to do so will impact your grade for an
assignment. For example, you should:
* pass linting tests
* use descriptive names and avoid single character names
* make identifiers easy to read (current_value instead of curval)
* follow the [PEP 8 style](https://pep8.org/)
* include comments (lots of comments)
* comments should be meaningful, describe the logic or reason for its code block, and be readable
* include documentation strings for modules (each file) and functions
* use named constants not magic numbers (unnamed constants)
* have messages and prompts that are nicely formatted
* provide information to the user in a consistent and helpful manner
* write good commit messages
* commit early and often
* push as needed (e.g. when done with work for the day)

## Submit your work by pushing it to GitHub

Commit your changes often (at least once per program, but likely many more
times for larger programs). Push when you are done with your work for the
day or have code that you want your partner or me to see. Until you push
your commits, they will only be on your local machine. Note that the
automated tests will run when you push as well. I will grade the last push
to the main branch that is done before the deadline. Commits or pushes done
after the deadline will receive no credit. Check that you can see your code
on GitHub before the deadline.
