import random
import string
stringlength=8
x= string.ascii_letters + string.digits + string.punctuation
print(''.join(random.choice(x) for i in range(stringlength)))