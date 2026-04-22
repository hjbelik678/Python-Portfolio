import random
import matplotlib.pyplot as plt
# Authors Fox W Henry B


def main():
    while True:
        try:
            num_dice = int(input("How many dice at least 1? "))
            while num_dice <= 0:
                num_dice = int(input("Try Again! How many dice at least 1?"))
            break
        except ValueError:
            print("Invalid input. Please enter an integer at least one.")
    while True:
        try:
            number_of_sides = int(input("How many sides at least 2?"))
            while number_of_sides <= 1:
                number_of_sides = int(input("Try Again! How many dice at least 2?"))
            break
        except ValueError:
            print("Invalid input. Please enter an integer at least 2.")

    while True:
        try:
            number_of_tests = int(input("How many test at least 1? "))
            while number_of_tests <= 0:
                number_of_tests = int(input("Try Again! How many dice at least 1?"))
            break
        except ValueError:
            print("Invalid input. Please enter an integer at least one.")

    high_possible_sum = num_dice * number_of_sides + 1
    left_edges = [0] * high_possible_sum
    n = 0
    while n != high_possible_sum:
        left_edges[n] = n
        n += 1
    counts = [0] * high_possible_sum
    while number_of_tests > 0:
        results = roll_dice(num_dice, number_of_sides)
        counts[results] += 1
        number_of_tests -= 1
    plt.xticks(left_edges)
    new = counts[num_dice: high_possible_sum]
    new_left_edge = left_edges[num_dice: high_possible_sum]
    plt.bar(new_left_edge, new)
    plt.title('Dice Roller')
    plt.show()


def roll_dice(x, y):
    return random.randint(x, y * x)


if __name__ == "__main__":
    main()
