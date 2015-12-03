import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
from datetime import date, datetime
from matplotlib import dates
from matplotlib.dates import date2num
import random
filename = sys.argv[1]

time1 = []
time2 = []
t1 = ['2007-09-18 12:00:00','2007-09-18 12:00:00','2007-10-04 12:00:00','2007-10-25 12:00:00','2007-11-27 12:00:00','2007-12-15 12:00:00','2007-12-11 12:00:00']

with open(filename, 'r') as f:
	csvReader = csv.reader(f)
	next(csvReader)
	
	for row in csvReader:
		#d = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
		d = datetime.strptime(row[0].split(':')[0], "%Y-%m-%d %H")
		time1.append(d)

for row in t1:
	#d = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
	date = datetime.strptime(row.split(':')[0], "%Y-%m-%d %H")
	time2.append(d)
# the histogram of the data
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.xaxis.set_major_locator(dates.DayLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d %H'))
ax.fmt_xdata = dates.DateFormatter('%Y-%m-%d %H:%M:%S')

#ts = np.array([ datetime.time(random.randint(24),*random.randint(60,size=2)) for i in range(100) ])
#for i in t1:
#	i = datetime.strptime(i,"%Y-%m-%d %H:%M:%S")


#plt.hist([t.date for t in time1], bins = 100)
#print 'HERE ' + str(len(date2num(time1)))

plt.hist(date2num(time1),bins = 1300, color = 'c')

for i in list(range(0,7)):
	#d = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
	date = datetime.strptime(t1[i].split(':')[0], "%Y-%m-%d %H")
	plt.axvline(date2num(date), color= np.random.rand(3,1), linestyle='solid', label='Assignment '+ str(i) + 'Due Time')

#plt.hist(time1, 50, normed=1, facecolor='green', alpha=0.75)
plt.title('Actions-fall-2007')
plt.xlabel('Time')
plt.ylabel('Amount of actions')
plt.legend()
plt.show()
#plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([0, 24*100, 0, 500])
#plt.grid(True)