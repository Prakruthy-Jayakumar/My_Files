def sum(arr,size):
	if(size==0):
		return 0
	else:
		return arr[size-1]+sum(arr,size-1)
n=int(input("Enter the limit:"))
a=[]
for i in range(0,n):
	x=int(input("enter the element:"))
	a.append(x)
z=sum(a,n)
print(z)