import visit
import os 
import time 

drt = "countourCurves" 
prt = "/home/meierms/solidphase/outs/output_mix2/"
#prt = "/home/mmeierdo/solidphase/outs/output_mix/"
path = os.path.join(prt,drt)

try: 
    os.mkdir(path)
except: 
    t = int(time.time())
    drt = "countourCurves" + str(t)
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
OpenDatabase("localhost:/home/meierms/solidphase/outs/output/celloutput.visit", 0)
#OpenDatabase("localhost:/home/mmeierdo/solidphase/outs/output/celloutput.visit", 0)


AddPlot("Contour", "eta", 1, 1)
ContourAtts = ContourAttributes()
ContourAtts.contourNLevels = 1
ContourAtts.contourValue = ()
ContourAtts.contourPercent = ()
ContourAtts.contourMethod = ContourAtts.Level
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0.5
ContourAtts.max = 0.5
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)
DrawPlots()

for i in range(int(steps)):
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = path
    SaveWindowAtts.fileName = "visit"
    SaveWindowAtts.family = 1
    SaveWindowAtts.format = SaveWindowAtts.CURVE  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
    SaveWindowAtts.width = 1024
    SaveWindowAtts.height = 1024
    SaveWindowAtts.screenCapture = 0
    SaveWindowAtts.saveTiled = 0
    SaveWindowAtts.quality = 80
    SaveWindowAtts.progressive = 0
    SaveWindowAtts.binary = 0
    SaveWindowAtts.stereo = 0
    #SaveWindowAtts.compression = SaveWindowAtts.None  # None, PackBits, Jpeg, Deflate, LZW
    SaveWindowAtts.compression = SaveWindowAtts.NONE
    SaveWindowAtts.forceMerge = 0
    SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
    SaveWindowAtts.pixelData = 1
    SaveWindowAtts.advancedMultiWindowSave = 0
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
    TimeSliderNextState()




