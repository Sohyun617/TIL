from xlrd import open_workbook
import os, glob

dir = os.path.dirname(os.path.realpath(__file__))


input_file = 'sales_2017.xlsx'
worksheet = open_workbook(dir + '/' +input_file)
print("number of worksheets : ", worksheet.nsheets)

for worksheet in worksheet.sheets():
    print('worksheet name:', worksheet.name, '\tRows:', worksheet.nrows, '\tColumns:', worksheet.ncols)
