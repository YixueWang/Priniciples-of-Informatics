import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


complaintfile= sys.argv[1]
zipfile = sys.argv[2]


complaintsByZip = {}
agency_Zipcount = {}

with open(complaintfile, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        zipCode = row[8]
        agency = row[3]

        if zipCode =="":
            continue
        if zipCode in agency_Zipcount:
            if agency in agency_Zipcount[zipCode]:
                agency_Zipcount[zipCode][agency] += 1
            else:
                agency_Zipcount[zipCode][agency] = 1
        else:
            myDict = {}
            myDict[agency] = 1
            agency_Zipcount[zipCode] = myDict

        if zipCode in complaintsByZip:
            complaintsByZip[zipCode] += 1
        else:
            complaintsByZip[zipCode] = 1


#open zip.csv
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
NYPD_p = []
NYPD_c = []
DOT_p = []
DOT_c = []
DOB_p = []
DOB_c = []
TLC_p = []
TLC_c = []
DPR_p = []
DPR_c = []
OTHER_p = []
OTHER_c = []
for zipCode in result:
    sortedComplaint = sorted(agency_Zipcount[zipCode].iteritems(), key = lambda x: (-x[1]), reverse=False)
    for item in sortedComplaint[0]:
        if item == 'NYPD':
            NYPD_p.append(zipPopulation[zipCode])
            NYPD_c.append(result[zipCode])
            break
        if item == 'DOT':
            DOT_p.append(zipPopulation[zipCode])
            DOT_c.append(result[zipCode])            
            break
        if item == 'DOB':
            DOB_p.append(zipPopulation[zipCode])
            DOB_c.append(result[zipCode])
            break
        if item == 'TLC':
            TLC_p.append(zipPopulation[zipCode])
            TLC_c.append(result[zipCode])
            break
        if item == 'DPR':
            DPR_p.append(zipPopulation[zipCode])
            DPR_c.append(result[zipCode])
            break
        else:
            OTHER_p.append(zipPopulation[zipCode])
            OTHER_c.append(result[zipCode])            
            break


plt.scatter(NYPD_p,NYPD_c, color = 'r',label = "NYPD, " + str(len(NYPD_c))+" complaints")
plt.scatter(DOT_p,DOT_c, color = 'b',label = "DOT, " + str(len(DOT_c))+" complaints")
plt.scatter(DOB_p,DOB_c, color = 'y',label = "DOB, "  + str(len(DOB_c))+" complaints")
plt.scatter(TLC_p,TLC_c, color = 'm',label = "TLC, " + str(len(TLC_c))+" complaints")
plt.scatter(DPR_p,DPR_c, color = 'g',label = "DPR, " + str(len(DPR_c))+" complaints")
plt.scatter(OTHER_p,OTHER_c, color = 'c',label = "Others, " + str(len(OTHER_c))+" complaints")


plt.xlabel('Population')
plt.ylabel('Complaints Volume')
plt.title('Plots for each zip code: population and complaints volume')
plt.legend()
plt.show()
