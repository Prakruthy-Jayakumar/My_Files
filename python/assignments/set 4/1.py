import datetime
x=datetime.datetime.now()
print(x)
print(x.strftime("%B"))
print(x.strftime("%w"))
print(x.strftime("%A"))
from datetime import datetime, timedelta
d = datetime.today() - timedelta(days=5)
print(d)
a= 1507126064
dt = (datetime.fromtimestamp(a) - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S')
print(dt)
#print(datetime.datetime(2015, 6, 16).isocalendar()[1])
from datetime import date
d0 = date(2000, 2, 28)
d1 = date(2001, 2, 28)
delta = d1 - d0
print(delta.days)