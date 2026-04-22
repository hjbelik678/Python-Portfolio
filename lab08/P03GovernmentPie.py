# Authors Fox W and Henry B
import csv
import matplotlib.pyplot as plt


def main():
    with open('data/budget/budget2021.csv') as file:
        reader = csv.reader(file)
        next(reader)
        data = [row for row in reader]

    labels = [row[0] for row in data]
    values = [float(row[1]) for row in data]

    plt.pie(values, labels=labels)
    plt.title('2021 US Federal Budget')
    plt.show()


if __name__ == "__main__":
    main()
