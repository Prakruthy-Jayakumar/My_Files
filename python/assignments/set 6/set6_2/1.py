import os
for root, dirs, files in os.walk("."):
    for filename in files:
        myString = ''.join(map(str, filename))
        q=myString[2]+myString[3];
        a={"01":"jan","02" :"feb","03":"mar","04":"apr","05":"may","06":"jun","07":"jul",
        "08":"aug","09":"sep","10":"oct","11":"nov","12":"dec"}
        for z in a:
        	if(z==q):
        		print(a[z]+"-"+filename)
     	