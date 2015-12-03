import sys
import csv

f = csv.reader(open(sys.argv[1]))

hashtag = {}

for row in f:
	for item in row:
		if item[0] == '#':
			if item in hashtag:
				hashtag[item]+=1
			else:
				hashtag[item]=1


order_d =sorted(hashtag.items(), key = lambda x:(-x[1],x[0]))
for n in order_d[0:10]:
	print str(n[0])+', '+ str(n[1])
