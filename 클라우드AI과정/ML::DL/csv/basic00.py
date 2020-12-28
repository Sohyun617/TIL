import glob, os

dir = os.path.dirname(os.path.realpath(__file__))

inputPath= '/'
for input_file in glob.glob(os.path.join(dir + inputPath, 'file_to_read.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))

my_letters = ['a','b','c','d','e','f','g','h']
filewriter = open(dir +inputPath + 'output.txt','a')
max_index = len(my_letters)

for index_value in range(max_index):
    if index_value <(max_index-1):
        filewriter.write(my_letters[index_value]+ ",")
    else:
        filewriter.write(my_letter[index_value] + "\n")
filewriter.close()