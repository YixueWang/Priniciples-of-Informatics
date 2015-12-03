import numpy as np 
import csv
import sys
from datetime import date, datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


aCount = {}
agencyCount = {}
minDate = datetime(2013, 06, 01, 00, 00).date()
dateList = [minDate + timedelta(days=x) for x in range(0, 92)]

k = int(sys.argv[2])

with open(sys.argv[1]) as f:
	csvReader = csv.reader(f)
	hearders = next(csvReader)

	for row in csvReader:
		agency = row[3]
		count = aCount.setdefault(agency, 0)
		aCount[agency] = count +1

sortedCompliant = sorted(aCount.iteritems(), key = lambda x: (-x[1]), reverse=False)
top_k = sortedCompliant[0:k]
agencies = []

for i in top_k:
	agencies.append(i[0])


with open(sys.argv[1]) as f:
	csvReader = csv.reader(f)
	hearders = next(csvReader)
	format_string = "%m/%d/%Y %H:%M:%S %p"

	for row in csvReader:
		agency = row[3]
		createdDate = row[1]
		stTime = datetime.strptime(createdDate, format_string)
		new_time = datetime.date(stTime)
		if agency in agencies:
			if agency in agencyCount:
				if new_time in agencyCount[agency]:
					agencyCount[agency][new_time] += 1
				else:
					agencyCount[agency][new_time] = 1
			else:
				myDict = {}
				for t in dateList:
					myDict[t] = 0
				myDict[new_time] = 1
				agencyCount[agency] = myDict

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_ylabel('Number of Complaints')
ax.set_xlabel('Date')

for item1 in agencyCount.values():
	sortedCompliant = sorted(item1.iteritems(), key = lambda x: x[0], reverse=False)
	x=[]
	y=[]
	for i in sortedCompliant:
		x.append(i[0])
		y.append(i[1])
	plt.plot_date(x,y,color = np.random.rand(3,1), fmt='-')

plt.legend(agencyCount.keys())
plt.show()
