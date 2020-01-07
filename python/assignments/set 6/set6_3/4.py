import csv
file= "mycsv.csv" 
f = open(file)
csv_file = csv.reader(f)
column = [] 
for line in csv_file:
    column.append(line[3])
    print(line[3])