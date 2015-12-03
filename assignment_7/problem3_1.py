import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


complaintfile= sys.argv[1]
zipfile = sys.argv[2]

complaintsByZip = {}
with open(complaintfile, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        zipCode = row[8]
        if zipCode =="":
            continue
        if zipCode in complaintsByZip:
            complaintsByZip[zipCode] += 1
        else:
            complaintsByZip[zipCode] = 1

zipPopulation = {}
with open(zipfile, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        zipCode = row[0]
        population = row[1]
        zipPopulation[zipCode] = population

result = {}
for zipCode in complaintsByZip:
    if zipCode in zipPopulation:
        population_num = zipPopulation[zipCode]
        complaints_num = complaintsByZip[zipCode]
        if zipCode in result:
            result[zipCode] += complaints_num
        else:
            result[zipCode] = complaints_num

population =[]
complaints=[]
for zipCode in result:
    population.append(np.float(zipPopulation[zipCode]))
    complaints.append(result[zipCode])

z = np.polyfit(population,complaints,1)
g = np.poly1d(z)

plot_label = " Trend " +"y = " +str(z[0])+"x+" +str(z[1])
plt.plot(population,g(population), color = 'b', label =plot_label)
plt.scatter(population,complaints, color = 'y')

plt.xlabel('Population')
plt.ylabel('Complaints Volume')
plt.title('Plots for each zip code: population and complaints volume')
plt.legend()
plt.show()
