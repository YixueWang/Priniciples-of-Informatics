import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.objects import HoverTool
from collections import OrderedDict



complaintfile= sys.argv[1]
zipfile = sys.argv[2]
shapeFilename = sys.argv[3]
agency1 = sys.argv[4]
agency2 = sys.argv[5]

complaintsByZip = {}
agency_Zipcount = {}
agencylist = []
zip_Codes = []
agency1_num = []
agency2_num = []


a=[]# list of zipcodes in NY
#current_agency = []
#complaint_num = []
polygons = {'lat_list': [], 'lng_list': [], 'color_list' : []}
record_index = 0

dat = shapefile.Reader(shapeFilename)

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

    if currentZip in agency_Zipcount.keys():
      complaintsbyagency = agency_Zipcount[currentZip]
      if agency1 in complaintsbyagency and agency2 in complaintsbyagency:
        agency1_vol = complaintsbyagency[agency1]
        agency2_vol = complaintsbyagency[agency2]
        color = '#%02x%02x%02x' % (int(agency1_vol*255/(agency2_vol+agency1_vol)),0, int(agency2_vol*255/(agency1_vol+agency1_vol)))
      elif agency1 in complaintsbyagency:
        color = 'red'
      elif agency2 in complaintsbyagency:
        color = 'blue'
      else:
        color = 'white'
    else:
      color = 'white'

    polygons['color_list'].append(color)

  record_index += 1

output_file("problem2.html", title="Agencies comparison in each NYC zip code ")

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,previewsave"

patches(polygons['lng_list'], polygons['lat_list'], fill_color= polygons['color_list'],line_color="gray", tools=TOOLS, plot_width=1100, plot_height=700, title="Complaints in New York")

hover = curplot().select(dict(type=HoverTool))

hover.tooltips = OrderedDict([
    ("(x,y)", "($x, $y)"),
    ("fill color", "$color[hex, swatch]:fill_color"),
])
hold()
x = -73.74
y = 40.92
text([x+0.02],[y],text="100% " + str(agency1), angle=0, text_font_size="8pt", text_align="left", text_baseline="middle")
for i in range(256):
  color = '#%02x%02x%02x' % (255-i, 0, i)
  rect([x],[y],color=color, width=0.01, height=0.0003)
  y = y - 0.0003
text([x+0.02],[y],text="100% " + str(agency2), angle=0, text_font_size="8pt", text_align="left", text_baseline="middle")
show()


