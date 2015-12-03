import csv,sys
from collections import OrderedDict

file1 = open(sys.argv[1])
reader = csv.reader(file1)
next(reader)

d={}

for row in reader:
	if row[3] in d:
		if row[7] in d[row[3]]:
			d[row[3]][row[7]] +=1
		else :
			d[row[3]][row[7]] = 1
	else:
		d[row[3]]= {}
		d[row[3]][row[7]] = 1
d = OrderedDict(sorted(d.items(), key=lambda x:x[0]))

for n in d:
	d[n] = OrderedDict(sorted(d[n].items(), key=lambda x:x[0]))

for n in d:
	print n,
	zipcode = d[n]
	for m in zipcode:
		print str(m),
	print d[n][m]