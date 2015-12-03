import sys
from datetime import *
import time

username = {}
minDate = datetime.max
maxDate = datetime.min

for line in open(sys.argv[1]):
	tokens = line.split(',')
	if tokens[0] in username:
		username[tokens[0]] += 1
	else:
		username[tokens[0]] = 1
	dt = tokens[1]
	eachdate = datetime.strptime(dt,'%a %b %d %H:%M:%S %Z %Y')
	if eachdate < minDate:
		minDate = eachdate
	if eachdate > maxDate:
		maxDate = eachdate

rowcount = 0
for n in username:
	rowcount +=1

Datemin = minDate.strftime('%B %d %Y, %H:%M:%S')
Datemax = maxDate.strftime('%B %d %Y, %H:%M:%S')
print str(rowcount) +" users tweeted between "+ str(Datemin) +" and "+ str(Datemax)