import csv

with open('mycsv.csv','w',newline='') as f:
	fieldnames=['id','name','product','price']
	thewriter=csv.DictWriter(f, fieldnames=fieldnames)

	thewriter.writeheader()
	thewriter.writerow({'id':'1','name':'anu','product':'phone','price':'500'})
	thewriter.writerow({'id':'2','name':'bhanu','product':'apple','price':'230'}) 
	thewriter.writerow({'id':'3','name':'chinchu','product':'chair','price':'2000'}) 
	thewriter.writerow({'id':'4','name':'diya','product':'mirror','price':'550'}) 
	thewriter.writerow({'id':'5','name':'elif','product':'hat','price':'300'}) 

	