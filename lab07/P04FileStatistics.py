"""Henry B & Fox W"""

"""For this project you will be writing a program that reads a file containing numbers and prints out some statistics
about the numbers. Your program should ask the user for the name of the file to read. Your program should then read the
 file a line at a time and print out the following statistics in a nice format:

The number of lines that were numbers in the file. 
The number of lines that were not numbers in the file. 
The sum of the lines that were numbers in the file.
The average of the lines that were numbers in the file.
The minimum value in the file.
The maximum value in the file.
The number of even numbers in the file."""


def main():
    file_name = input("What file do you want to read? ")

    with open(file_name, "r") as file:
        number_of_lines = 0
        lines_with_numbers = 0
        lines_without_numbers = 0
        even_numbers = 0
        sum_of_numbers = 0
        minimum = None
        maximum = None

        for line in file:
            number_of_lines += 1

            try:
                number = int(line.strip())
                lines_with_numbers += 1
                sum_of_numbers += number

                if number % 2 == 0:
                    even_numbers += 1

                if minimum is None:
                    minimum = number

                if maximum is None:
                    maximum = number

                if number < minimum and minimum is not None:
                    minimum = number

                if number > maximum and maximum is not None:
                    maximum = number

            except ValueError:
                lines_without_numbers += 1

            # calculates the average value
            if lines_with_numbers > 0:
                average = sum_of_numbers / lines_with_numbers
            else:
                average = 0

    # prints them all out
    print(f"There are {number_of_lines} line(s)")
    print(f"There are {lines_with_numbers} line(s) containing a numbers.")
    print(f"There are {lines_without_numbers} line(s) without a number.")
    print(f"The sum of all the line(s) with numbers is {sum_of_numbers}.")
    print(f"The minimum value is {minimum}.")
    print(f"The maximum value is {maximum}.")
    print(f"The average value is {average}.")
    print(f"There are {even_numbers} even numbers in the file.")


if __name__ == "__main__":
    main()
