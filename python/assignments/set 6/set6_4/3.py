import csv

with open('01022017_sample.csv','w',newline='') as f:
	fieldnames=['id','date','location','car_name','model_name','seller_name','seller_address','price']
	thewriter=csv.DictWriter(f, fieldnames=fieldnames)
	thewriter.writerow({'id':'1','date':'01022017','location':'sample','car_name':'aaaa','model_name':'mkj','seller_name':'ffff','seller_address':'dddddddd','price':'500'})
	thewriter.writerow({'id':'2','date':'01022017','location':'sample','car_name':'aaaa','model_name':'mkj','seller_name':'ffff','seller_address':'dddddddd','price':'500'})
	thewriter.writerow({'id':'3','date':'01022017','location':'sample','car_name':'aaaa','model_name':'mkj','seller_name':'ffff','seller_address':'dddddddd','price':'500'})
	thewriter.writerow({'id':'4','date':'01022017','location':'sample','car_name':'aaaa','model_name':'mkj','seller_name':'ffff','seller_address':'dddddddd','price':'500'})
