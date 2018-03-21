from info import information
import csv
import os


l = []
for i in information:
    l.append(information[i])
'''
def WriteListToCSV(csv_file,csv_columns,data_list):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(csv_columns)
            for data in data_list:
                writer.writerow(data)
    except IOError as err:
            print("I/O error({0}): {1}".format(errno, strerror))
    return


csv_columns = ['Price','Score','Pros', 'Cons', 'Name', 'Link']
csv_data_list = l
currentPath = os.getcwd()
csv_file = currentPath + "list.csv"


WriteListToCSV(csv_file,csv_columns,csv_data_list)
'''
import csv

with open('a.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

for i in your_list[1:]:
    i[0] = int(i[0])
    i[2] = eval(i[2])
    i[3] = eval(i[3])
    i[4] = eval(i[4])

print(your_list[57:])
