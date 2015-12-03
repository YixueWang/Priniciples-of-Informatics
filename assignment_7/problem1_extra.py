import numpy as np 
import csv
import sys
from datetime import date, datetime
import matplotlib.pyplot as plt

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
		d = date(2013,6,8)
		
		if new_time < d:
			if agency == 'HPD':
				if new_time in agencyCount:
					agencyCount[new_time] += 1
				else:
					agencyCount[new_time] = 1

N = 7
ind = np.arange(N)
width = 0.4

sortedCompliant = sorted(agencyCount.iteritems(), key = lambda x: x[0], reverse=False)
time1 = []
count1 = []
for i in sortedCompliant:
	time1.append(str(i[0].strftime('%b/%d, %a')))
	count1.append(i[1])

plt.ylabel('Volume')
plt.title('Complaint volume of HPD, Jun/01/2013 - Jun/07/2013')
plt.xlabel('Time')
plt.xticks(ind+width/2., time1)

ax = plt.gca()
ax.tick_params(axis = 'x', colors = 'blue')
ax.tick_params(axis = 'y', colors = 'red')


my_colors = 'rgbkymc'

p1 = plt.bar(ind, count1, width, color = my_colors)

plt.show()


