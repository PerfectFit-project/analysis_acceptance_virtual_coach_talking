# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import numpy
from numpy import genfromtxt, transpose, isnan
from scipy.stats import mstats
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = 'complete.csv'

    csv2 = []
    with open(filename, 'r') as file2:
        reader = csv.reader(file2)
        for row in reader:
            csv2.append(row)

    # Name of the 2 columns to check for a pearson correlation
    col1 = csv2[0].index("t_impersonal")
    col2 = csv2[0].index("age")
    print("column 1: " + str(csv2[0][col1]))
    print("column 2: " + str(csv2[0][col2]))


    file = open(filename)
    data = transpose(genfromtxt(file, delimiter=','))

    data11 = data[col1][1:]
    data22 = data[col2][1:]
    data1 = []
    data2 = []
    # this filters out any responses with an empty identifier in the selected columns
    for i in range(len(data11)):
        if (not numpy.isnan(data11[i]) and not numpy.isnan(data22[i])):
            data1.append(data11[i])
            data2.append(data22[i])



    # print(data1)
    print("number of answers: " + str(len(data1)))
    res = mstats.pearsonr(data2, data1)
    print("Correlation: " + str(res[0]))
    print("P-Value: " + str(res[1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
