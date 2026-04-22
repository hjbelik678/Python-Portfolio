"""Henry B & Fox W
For this project you will be writing a program that generates files that contain random numbers. Your program should
ask the user for the name of the file to create, the minimum and maximum values for the random numbers, and the number
of random numbers to generate. Your program should then generate the file with the specified number of random numbers
 in the specified range with one number per line."""
import random


def main():
    # obtains values from the user
    min_value = int(input("What is the minimum value you want to use [integer only]? "))
    if min_value is None:
        min_value = int(input("What is the minimum value you want to use [integer only]? "))

    max_value = int(input("What is the maximum value you want to use [integer only]? "))
    if max_value is None:
        max_value = int(input("What is the maximum value you want to use [integer only]? "))

    number_of_values = int(input("How many numbers do you want to generate[integer only]? "))
    if number_of_values is None:
        number_of_values = int(input("How many numbers do you want to generate[integer only]? "))

    file_name = input("What would you like the file to be named? ")
    if file_name is None:
        file_name = input("What would you like the file to be named? ")

    # opens the file
    file = open(file_name, "w")

    for _ in range(number_of_values):
        # repeats for however long the user says to
        # appends the randomly generated number to the file
        file.write(str(random.randint(min_value, max_value)) + "\n")

    # closes file
    file.close()


if __name__ == "__main__":
    main()
