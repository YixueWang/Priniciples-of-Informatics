import sys
import csv

f1 = csv.reader(open(sys.argv[1]))
f2 = csv.reader(open(sys.argv[2]))

hashtag1 ={}
hashtag2 ={}

for row in f1:
	for item in row:
		if item[0] == '#':
			if item in hashtag1:
				hashtag1[item] += 1
			else:
				hashtag1[item] = 1

for row in f2:
	for item in row:
		if item[0] == '#':
			if item in hashtag1:
				if item in hashtag2:
					hashtag2[item] +=1
				else:
					hashtag2[item] =1

order_d = sorted(hashtag2.items(), key = lambda x:(x[0]))

for n in order_d:
	print str(n[0])