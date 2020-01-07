f=open("1.txt","r")
x=f.readline()
print(x)
print(f.readline())
lineList = [line.rstrip('\n') for line in open("1.txt")]
print(lineList)
content = f.readlines()
content = [x.strip() for x in content] 
print(content)