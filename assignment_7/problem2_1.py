import numpy as np 
import csv
import sys
from datetime import date, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


agencyCount = {}

agencies = ['NYPD','TLC','DPR']


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