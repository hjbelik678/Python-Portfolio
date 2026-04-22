"""Henry B & Fox W"""


def print_stars(height):
    for n in range(height):
        if n == 0:
            # for the first row
            print("_" * (height - n - 1), end="*")
            print("")
        elif n == height - 1:
            # for the last row print all stars
            print("*" * (2 * height - 1))
        else:
            # print the middle pattern
            print("_" * (height - n - 1), end="*")
            print("." * (2 * n - 1), end="*")
            print()


def main():
    height = int(input("Enter height of pyramid: "))
    # repeats the pattern if users wants to
    while height >= 0:
        print_stars(height)
        height = int(input("Enter height of pyramid: "))


if __name__ == "__main__":
    main()
