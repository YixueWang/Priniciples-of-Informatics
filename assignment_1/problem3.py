import sys
import pandas as pd

file1 = open(sys.argv[1])
df = pd.DataFrame.from_csv(file1)
a = df['Complaint Type']
d = dict()

for row in a:
    if row in d:
    	d[row]+=1
    else:
    	d[row]=1

order_d = sorted(d.items(), key = lambda x:(-x[1],x[0]))
for n in order_d:
	print str(n[0])+' with '+ str(n[1])+' complaints'