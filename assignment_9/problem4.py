import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.objects import HoverTool
from collections import OrderedDict
import numpy as np


complaintfile= sys.argv[1]
zipfile = sys.argv[2]
shapeFilename = sys.argv[3]

complaintsByZip = {}
zip_Codes = []
agency1_num = []
agency2_num = []

a=[]# list of zipcodes in NY
#current_agency = []
#complaint_num = []
polygons = {'lat_list': [], 'lng_list': [],'lat_list_a':[],'lng_list_a':[] ,'r_list' : []}
record_index = 0

dat = shapefile.Reader(shapeFilename)

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
    lng = np.mean(lngs)
    lat = np.mean(lats)
    # Stores lat/lng for current zip shape.
    polygons['lng_list'].append(lngs)
    polygons['lat_list'].append(lats)
    polygons['lng_list_a'].append(lng)
    polygons['lat_list_a'].append(lat)

    if currentZip in complaintsByZip.keys():
      complaint = complaintsByZip[currentZip]
      rad = int(complaint)/100
    else:
      rad = 0
    polygons['r_list'].append(rad)

  record_index += 1

output_file("problem4.html", title="Complaints in each NYC zip code ")

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,previewsave"

patches(polygons['lng_list'], polygons['lat_list'],fill_color = "white", line_color="gray", tools=TOOLS, plot_width=1100, plot_height=700, title="Complaints in New York")

hold()

scatter(polygons['lng_list_a'], polygons['lat_list_a'],size = polygons['r_list'], tools=TOOLS, fill_alpha=0.6,line_color=None)
#hover = curplot().select(dict(type=HoverTool))

#hover.tooltips = OrderedDict([
#    ("(x,y)", "($x, $y)"),
#    ("fill color", "$color[hex, swatch]:fill_color"),
#])

show()


