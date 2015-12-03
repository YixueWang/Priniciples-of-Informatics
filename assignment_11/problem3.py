import sys
import time
import csv
from scipy.spatial import KDTree, cKDTree
import matplotlib.path as mplPath
import numpy as np


def loadTaxiTripsPickupAndDropoffs(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    lngIndex0 = header.index(' pickup_longitude')
    latIndex0 = header.index(' pickup_latitude')
    latIndex1 = header.index(' dropoff_latitude')
    lngIndex1 = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point0 = [float(l[latIndex0]),float(l[lngIndex0])]
            point1 = [float(l[latIndex1]),float(l[lngIndex1])]
            if latBounds[0] <= point0[0] <= latBounds[1] and lngBounds[0] <= point0[1] <= lngBounds[1] and latBounds[0] <= point1[0] <= latBounds[1] and lngBounds[0] <= point1[1] <= lngBounds[1]:
                result.append([point0[0],point0[1],point1[0],point1[1]])
        except:
            print l
    return result
    
def naiveApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
    startTime = time.time()

    #TODO: insert your code here. You should implement the naive approach, i.e., loop 
    #      through all the trips and find the closest intersection by looping through
    #      all of them
    sr_lat_min = startRectangle[0][0]
    sr_lat_max = startRectangle[0][1]
    sr_lng_min = startRectangle[1][0]
    sr_lng_max = startRectangle[1][1]

    er_lat_min = endRectangle[0][0]
    er_lat_max = endRectangle[0][1]
    er_lng_min = endRectangle[1][0]
    er_lng_max = endRectangle[1][1]

    #[[minLat,maxLat],[minLng,maxLng]]
    #[[minLat,maxLat],[minLng,maxLng]]

    for row in tripLocations:
        s_lat = float(row[0])
        s_lng = float(row[1])

        e_lat = float(row[2])
        e_lng = float(row[3])

        if sr_lat_min <= s_lat <= sr_lat_max and sr_lng_min <= s_lng <= sr_lng_max and er_lng_min <= e_lng <= er_lng_max and er_lat_min <= e_lat <=er_lat_max:
            indices.append(tripLocations.index(row))

    #
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return indices

def kdtreeApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
    startTime = time.time()

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip

    listoriginal = []
    sr_lat_min = startRectangle[0][0]
    sr_lat_max = startRectangle[0][1]
    sr_lng_min = startRectangle[1][0]
    sr_lng_max = startRectangle[1][1]

    er_lat_min = endRectangle[0][0]
    er_lat_max = endRectangle[0][1]
    er_lng_min = endRectangle[1][0]
    er_lng_max = endRectangle[1][1]

    sr_lat_center = (sr_lat_min + sr_lat_max)/2
    sr_lng_center = (sr_lng_max + sr_lng_min)/2
    er_lat_center = (er_lat_max + er_lat_min)/2
    er_lng_center = (er_lng_max + er_lng_min)/2

    start_point_center = [sr_lat_center,sr_lng_center]
    end_point_center = [er_lat_center,er_lng_center]

    start_radius = (((sr_lat_max - sr_lat_min)/2)**2 + ((sr_lng_max - sr_lng_min)/2)**2)**0.5
    end_radius = (((er_lat_max - er_lat_min)/2)**2 + ((er_lng_max - er_lng_min)/2)**2)**0.5
    
    start_locations = []
    end_locations = []

    ##np.asarray()??
    
    for row in tripLocations:
        start_locations.append([row[0],row[1]])
        end_locations.append([row[2],row[3]])

    taxi_start = KDTree(start_locations)
    taxi_end = KDTree(end_locations)
    id_start = taxi_start.query_ball_point(start_point_center, start_radius)
    id_end = taxi_end.query_ball_point(end_point_center, end_radius)

    for i in id_start:
        if i in id_end:
            listoriginal.append(i)

    for item in listoriginal:
        n = tripLocations[item]
        
        s_lat = float(n[0])
        s_lng = float(n[1])

        e_lat = float(n[2])
        e_lng = float(n[3])

        if sr_lat_min <= s_lat <= sr_lat_max and sr_lng_min <= s_lng <= sr_lng_max and er_lng_min <= e_lng <= er_lng_max and er_lat_min <= e_lat <=er_lat_max:
            indices.append(item)


    #
    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return indices


def extraCredit(tripLocations, startPolygon, endPolygon):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startPolygon region and end in the endPolygon region
    indices = []
    #latitude  ~ 40....

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip

    startpath = mplPath.Path(np.array(startPolygon))
    endpath = mplPath.Path(np.array(endPolygon))

    start_locations = []
    end_locations = []

    for row in tripLocations:
        start_locations.append((row[0],row[1]))
        end_locations.append((row[2],row[3]))

    for item in start_locations:
        if startpath.contains_point(item):
            index = start_locations.index(item)
            endp = end_locations[index]
            if endpath.contains_point(endp):
                indices.append(tripLocations.index(row))
    return indices    

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    trips             = loadTaxiTripsPickupAndDropoffs(sys.argv[1])
    #
    startRectangle    = [[40.713590,40.721319],[-74.011116,-73.994722]] #[[minLat,maxLat],[minLng,maxLng]]
    endRectangle      = [[40.744532,40.748398],[-74.003005,-73.990881]] #[[minLat,maxLat],[minLng,maxLng]]

    #You need to implement this one. You need to make sure that the counts are correct
    naiveIndices = naiveApproach(trips,startRectangle, endRectangle)
    startPolygon      = [[40.713590,-74.011116],[40.713590,-73.994722],[40.721319,-73.994722],[40.721319,-74.011116]]
    endPolygon        = [[40.744532,-74.003005],[40.744532,-73.990881],[40.748398,-73.990881],[40.748398,-74.003005]]
    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeIndices = kdtreeApproach(trips,startRectangle, endRectangle)
    extraCredit(trips, startPolygon, endPolygon)

    print "For the extra credit, I assume a position by myself, and I use matplotlib.path as mplPath and contains_point to figure out if the point is in the polygon area."
