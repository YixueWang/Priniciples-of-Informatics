import sys
from datetime import date, datetime
import csv
import matplotlib.pyplot as plt

filename = sys.argv[1]

month_apple = {}
time1 = []
apple = []

with open(filename, 'r') as f:
	csvReader = csv.reader(f)
	next(csvReader)
	
	for row in csvReader:
		month = datetime.strptime(row[0], "%Y-%m")
		appledata = row[1]
		month_apple[month] = appledata

sortedTime = sorted(month_apple.iteritems(), key=lambda x: (x[0]), reverse=False)

for item in sortedTime:
	time1.append(item[0])
	apple.append(item[1])

plt.plot_date(time1,apple,color = 'y', fmt ='bo-', label = 'Apple')
plt.ylabel("Stock Quote")
plt.xlabel("Time")
plt.title("Apple's stock data")
plt.legend()
plt.show()
