import csv
with open('mycsv.csv') as f:
    reader = csv.DictReader(f)
    for i,row in enumerate(reader):
        print(row['id'], row['name'], row['product'], row['price'])
        if(i >=2):
            break