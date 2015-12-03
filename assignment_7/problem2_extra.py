import numpy as np 
import csv
import sys
from datetime import date, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

agencyCount = {}

with open(sys.argv[1]) as f:
	csvReader = csv.reader(f)
	hearders = next(csvReader)
	format_string = "%m/%d/%Y %H:%M:%S %p"

	for row in csvReader:
		agency = row[3]
		createdDate = row[1]
		stTime = datetime.strptime(createdDate, format_string)
		new_time = datetime.date(stTime)
		d = date(2013,7,15)
		if new_time < d:
			if agency == 'HPD':
				if new_time in agencyCount:
					agencyCount[new_time] += 1
				else:
					agencyCount[new_time] = 1


fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_ylabel('Number of Complaints')
ax.set_xlabel('Date')

sortedCompliant = sorted(agencyCount.iteritems(), key = lambda x: x[0], reverse=False)
x=[]
y=[]
for i in sortedCompliant:
	x.append(i[0])
	y.append(i[1])
plt.plot_date(x,y,color = np.random.rand(3,1), fmt='-', label = 'HPD')
plt.title('Complaint volume of HPD, Jun/01/2013 - Jul/14/2013')
plt.legend()
plt.show()