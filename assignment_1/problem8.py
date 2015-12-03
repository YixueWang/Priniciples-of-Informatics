import sys
import csv
import string

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
reader1 = csv.reader(f1)
reader2 = csv.reader(f2)
next(reader1)
next(reader2)
incident_borough = {}
borough_complaints = {'BROOKLYN':0,'BRONX':0, 'MANHATTAN':0, 'QUEENS':0, 'STATEN ISLAND':0}

for m in reader2:
	incident_borough[m[0]] = m[1]

for n in reader1:
	if n[7]:
		borough = incident_borough[n[7]]
		borough_complaints[borough]+=1
	else:
		pass

l = sorted(borough_complaints.items(), key=lambda x:(-x[1]))
for m, n in l:
	print string.capwords(str(m))+" with " + str(n)+" complaints"
