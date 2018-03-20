from info import information
import csv
import os


l = []
for i in information:
    l.append(information[i])

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
