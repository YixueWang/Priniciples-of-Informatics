import sys
import pandas as pd

file1 = open(sys.argv[1])
df = pd.DataFrame.from_csv(file1)
a = set(df['Complaint Type'])
b = list(df['Complaint Type'])

for n in a:
	print str(n) +' with '+ str(b.count(n)) +' complains'