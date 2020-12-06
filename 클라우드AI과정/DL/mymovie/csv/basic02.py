# basic02.py
import sys
import csv
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/output2.csv'

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file) 
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row in filereader: # first row -> header 
            supplier = str(row[0]).strip()
            cost = str(row[3]).strip('$').replace(',', '') # $3,000 -> 3000
            if supplier == 'Supplier Z' or float(cost) > 600:
                filewriter.writerow(row)
print('Done.')