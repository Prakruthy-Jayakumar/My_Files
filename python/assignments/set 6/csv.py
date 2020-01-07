import csv
with open('csvfile.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)