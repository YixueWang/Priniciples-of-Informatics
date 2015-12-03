import csv
import sys
from datetime import*
import time

f = csv.reader(open(sys.argv[1]))
username={}
minDate = datetime.max
maxDate = datetime.min

for row in f:
	eachdate = datetime.strptime(row[1],'%a %b %d %H:%M:%S %Z %Y')
	if eachdate < minDate:
		minDate = eachdate
	if eachdate > maxDate:
		maxDate = eachdate
	if row[0] in username:
		username[row[0]] += 1
	else:
		username[row[0]] = 1

order_d = sorted(username.items(), key= lambda x:(-x[1]))
tp = order_d[0]
d1 = maxDate.strftime('%B %d %Y, %H:%M:%S')
d2 = minDate.strftime('%B %d %Y, %H:%M:%S')
b = str(tp[0])
print b +' tweeted the most'
print'Dataset range: '+ d2 +' and '+d1

