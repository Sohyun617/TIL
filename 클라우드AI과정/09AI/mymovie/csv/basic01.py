# basic01.py
import sys
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/output1.csv'

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',') # list (not array)
        print(header_list)
        #print(','.join(map(str, header_list)))
        filewriter.write(','.join(map(str, header_list))+'\n') # header writer...
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str, row_list))+'\n')
print('Done.')