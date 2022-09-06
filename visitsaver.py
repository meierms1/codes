import visit
import os 

drt = "countourCurves" 
prt = "/home/mmeierdo/solidphase/outs/output/"
path = os.path.join(prt,drt)
os.mkdir(path)
 

OpenDatabase("localhost:/home/mmeierdo/solidphase/outs/output/celloutput.visit", 0)

size = 200

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

for i in range(size):
    ContourAtts = ContourAttributes()
    ContourAtts.contourNLevels = 1
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = "/home/mmeierdo/solidphase/outs/output"
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
    SaveWindowAtts.compression = SaveWindowAtts.None  # None, PackBits, Jpeg, Deflate, LZW
    SaveWindowAtts.forceMerge = 0
    SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
    SaveWindowAtts.pixelData = 1
    SaveWindowAtts.advancedMultiWindowSave = 0
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
    TimeSliderNextState()


