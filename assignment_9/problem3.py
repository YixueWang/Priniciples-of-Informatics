import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.objects import HoverTool
from collections import OrderedDict
import numpy as np

n = int(sys.argv[1])
complaintfile= sys.argv[2]
zipfile = sys.argv[3]
shapeFilename = sys.argv[4]

complaintsByZip = {}
zip_Codes = []
agency1_num = []
agency2_num = []

a=[]# list of zipcodes in NY
latlist = []
lnglist = []
countnum = []
#complaint_num = []
polygons = {'lat_list': [], 'lng_list': [],'lat_list_a':[],'lng_list_a':[] ,'r_list' : []}
record_index = 0

dat = shapefile.Reader(shapeFilename)


with open(complaintfile, 'r') as f:
  csvReader = csv.reader(f)
  headers = csvReader.next()
  latColIndex = headers.index('Latitude')
  lngColIndex = headers.index('Longitude')

  for row in csvReader:
    try:
      latlist.append(float(row[latColIndex]))
      lnglist.append(float(row[lngColIndex]))
    except:
      pass


with open(zipfile) as f:
  csvReader = csv.reader(f)
  csvReader.next()
  for row in csvReader:
    a.append(row[0])

for r in dat.iterRecords():
  currentZip = r[0]

  if currentZip in a:
    zip_Codes.append(currentZip)

    shape = dat.shapeRecord(record_index).shape
    points = shape.points

    lngs = [p[0] for p in points]
    lats = [p[1] for p in points]

    # Stores lat/lng for current zip shape.
    polygons['lng_list'].append(lngs)
    polygons['lat_list'].append(lats)
  record_index += 1

output_file("problem3.html", title="Complaints in each NYC zip code ")

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,previewsave"
hold()
lngmin = min(lnglist)
latmin = min(latlist)
lngmax = max(lnglist)
latmax = max(latlist)
lng_n = (lngmax-lngmin)/n
lat_n = (latmax-latmin)/n

twodim = []
location = []
for i in range(n):
  twodim.append([])
  location.append([])
  for a in range(n):
    twodim[i].append(0)
    location[i].append((0,0))

points=[]
for item in range(len(lnglist)):
  points.append([])

for i in range(len(lnglist)):
  points[i].append(lnglist[i])
  points[i].append(latlist[i])

for point in points:
    index_x = int(n*(point[0] - lngmin)/(lngmax-lngmin))
    index_y = int(n*(point[1] - latmin)/(latmax-latmin))
    try:
      twodim[index_x][index_y] += 1
      location[index_x][index_y] = (float(lngmin + index_x*lng_n)+ 0.5*lng_n, float(latmin + index_y*lat_n)+0.5*lat_n)
    except:
      pass

sum_1 =0
for item in twodim:
  for i in item:
    sum_1 = sum_1+i
#print sum_1

for a in range(n):
  for b in range(n):
    if twodim[a][b] == 0:
      pass
    else:
      polygons['lng_list_a'].append(location[a][b][0])
      polygons['lat_list_a'].append(location[a][b][1])
      polygons['r_list'].append(twodim[a][b]*800/sum_1)
#print polygons['lng_list_a']
#print polygons['lat_list_a']
#print polygons['r_list']
patches(polygons['lng_list'], polygons['lat_list'],fill_color = "white", line_color="gray", tools=TOOLS, plot_width=1100, plot_height=700, title="Complaints in New York")
scatter(polygons['lng_list_a'], polygons['lat_list_a'],size = polygons['r_list'], tools=TOOLS, fill_alpha=0.6,line_color=None)
#hover = curplot().select(dict(type=HoverTool))

#hover.tooltips = OrderedDict([
#    ("(x,y)", "($x, $y)"),
#    ("fill color", "$color[hex, swatch]:fill_color"),
#])

show()



