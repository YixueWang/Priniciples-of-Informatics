import sys
import csv
import datetime

file1 = open(sys.argv[1])
reader = csv.reader(file1)
next(reader)
minDate = datetime.datetime(2200,1,1,0,0)
maxDate = datetime.datetime(1800,1,1,0,0)
counter = 0

for row in reader:
	counter += 1
	date=datetime.datetime.strptime(row[1],'%m/%d/%Y %I:%M:%S %p')
	if date < minDate:
		minDate = date
	if date > maxDate:
		maxDate = date


print str(counter)+' complaints between '+str(minDate.strftime('%m/%d/%y %H:%M:%S'))+' and '+str(maxDate.strftime('%m/%d/%y %H:%M:%S'))
    

