import visit
import os
import sys
import time
import getpass

user = getpass.getuser();
fld = sys.argv[1] #"output_mix" 
step = int(sys.argv[2])
drt = "heatCurves" 
prt = "/home/" + user + "/solidphase/outs/"+fld+"/"
path = os.path.join(prt,drt)

try: 
    os.mkdir(path)
except: 
    t = int(time.time())
    drt = "contourCurves" + str(t)
    path = os.path.join(prt,drt)
    os.mkdir(path)

OpenDatabase("localhost:/home/meierms/solidphase/outs/"+fld+"/celloutput.visit", 0)

SetTimeSliderState(step)

AddPlot("Curve", "operators/Lineout/temp", 1, 1)
LineoutAtts = LineoutAttributes()
LineoutAtts.point1 = (0, 0, 0)
LineoutAtts.point2 = (0.4, 0, 0)
LineoutAtts.interactive = 0
LineoutAtts.ignoreGlobal = 0
LineoutAtts.samplingOn = 0
LineoutAtts.numberOfSamplePoints = 50
LineoutAtts.reflineLabels = 0
SetOperatorOptions(LineoutAtts, 0, 1)
DrawPlots()

SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.format = SaveWindowAtts.CURVE  # BMP, CURVE, JPEG, OBJ, PNG, POA, VTK, PLY, EXR
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = path
SaveWindowAtts.fileName = "heatprofile"
SaveWindowAtts.family = 1  
SaveWindowAtts.width = 1024
SaveWindowAtts.height = 1024
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
#SaveWindowAtts.compression = SaveWindowAtts.None
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.pixelData = 1
SaveWindowAtts.advancedMultiWindowSave = 0
SaveWindowAtts.opts.types = (5)
SaveWindowAtts.opts.help = ""
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()

