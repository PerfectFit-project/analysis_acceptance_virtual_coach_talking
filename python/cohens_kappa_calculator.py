# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy
import numpy as np
from numpy import genfromtxt, transpose
from sklearn.metrics import cohen_kappa_score
import csv

def datatrimmer(filename, columns_to_ignore, rows_to_ignore):
    file = open(filename, encoding="utf8")
    my_data = genfromtxt(file, delimiter=',')
    my_data_trimmed = []
    for response in my_data[rows_to_ignore:]:
        my_data_trimmed.append(response[columns_to_ignore:])
    my_data_trimmed = transpose(my_data_trimmed)
    return my_data_trimmed

# This code calculates the Cohen's Kappa values between the first and second coder.
# It does this per code, resulting in a list of codes, as well as giving the average Cohen's Kappa.
if __name__ == '__main__':
    # File names of the two coded files
    own_file_name = 'first_coders_hot_one_encoding.csv'
    double_coder_file_name = 'second_coders_hot_one_encoding.csv'
    # Data trimming to remove text and leave just the 0 and 1 values.
    columns_to_ignore = 6
    rows_to_ignore = 21

    my_data_trimmed = datatrimmer(own_file_name, columns_to_ignore, rows_to_ignore)
    mahira_data_trimmed = datatrimmer(double_coder_file_name, columns_to_ignore, rows_to_ignore)

    results = []
    # Calculate Cohen's Kappa
    for i in range(len(mahira_data_trimmed)):
        results.append(round(cohen_kappa_score(my_data_trimmed[i], mahira_data_trimmed[i]), 6))

    csv2 = []
    with open(double_coder_file_name, 'r') as file2:
        reader = csv.reader(file2)
        for row in reader:
            csv2.append(row)

    # This code throws a NaN error when one of the coders never uses a code
    # To negate this, we set the Cohen's Kappa to 0.
    results[12] = 0.0
    for i in range(len(results)):
        print(str(csv2[0][columns_to_ignore+i]) + ": " + str(results[i]))

    print("Average Cohen's Kappa: " + str(round(np.average(results), 2)))


