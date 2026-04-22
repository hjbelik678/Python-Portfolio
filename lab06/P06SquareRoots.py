"""Henry B & Fox W
This Programs approximates the square root of a numeric value, compares the approximation to the answer given by the
math module, and repeat as the user desires. User will input the number and how many iterations they desire. The more
iterations, the closer to the root
"""
import math
X = 1


def next_x(x, n):
    """
    Calculates the next approximation of the square root of n given the old approximation x
    :param x: the old approximation of the square root of n
    :param n: the number for which we're trying to find the square root
    :return: next approximation of the root of n, 1/2(x + n/x)
    """
    return (1/2) * (x + (n / x))


def approximate_square_root(n, number_of_iterations):
    """
    Calculates an approximation x of the square root of n found by iteratively replacing the current approximation with
    one that is half-way between it and n/x
    :param n: the number for which we wish to find a square root
    :param number_of_iterations: the number of times we refine the approximation for the square root of n
    :return: an approximation for the square root of n
    """
    root = next_x(X, n)
    for _ in range(number_of_iterations - 1):
        root = next_x(root, n)
    return root


def ask_user():
    """
    Used to determine whether the user wishes to continue with the program; they must enter a `y`, `n`, `yes`, or `no`
    regardless of capitalization to continue.
    :return: True if they wish to continue or False if they wish to quit
    """
    users_answer = input("Do you wish to see the next approximation? (Yes or No) ").lower()
    if users_answer == "yes" or users_answer == "y":
        return True
    else:
        return False


def main():
    # gets user input
    users_root = int(input("Enter a number to find the root of: "))
    users_num_times = int(input("Enter how many times you would like to run it: "))
    # makes sure the user's input is valid
    if users_num_times < 1:
        users_num_times = 1
    root = approximate_square_root(users_root, users_num_times)
    # tells user the real root and the error
    print(f"calculated root: {root}")
    print(f"true answer: {math.sqrt(users_root)}")
    print(f"error: {abs(math.sqrt(users_root) - root)}")
    while ask_user():
        # keeps returning roots until the user says not to
        users_root = int(input("Enter a number to find the root of: "))
        users_num_times = int(input("Enter how many times you would like to run it: "))
        # makes sure the user's input is valid

        if users_num_times < 1:
            users_num_times = 1
        root = approximate_square_root(users_root, users_num_times)
        # tells user the real root and the error
        print(f"calculated root: {root}")
        print(f"true answer: {math.sqrt(users_root)}")
        print(f"error: {abs(math.sqrt(users_root) - root)}")


if __name__ == "__main__":
    main()
