x=["apple","ball","chair","doll","elephant"]
print(x)
print(x[3])
print(x[-3])
print(x[1:4])
print(x[-1:-4])
x[1]="bell"
print(x)
print(len(x))
x.append("fan")
print(x)
x.remove('fan')
print(x)

x.insert(4,'donkey')
print(x)
x.pop()
print(x)

print("Enter your name:")
x = input()
print("Hello ", x)