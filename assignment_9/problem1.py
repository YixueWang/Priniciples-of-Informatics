import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.objects import HoverTool
from collections import OrderedDict


complaintfile= sys.argv[1]
zipfile = sys.argv[2]
shapeFilename = sys.argv[3]

complaintsByZip = {}
agency_Zipcount = {}
agencylist = []
agencylist2 = []
zip_Codes = []
b = {}
a=[]# list of zipcodes in NY
#current_agency = []
#complaint_num = []
polygons = {'lat_list': [], 'lng_list': [], 'color_list' : [], 'current_agency' :[], 'complaint_num':[]}
record_index = 0

dat = shapefile.Reader(shapeFilename)
colorscale = ["#FF0000","#BF3030","#A60000","#FF4040","#FF7373","#FF7400","#BF7130","#A64B00","#FF9640","#FFB273","#CD0074","#992667"]

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

for item1 in agency_Zipcount.values():
  z = sorted(item1.iteritems(), key = lambda x: (-x[1]), reverse=False)
  agencylist.append(z[0][0])

with open(zipfile) as f:
  csvReader = csv.reader(f)
  csvReader.next()
  for row in csvReader:
    a.append(row[0])

agencylist = ['DPR', 'DOHMH', 'DEP', 'TLC', 'FDNY', 'NYPD', 'DOT', 'HPD']

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
      f = sorted(complaintsbyagency.iteritems(), key = lambda x:(-x[1]))
      current_agency = f[0][0]
      agencylist2.append(current_agency)
      complaint_num = f[0][1]
      color= colorscale[agencylist.index(f[0][0])]
    else:
      color = 'white'
      current_agency = 'none'
      complaint_num = 'none'

    polygons['color_list'].append(color)
    polygons['current_agency'].append(current_agency)
    polygons['complaint_num'].append(complaint_num)
  record_index += 1
#agencylist2 = list(set(agencylist2))
#print agencylist2
source = ColumnDataSource(
    data=dict(
        x = polygons['lng_list'],
        y = polygons['lat_list'],
        colors=polygons['color_list'],
        complaintname=polygons['current_agency'],
        complaintnumber=polygons['complaint_num'],
    )
)

#print agencylist
output_file("problem1.html", title="top agency in number of complaints sin each NYC zip code ")

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,previewsave"

patches(polygons['lng_list'], polygons['lat_list'], fill_color= polygons['color_list'],line_color="gray", source = source, tools=TOOLS, plot_width=1100, plot_height=700, title="Complaints in New York")

hover = curplot().select(dict(type=HoverTool))

hover.tooltips = OrderedDict([
    ("agency", "@complaintname"),
    ("complaints Volumn", "@complaintnumber"),
    ("(x,y)", "($x, $y)"),
    ("fill color", "$color[hex, swatch]:fill_color"),
])
hold()

x = -73.74
y = 40.9
for i in agencylist:
  rect([x],[y],color=colorscale[agencylist.index(i)], width=0.01, height=0.01)
  text([x+0.02],[y],text=i, angle=0, text_font_size="8pt", text_align="left", text_baseline="middle")
  y = y - 0.015
show()


