import csv
reader1 = csv.reader(open("01022017_ekm.csv"))
reader2 = csv.reader(open("01022017_klm.csv"))
reader3 = csv.reader(open("01022017_tvm.csv"))
reader4 =csv.reader(open("01022017_sample.csv"))
f = open("01022017__all3.csv", "w")
writer = csv.writer(f)

for row in reader1:
    writer.writerow(row)
for row in reader2:
    writer.writerow(row)
for row in reader3:
    writer.writerow(row)
for row in reader4:
    writer.writerow(row)
f.close()