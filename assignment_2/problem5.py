import sys
import csv
from datetime import *
import time

tweettime = {}
f = csv.reader(open(sys.argv[1]))

for row in f:
	dt = datetime.strptime(row[1], '%a %b %d %H:%M:%S %Z %Y')
	if dt in tweettime:
		tweettime[dt] += 1
	else:
		tweettime[dt] = 1

order_d = sorted(tweettime.items(), key = lambda x:(-x[1]))
tp = order_d[0]
a= tp[0].strftime('%B %d %Y, %H:%M:%S')
b = str(tp[1])
print a +' with '+ b +' tweets'