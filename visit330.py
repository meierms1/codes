import visit
import os 
import time 
import sys

def savepic(path):
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = path
    SaveWindowAtts.fileName = "lasframe"
    SaveWindowAtts.family = 1
    SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
    SaveWindowAtts.width = 1024
    SaveWindowAtts.height = 1024
    SaveWindowAtts.screenCapture = 0
    SaveWindowAtts.saveTiled = 0    
    SaveWindowAtts.quality = 80
    SaveWindowAtts.progressive = 0
    SaveWindowAtts.binary = 0
    SaveWindowAtts.stereo = 0
    SaveWindowAtts.compression = SaveWindowAtts.NONE  # NONE, PackBits, Jpeg, Deflate, LZW
    SaveWindowAtts.forceMerge = 0
    SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
    SaveWindowAtts.pixelData = 1
    SaveWindowAtts.advancedMultiWindowSave = 0
    SaveWindowAtts.opts.types = ()
    SaveWindowAtts.opts.help = ""
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

fld = sys.argv[1] #"output_mix" 
drt = "contourCurves" 
prt = "/home/meierms/solidphase/outs/"+fld+"/"
#prt = "/home/mmeierdo/solidphase/outs/output_mix/"
path = os.path.join(prt,drt)

try: 
    os.mkdir(path)
except: 
    t = int(time.time())
    drt = "contourCurves" + str(t)
    path = os.path.join(prt,drt)
    os.mkdir(path)

    
a={}
with open(prt + "metadata") as f:
    for line in f: 
        if line[0] != "#" and line[0] != "\n" and line[0] != " ":
            #print(line)
            k,v = line.split(" = ")
            v = v.split(" #")[0]
            a[k] = v
special = ["geometry.prob_lo", "geometry.prob_hi", "amr.n_cell", "phi.ic.laminate.center"]
for i in a.keys():
    a[i] = a[i].replace("\n", "")
    if " " in a[i]:
        if i not in special:
            a[i] = a[i].replace(" ", '')

steps = 50
if a["Status"][0] == "C":
    steps = float(a["stop_time"]) / float(a["amr.plot_dt"])
else:
    g = ""
    for i in a["Status"]:
        if i <= '9' and i >= '0':
            g += i 
    steps = float(g) / 100 * float(a["stop_time"]) / float(a["amr.plot_dt"])
print(steps)
OpenDatabase("localhost:/home/meierms/solidphase/outs/"+fld+"/celloutput.visit", 0)
#OpenDatabase("localhost:/home/mmeierdo/solidphase/outs/output/celloutput.visit", 0)


AddPlot("Contour", "eta", 1, 1)
ContourAtts = ContourAttributes()
ContourAtts.contourNLevels = 1
ContourAtts.contourValue = ()
ContourAtts.contourPercent = ()
ContourAtts.contourMethod = ContourAtts.Level
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0
ContourAtts.max = 1
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)
DrawPlots()

for i in range(int(steps)):
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.format = SaveWindowAtts.CURVE  # BMP, CURVE, JPEG, OBJ, PNG, POA, VTK, PLY, EXR
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = path
    SaveWindowAtts.fileName = "visit"
    SaveWindowAtts.family = 1  
    SaveWindowAtts.width = 1024
    SaveWindowAtts.height = 1024
    SaveWindowAtts.screenCapture = 0
    SaveWindowAtts.saveTiled = 0
    SaveWindowAtts.quality = 80
    SaveWindowAtts.progressive = 0
    SaveWindowAtts.binary = 0
    SaveWindowAtts.stereo = 0
    SaveWindowAtts.compression = SaveWindowAtts.NONE
    SaveWindowAtts.forceMerge = 0
    SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
    SaveWindowAtts.pixelData = 1
    SaveWindowAtts.advancedMultiWindowSave = 0
    SaveWindowAtts.opts.types = (5)
    SaveWindowAtts.opts.help = ""
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
    if i == steps-1: 
        savepic(path)
    TimeSliderNextState()



