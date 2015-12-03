import sys
import csv
import matplotlib.pyplot as plt 
import numpy as np

agencyCount = {}

with open(sys.argv[1]) as f:
	csvReader = csv.reader(f)
	hearders = next(csvReader)

	for row in csvReader:
		agency = row[3]
		count = agencyCount.setdefault(agency, 0)
		agencyCount[agency] = count +1

N = 5
ind = np.arange(N)
width = 0.4

agency = ['NYPD', 'DOT', 'DOB', 'TLC', 'DPR']
count1 = []
for i in agency:
	count1.append(agencyCount[i])

plt.ylabel('Volume')
plt.title('Complaint volume of requested agency, Jun/01/2013 - Aug/31/2013')
plt.xlabel('Agencies')
plt.xticks(ind+width/2., agency)

ax = plt.gca()
ax.tick_params(axis = 'x', colors = 'blue')
ax.tick_params(axis = 'y', colors = 'red')


my_colors = 'rgbky'

p1 = plt.bar(ind, count1, width, color = my_colors)

plt.show()
