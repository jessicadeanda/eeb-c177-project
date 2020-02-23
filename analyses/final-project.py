import pandas
# need pandas to import dataset
import numpy
# need numpy for numerical analysis
import matplotlib.pyplot as plt
# need matplotlib.pyplot to plot data; visual representation of data
import csv
# need csv to import my csv file

def np_from_csv(csv_file):
    temp_data = pandas.read_csv(csv_file, header = None)
    data = temp_data.to_numpy()
    return data
# this function imports a csv file as pandas and change it to a numpy array
# 'header = None': https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
data = np_from_csv('food_access_data.csv')

# imported my food access csv file as pandas, converted it to numpy, and saved it as data
# variable name = column # corresponding to the variable in the dataset

# Total population counts per race
white_total = 43
black_total = 44
asian_total = 45
islander_total = 46
native_total = 47
other_total = 48

# Population count living 1/2 mile beyond a supermarket per race
white_half = 8
black_half = 9
asian_half = 10
islander_half = 11
native_half = 12
other_half = 13
latino_half = 14

# Population count living 1 mile beyond a supermarket per race
white_1 = 17
black_1 = 18
asian_1 = 19
islander_1 = 20
native_1 = 21
other_1 = 22
latino_1 = 23

# Population count living 10 miles beyond a supermarket per race
white_10 = 26
black_10 = 27
asian_10 = 28
islander_10 = 29
native_10 = 30
other_10 = 31
latino_10 = 32

# Population count living 20 miles beyond a supermarket per race
white_20 = 35
black_20 = 36
asian_20 = 37
islander_20 = 38
native_20 = 39
other_20 = 40
latino_20 = 41

# MODIFICATIONS:
# in the past assignment, each distance for the supermarket (1/2, 1, 10, 20) had its own function
# the function below consolidates the functions into one
# the defined fuction also rounds the calculated percentage and sets a default value of 2 decimal places

def percent_race_at_distance(input_data, race_distance, race_total, dec = 2):
    race_distance_sum = numpy.sum(input_data[:, race_distance])
    race_total_sum = numpy.sum(input_data[:, race_total])
    # 'numpy.sum' is a functionality that adds up all values in the specified column
    # inside the parentheses, the format is: dataset_imported[rows, columns]
    # I want all rows ':' and the column corresponding to the variable specified in the first line of the function
    percentage = race_distance_sum/race_total_sum * 100
    return round(percentage, dec)
    # 'round' will round the final value

percent_white_half = percent_race_at_distance(data, white_half, white_total, 1)
print(percent_white_half, '% of the white population lives beyond 1/2 mile of the supermarket')

percent_white_1 = percent_race_at_distance(data, white_1, white_total, 1)
percent_white_10 = percent_race_at_distance(data, white_10, white_total, 1)
percent_white_20 = percent_race_at_distance(data, white_20, white_total, 1)

# the function takes input of the race name and the percentages of the race at 4 distances
# these inputs correspond to the percentage function

def plot_race_percentage_vs_distance(race, half, one, ten, twenty):
    plt.plot([0.5, 1, 10, 20],[half, one, ten, twenty])
    # plots distance values vs percentages
    plt.axis([0, 20, 0, 100])
    # sets x-axis (0, 20) and y-axis (1, 100)
    plt.xlabel('Distance from Supermarket (Miles)')
    # labels the x-axis
    plt.ylabel('Percentage')
    # labels the y-axis
    plt.title('Percentage of %s Population Living at a Distance from a Supermarket' % race)
    # sets axis title
    plt.show()
    return

plot_race_percentage_vs_distance('White', percent_white_half, percent_white_1, percent_white_10, percent_white_20)
