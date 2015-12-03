from pandas.tools.plotting import scatter_matrix
import pandas as pd
import sys
import csv
import matplotlib.pyplot as plt
filename = sys.argv[1]
a=[]
b=[]
c=[]
d=[]

with open(filename, 'r') as f:
	csvReader = csv.reader(f)
	next(csvReader)
	for row in csvReader:
		a.append(float(row[0]))
		b.append(float(row[1]))
		c.append(float(row[2]))
		d.append(float(row[3]))
d = { 'a' : a, 'c' :c,'d' :d, 'b':b}
df = pd.DataFrame(d)
df1 = df.reindex(columns = ['a','c','d','b'])
scatter_matrix(df1, alpha = 0.2, figsize = (6,6), diagonal ='kde')
plt.show()
