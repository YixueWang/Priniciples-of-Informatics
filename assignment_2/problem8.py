import csv
import sys

f = csv.reader(open(sys.argv[1]))

hashtag1={}
hashtag2={}

NY0 = -74.2557
NY1 = 40.4957
ny0 = -73.6895
ny1 = 40.9176

SF0 = -122.5155
SF1 = 37.7038
sf0 = -122.3247
sf1 = 37.8545

for row in f:
	if float(row[2])>= NY0 and float(row[2])<=ny0 and float(row[3])>= NY1 and float(row[3])<=ny1 :
		for item in row:
			if item[0] == '#':
				if item in hashtag1:
					hashtag1[item] +=1
				else:
					hashtag1[item] =1

	if float(row[2])>=SF0 and float(row[2])<=sf0 and float(row[3])>= SF1 and float(row[3])<=sf1 :
		for item in row:
			if item[0] == '#':
				if item in hashtag2:
					hashtag2[item]+=1
				else:
					hashtag2[item] = 1


h1 = sorted(hashtag1.items(), key = lambda x:(-x[1],x[0]))
h2 = sorted(hashtag2.items(), key = lambda x:(-x[1],x[0]))

print"New York:"
for i,v in h1[0:5]:
	print str(i)+', '+str(v)
print "San Francisco:"
for i,v in h2[0:5]:
	print str(i)+', '+str(v)
