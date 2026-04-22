"""Henry B & Fox W"""
import math
import random


def throw_dart():
    """Returns a random location of a dart impact as a pair of floats (x, y). Where  0 <= x < 1 and 0 <= y < 1."""
    x = random.random()
    y = random.random()
    return x, y


def is_in_circle(x, y):
    """Returns True if the location (x, y) is within the unit circle centered at the origin, False otherwise."""
    d = math.sqrt(x**2 + y**2)
    return d <= 1.0


def monte_carlo_pi(number_of_darts):
    """Returns an estimate of pi using the Monte Carlo method for a given number of darts. number_of_darts must be a
    positive integer."""
    counter = 0
    for _ in range(number_of_darts):
        x, y = throw_dart()
        if is_in_circle(x, y):
            counter += 1
    return 4 * (counter / number_of_darts)


# Make a table of estimates of pi for different numbers of darts. The number of darts should be increasing by a factor
# of 10 each time. The number of darts should start at 10 and end at 100,000,000. For each number of darts, print the
# number of darts as a power of 10 (e.g. 10^1, 10^2, 10^3, etc.), the estimate of pi, and its error (i.e. the
# difference between the estimate and math.pi). Format the output as a table where the numbers are aligned in columns
# where 6 digits are shown after the decimal point. For example:
# darts | Estimate of pi | Error
# ------+----------------+---------
# 10^1  | 2.400000       | 0.741593
# 10^2  | 3.000000       | 0.141593
# 10^3  | 3.200000       | 0.058407
# 10^4  | 3.148400       | 0.006807
# 10^5  | 3.149800       | 0.008207
# 10^6  | 3.141856       | 0.000263
# 10^7  | 3.141476       | 0.000116
# 10^8  | 3.141896       | 0.000304
def main():
    print("darts | Estimate of pi | Error")
    print("------+----------------+---------")
    for n in range(1, 9):
        # computes the result for increasing powers of 10
        print(f"10^{n}  | ", end="")
        result = monte_carlo_pi(10 ** n)
        # edited
        print(f"{result:1.6f}       | {abs((math.pi - result)):1.6f}")


# ********************************************************************************************************************
# Look at, but do not edit the code past this point
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
