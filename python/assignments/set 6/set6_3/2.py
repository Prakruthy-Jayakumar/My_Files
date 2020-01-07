import csv
filename="mycsv.csv"
fields=[]
rows=[]

with open('mycsv.csv','r') as f:
	reader=csv.reader(f)
	fields=reader.next()
	for row in reader: 
    	rows.append(row)
for row in rows[:5]:
	for col in row: 
       print("%10s"%col),
    print('\n') 