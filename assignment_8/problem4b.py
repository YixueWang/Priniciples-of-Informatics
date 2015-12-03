from pandas.tools.plotting import scatter_matrix
import pandas as pd
import sys
import csv
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


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
diction = { 'a' : a, 'b' :b,'c' :c, 'd':d}
df = pd.DataFrame(diction)
a = np.array(a)
b = np.array(b)
c = np.array(c)
d = np.array(d)

df1 = df.reindex(columns = ['a','c','d','b'])
fig, axes = plt.subplots(3,1)
target1 = axes[0]
target2 = axes[1]
target3 = axes[2]


z1 = np.polyfit(a, c, 1)
p1 = np.poly1d(z1)
target1.plot(a,p1(a),".",color="r", label = "Best Fit Line")
target1.legend()
target1.scatter(a, c, alpha = 0.8)
target1.set_ylabel('Gene C')


z2 = np.polyfit(a, d, 3)
p2 = np.poly1d(z2)
target2.plot(a,p2(a),".",color="g", label = "Cubic Best Fit Curve")
target2.legend()
target2.scatter(a, d, alpha = 0.8)
target2.set_ylabel('Gene D')


z3 = np.polyfit(a, b, 5)
p3 = np.poly1d(z3)
target3.plot(a,p3(a),".",color="y", label = "Degree-5 Polynomial Best Fit")
target3.legend()
target3.scatter(a, b, alpha = 0.8)
target3.set_ylabel('Gene B')
target3.set_xlabel('Gene A')

fig.suptitle('Gene Plot')
#scatter_matrix(df, diagonal ='kde')
plt.show()