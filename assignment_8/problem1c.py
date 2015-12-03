import sys
from datetime import date, datetime
import csv
import matplotlib.pyplot as plt

filename = sys.argv[1]

month_apple = {}
month_micro = {}
time1 = []
apple = []
micro = []
a=[]
b=[]

with open(filename, 'r') as f:
	csvReader = csv.reader(f)
	next(csvReader)
	
	for row in csvReader:
		month = datetime.strptime(row[0], "%Y-%m")
		appledata = row[1]
		microdata = row[2]
		month_micro[month] = microdata
		month_apple[month] = appledata

sortedTime1 = sorted(month_apple.iteritems(), key=lambda x: (x[0]), reverse=False)
sortedTime2 = sorted(month_micro.iteritems(), key=lambda x: (x[0]), reverse=False)

for item in sortedTime1:
	time1.append(item[0])
	apple.append(item[1])

for item in sortedTime2:
	micro.append(item[1])

for i in range(len(apple)):
	a.append(apple[0])
for i in range(len(micro)):
	b.append(micro[0])

plt.figure(1)
plt.subplot(211)
plt.plot_date(time1,apple,color = 'r', fmt ='bo-',label = 'Apple')
plt.plot_date(time1,a, color = 'r', fmt = '-', label="Apple's baseline")
plt.ylabel("Stock Quote")
plt.xlabel("Time")
plt.title("Apple's stock data")
plt.legend()

plt.subplot(212)
plt.plot_date(time1,micro, color = 'b', fmt = 'bo-', label = 'Microsoft')
plt.plot_date(time1,b, color = 'b', fmt = '-', label="Microsoft's baseline")
plt.ylabel("Stock Quote")
plt.xlabel("Time")
plt.title("Microsoft's stock data")
plt.legend()
plt.show()