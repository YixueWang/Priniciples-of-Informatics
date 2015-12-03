import sys
import time
import csv
from scipy.spatial import KDTree, cKDTree
from bokeh.plotting import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.neighbors import KernelDensity


def loadRoadNetworkIntersections(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    listWithIntersectionCoordinates = []
    f = open(filename)
    reader = csv.reader(f, delimiter=' ')
    for l in reader:
        try:
            point = [float(l[0]),float(l[1])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                listWithIntersectionCoordinates.append(point)
        except:
            print l

    return listWithIntersectionCoordinates

def loadTaxiTrips(filename):
    #load pickup positions
    loadPickup = True
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    if loadPickup:        
        lngIndex = header.index(' pickup_longitude')
        latIndex = header.index(' pickup_latitude')
    else:
        latIndex = header.index(' dropoff_latitude')
        lngIndex = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point = [float(l[latIndex]),float(l[lngIndex])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                result.append(point)

        except:
            print l
    return result
    
def naiveApproach(intersections, tripLocations, distanceThreshold):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which are within a distance of
    #distanceThreshold from the intersection
    counts = {}
    startTime = time.time()

    #TODO: insert your code here. You should implement the naive approach, i.e., loop 
    #      through all the trips and find the closest intersection by looping through
    #      all of them
    dis_min = distanceThreshold ** 2

    for row in tripLocations:
        llat = float(row[0])
        llng = float(row[1])

        for item in intersections:
            ilat = float(item[0])
            ilng = float(item[1])

            distance = (ilat-llat)**2+(ilng-llng)**2

            if distance < dis_min:
                idx = intersections.index(item)
                if idx in counts:
                    counts[idx] += 1
                else:
                    counts[idx] = 1
            else:
                pass
    #
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return counts

def kdtreeApproach(intersections, tripLocations, distanceThreshold):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which are within a distance of
    #distanceThreshold from the intersection
    counts = {}
    startTime = time.time()

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip
    intersections = KDTree(intersections)
    idx_start =intersections.query_ball_point(tripLocations,distanceThreshold)
    
    for item in idx_start:
        for i in item:
            if i in counts:
                counts[i] +=1
            else:
                counts[i] = 1
    #
    endTime = time.time()

    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return counts

def plotResults(intersections, counts):
    #TODO: intersect the code to plot here
    lat_list = []
    lng_list = []
    count_num = []
    r_list = []

    for item in counts:
        lat_list.append(intersections[item][0])
        lng_list.append(intersections[item][1])
        count_num.append(counts[item])

    total1 = sum(count_num)
    print total1

    for item in count_num:
        r_list.append('#%02x%02x%02x' % (int(item*255/total1),255,0))

    output_file("plot for problem2.html", title="Plots for problem2 ")

    scatter(lng_list, lat_list, color=r_list,alpha = 0.5, fill_alpha=0.6,line_color=None, title = "Plots for problem2")

    show()


def extraCredit(intersections, counts):
    #TODO: intersect the code to plot here

    lat_list = []
    lng_list = []
    count_num = []
    r_list = []

    for item in counts:
        lat_list.append(intersections[item][0])
        lng_list.append(intersections[item][1])
        count_num.append(counts[item])

    count_num = np.array(count_num)

    kde = stats.gaussian_kde(count_num)
    density = kde(count_num)

    fig, ax = plt.subplots(figsize=(8, 6),
                           subplot_kw={'axisbg':'#EEEEEE',
                                       'axisbelow':True})
    ax.grid(color='white', linestyle='-', linewidth=2)
    
    ax.scatter(lng_list, lat_list, c = density)

    ax.legend()

    plt.show()

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    roadIntersections = loadRoadNetworkIntersections(sys.argv[1])
    tripPickups       = loadTaxiTrips(sys.argv[2])
    distanceThreshold = float(sys.argv[3])

    #You need to implement this one. You need to make sure that the counts are correct
    #naiveCounts = naiveApproach(roadIntersections,tripPickups, distanceThreshold)

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeCounts = kdtreeApproach(roadIntersections,tripPickups, distanceThreshold)
    #
    plotResults(roadIntersections,kdtreeCounts)

    extraCredit(roadIntersections,kdtreeCounts)

