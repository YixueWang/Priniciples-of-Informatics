import sys
import csv
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


agencyCount = {}
k = int(sys.argv[2])

with open(sys.argv[1]) as f:
	csvReader = csv.reader(f)
	hearders = next(csvReader)

	for row in csvReader:
		agency = row[3]
		count = agencyCount.setdefault(agency, 0)
		agencyCount[agency] = count +1

sortedCompliant = sorted(agencyCount.iteritems(), key = lambda x: (-x[1]), reverse=False)
top_k = sortedCompliant[0:k]
agency = []
count1 = []

for i in top_k:
	agency.append(i[0])
	count1.append(i[1])
s = pd.Series(count1, index = agency)
plt.title('Top-' +str(k)+' complaint agencies, Jun/01/2013 - Aug/31/2013')
plt.xlabel('Compliant Type')
plt.ylabel('Volume')

ax = plt.gca()
ax.tick_params(axis = 'x', colors = 'blue')
ax.tick_params(axis = 'y', colors = 'red')

colors ='rgbky'
pd.Series.plot(
	s,
	kind = 'bar',
	color = colors,
	)
plt.show()