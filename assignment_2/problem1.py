from datetime import *
import time
import sys

minDate = datetime.max
maxDate = datetime.min

row_counter = 0

for line in open(sys.argv[1]):
	row_counter +=1
	tokens = line.split(',')
	dt = tokens[1]
	eachdate = datetime.strptime(dt,'%a %b %d %H:%M:%S %Z %Y')
	if eachdate < minDate:
		minDate = eachdate
	if eachdate > maxDate:
		maxDate = eachdate

Datemin = minDate.strftime('%B %d %Y, %H:%M:%S')
Datemax = maxDate.strftime('%B %d %Y, %H:%M:%S')
print "There were " + str(row_counter) +" tweets between "+ str(Datemin) +" and "+ str(Datemax)