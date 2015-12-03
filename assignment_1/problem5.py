import sys
import csv
import datetime

file1 = open(sys.argv[1])
reader = csv.reader(file1)
next(reader)
d = dict()
d_c ={'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0,'Sunday':0}

for row in reader:
	date = datetime.datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p')
	date_w = date.strftime('%A')
	d_c[date_w]+=1

for k,v in d_c.items():
	print str(k)+' == '+ str(v)