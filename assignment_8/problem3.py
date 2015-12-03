import sys
import csv
import matplotlib.pyplot as plt

filename = sys.argv[1]

processor_name = []
year_of_introduction =[]
transistors = []

with open(filename, 'r') as f:
	csvReader = csv.reader(f)
	next(csvReader)
	
	for row in csvReader:
		name = row[0]
		year = int(row[1])
		number = int(row[2])
		processor_name.append(name)
		year_of_introduction.append(year)
		transistors.append(number)
xi = range(len(processor_name))

plt.figure(1)
plt.subplot(121)
ax = plt.gca()
ax.scatter(year_of_introduction, xi, color = "r", marker = '^', label = "Year")
ax.scatter
ax.set_yticks(xi)
ax.set_yticklabels(processor_name)
plt.legend()
plt.title("Year of Introduction of Microprocessors")
plt.draw()

plt.subplot(122)
ax = plt.gca()
ax.scatter(transistors, xi, color = 'b', marker = "x", label = "Number(log base 10 scale)")
ax.scatter
ax.set_yticks(xi)
ax.set_yticklabels(processor_name)
ax.set_xscale('log')
plt.title("Number of Transistors(log base 10 scale)")
plt.legend()
plt.draw()
#plt.plot(name ,year ,color = 'r',  label = 'Year Of Introduction')
#plt.ylabel(" Name ")
#plt.xlabel(" Year ")
#plt.title("Year of Introduction of Microprocessors")


#plt.plot(name, transistors, color = 'y', label = 'Number of Transistors')
#plt.yscale('log')
#plt.ylabel(" Name ")
#plt.xlabel(" Number of Transistors ")
#plt.title(" Number of Transistors(log base 10 scale) ")
#plt.legend()
plt.show()