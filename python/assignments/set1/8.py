import random
x=random.randrange(1,9)
print(x)
print("Enter a no:")
y=input()
z=int(y)
#for x in z:
if x<z:
	print("too high")
elif x==z:
	print("exactly right")
else:
	print("too low")