# Authors Fox W and Henry B

import csv
import matplotlib.pyplot as plt
import datetime


def main():
    # Open the CSV file and read in the data
    with open('data/gas/gas.csv') as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row
        dataset = [row for row in reader]

    # Prompt the user for the start and end years
    start_year = input("Enter the start year: ")
    end_year = input("Enter the end year: ")

    # Convert the user input into datetime objects
    start_date = datetime.datetime.strptime('01/01/' + start_year, '%m/%d/%Y')
    end_date = datetime.datetime.strptime('12/31/' + end_year, '%m/%d/%Y')

    # Extract the data for the selected years
    selected_data = [row for row in dataset if start_date <= datetime.datetime.strptime(row[0], '%m/%d/%Y') <= end_date]
    dates = [datetime.datetime.strptime(row[0], '%m/%d/%Y') for row in selected_data]
    prices = [float(row[1]) for row in selected_data]

    # Create the line graph
    plt.plot(dates, prices)
    plt.xlabel('Year')
    plt.ylabel('Price ($/gallon)')
    plt.title('Gas Prices in the US ({0}-{1})'.format(start_date, end_date))

    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    main()
