import pandas
import numpy
import matplotlib.pyplot as plt
import csv
def np_from_csv(csv_file):
    temp_data = pandas.read_csv(csv_file, header = None)
    data = temp_data.to_numpy()
    return data
data = np_from_csv('food_access_data.csv')

white_total = 43
black_total = 44
asian_total = 45
islander_total = 46
native_total = 47
other_total = 48
latino_total = 49
white_half = 8
black_half = 9
asian_half = 10
islander_half = 11
native_half = 12
other_half = 13
latino_half = 14
white_1 = 17
black_1 = 18
asian_1 = 19
islander_1 = 20
native_1 = 21
other_1 = 22
latino_1 = 23
white_10 = 26
black_10 = 27
asian_10 = 28
islander_10 = 29
native_10 = 30
other_10 = 31
latino_10 = 32
white_20 = 35
black_20 = 36
asian_20 = 37
islander_20 = 38
native_20 = 39
other_20 = 40
latino_20 = 41

def percent_race_at_distance(input_data, race_distance, race_total, dec = 2):
    race_distance_sum = numpy.sum(input_data[:, race_distance])
    race_total_sum = numpy.sum(input_data[:, race_total])
    percentage = race_distance_sum/race_total_sum * 100
    return round(percentage, dec)

def plot_race_percentage_vs_distance(race, perc):
    [half,one,ten,twenty] = perc
    plt.plot([0.5, 1, 10, 20],[half, one, ten, twenty])
    plt.axis([0, 20, 0, 100])
    plt.xlabel('Distance from Supermarket (Miles)')
    plt.ylabel('Percentage')
    plt.title('Percentage of %s Population Living at a Distance from a Supermarket' % race)
    return

total = [white_total, black_total, asian_total, islander_total, native_total, other_total, latino_total]
distance = [[white_half, white_1, white_10, white_20],
            [black_half, black_1, black_10, black_20],
            [asian_half, asian_1, asian_10, asian_20],
            [islander_half, islander_1, islander_10, islander_20],
            [native_half, native_1, native_10, native_20],
            [other_half, other_1, other_10, other_20],
            [latino_half, latino_1, latino_10, latino_20]]
name = ['White', 'Black', 'Asian', 'Islander', 'Native', 'Other', 'Latino']
num_races = len(total)
num_dist = 4
perc = numpy.zeros((num_races,num_dist))

for race in range(num_races):
    for dist in range(num_dist):
        perc[race][dist] = percent_race_at_distance(data, distance[race][dist], total[race], 2)
    plot_race_percentage_vs_distance(name[race], perc[race])
plt.legend(name)
plt.show()

with open('food_access_data.csv', mode = 'r', encoding = 'utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    occurrences = 0
    for row in reader:
        occurrences = occurrences + 1
    print('we have {} occurrences of values to a key.\n'.format(occurrences))

output_file = open('final-project.txt','w+')
output_file.write('The total number of occurrences in my data is {}.\n'.format(occurrences))
output_file.write('Percentage of white population living beyond half a mile from the supermarket: {:0.2f}%.\n'.format(perc[0,0]))
output_file.close()
