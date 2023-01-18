#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:45:28 2022

@author: mmeierdo
"""

import visit
import os 
import time 
import sys
import getpass
#import simba

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
    SaveWindowAtts.compression = SaveWindowAtts.None  # NONE, PackBits, Jpeg, Deflate, LZW
    SaveWindowAtts.forceMerge = 0
    SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
    SaveWindowAtts.pixelData = 1
    SaveWindowAtts.advancedMultiWindowSave = 0
    SaveWindowAtts.opts.types = ()
    SaveWindowAtts.opts.help = ""
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

#fld = sys.argv[1] #"output_mix

var = ['AP_HTPB_SandwichNew/output.old.20230114115944', 'AP_HTPB_SandwichNew/output.old.20230114130642', 'AP_HTPB_SandwichNew/output.old.20230114133818', 'AP_HTPB_SandwichNew/output.old.20230114144045', 'AP_HTPB_SandwichNew/output.old.20230114131939', 'AP_HTPB_SandwichNew/output.old.20230114160324', 'AP_HTPB_SandwichNew/output.old.20230114131846', 'AP_HTPB_SandwichNew/output.old.20230114143921', 'AP_HTPB_SandwichNew/output.old.20230114115910', 'AP_HTPB_SandwichNew/output.old.20230114160414', 'AP_HTPB_SandwichNew/output.old.20230114131933', 'AP_HTPB_SandwichNew/output.old.20230114154410', 'AP_HTPB_SandwichNew/output.old.20230114144127', 'AP_HTPB_SandwichNew/output.old.20230114125333', 'AP_HTPB_SandwichNew/output.old.20230114143939', 'AP_HTPB_SandwichNew/output.old.20230114144003', 'AP_HTPB_SandwichNew/output.old.20230114115933', 'AP_HTPB_SandwichNew/output.old.20230114160329', 'AP_HTPB_SandwichNew/output.old.20230114142320', 'AP_HTPB_SandwichNew/output.old.20230114120553', 'AP_HTPB_SandwichNew/output.old.20230114131752', 'AP_HTPB_SandwichNew/output.old.20230114150847', 'AP_HTPB_SandwichNew/output.old.20230114154129', 'AP_HTPB_SandwichNew/output.old.20230114135932', 'AP_HTPB_SandwichNew/output.old.20230114132745', 'AP_HTPB_SandwichNew/output.old.20230114140443', 'AP_HTPB_SandwichNew/output.old.20230114143951', 'AP_HTPB_SandwichNew/output.old.20230114131923', 'AP_HTPB_SandwichNew/output.old.20230114115950', 'AP_HTPB_SandwichNew/output.old.20230114145224', 'AP_HTPB_SandwichNew/output.old.20230114160333', 'AP_HTPB_SandwichNew/output.old.20230114134614', 'AP_HTPB_SandwichNew/output.old.20230114145756', 'AP_HTPB_SandwichNew/output.old.20230114115956', 'AP_HTPB_SandwichNew/output.old.20230114133544', 'AP_HTPB_SandwichNew/output.old.20230114144055', 'AP_HTPB_SandwichNew/output.old.20230114131840', 'AP_HTPB_SandwichNew/output.old.20230114132218', 'AP_HTPB_SandwichNew/output.old.20230114143943', 'AP_HTPB_SandwichNew/output.old.20230114115904', 'AP_HTPB_SandwichNew/output.old.20230114143925', 'AP_HTPB_SandwichNew/output.old.20230114144104', 'AP_HTPB_SandwichNew/output.old.20230114134851', 'AP_HTPB_SandwichNew/output.old.20230114141756', 'AP_HTPB_SandwichNew/output.old.20230114123457', 'AP_HTPB_SandwichNew/output.old.20230114160349', 'AP_HTPB_SandwichNew/output.old.20230114135410', 'AP_HTPB_SandwichNew/output.old.20230114153319', 'AP_HTPB_SandwichNew/output.old.20230114144113', 'AP_HTPB_SandwichNew/output.old.20230114131817', 'AP_HTPB_SandwichNew/output.old.20230114131912', 'AP_HTPB_SandwichNew/output.old.20230114160316', 'AP_HTPB_SandwichNew/output.old.20230114142832', 'AP_HTPB_SandwichNew/output.old.20230114131928', 'AP_HTPB_SandwichNew/output.old.20230114144109', 'AP_HTPB_SandwichNew/output.old.20230114140728', 'AP_HTPB_SandwichNew/output.old.20230114122148', 'AP_HTPB_SandwichNew/output.old.20230114143917', 'AP_HTPB_SandwichNew/output.old.20230114115859', 'AP_HTPB_SandwichNew/output.old.20230114124537', 'AP_HTPB_SandwichNew/output.old.20230114144652', 'AP_HTPB_SandwichNew/output.old.20230114122944', 'AP_HTPB_SandwichNew/output.old.20230114143350', 'AP_HTPB_SandwichNew/output.old.20230114115927', 'AP_HTPB_SandwichNew/output.old.20230114120827', 'AP_HTPB_SandwichNew/output.old.20230114141524', 'AP_HTPB_SandwichNew/output.old.20230114152230', 'AP_HTPB_SandwichNew/output.old.20230114150607', 'AP_HTPB_SandwichNew/output.old.20230114120013', 'AP_HTPB_SandwichNew/output.old.20230114144016', 'AP_HTPB_SandwichNew/output.old.20230114131800', 'AP_HTPB_SandwichNew/output.old.20230114153040', 'AP_HTPB_SandwichNew/output.old.20230114123742', 'AP_HTPB_SandwichNew/output.old.20230114160320', 'AP_HTPB_SandwichNew/output.old.20230114160406', 'AP_HTPB_SandwichNew/output.old.20230114131748', 'AP_HTPB_SandwichNew/output.old.20230114142553', 'AP_HTPB_SandwichNew/output.old.20230114151129', 'AP_HTPB_SandwichNew/output.old.20230114131735', 'AP_HTPB_SandwichNew/output.old.20230114132458', 'AP_HTPB_SandwichNew/output.old.20230114131821', 'AP_HTPB_SandwichNew/output.old.20230114120018', 'AP_HTPB_SandwichNew/output.old.20230114144123', 'AP_HTPB_SandwichNew/output.old.20230114122659', 'AP_HTPB_SandwichNew/output.old.20230114115938', 'AP_HTPB_SandwichNew/output.old.20230114131907', 'AP_HTPB_SandwichNew/output.old.20230114131804', 'AP_HTPB_SandwichNew/output.old.20230114150036', 'AP_HTPB_SandwichNew/output.old.20230114153601', 'AP_HTPB_SandwichNew/output.old.20230114131727', 'AP_HTPB_SandwichNew/output.old.20230114121351', 'AP_HTPB_SandwichNew/output.old.20230114143117', 'AP_HTPB_SandwichNew/output.old.20230114124810', 'AP_HTPB_SandwichNew/output.old.20230114131830', 'AP_HTPB_SandwichNew/output.old.20230114160341', 'AP_HTPB_SandwichNew/output.old.20230114115916', 'AP_HTPB_SandwichNew/output.old.20230114143955', 'AP_HTPB_SandwichNew/output.old.20230114144407', 'AP_HTPB_SandwichNew/output.old.20230114131740', 'AP_HTPB_SandwichNew/output.old.20230114145506', 'AP_HTPB_SandwichNew/output.old.20230114131901', 'AP_HTPB_SandwichNew/output.old.20230114144035', 'AP_HTPB_SandwichNew/output.old.20230114144050', 'AP_HTPB_SandwichNew/output.old.20230114134342', 'AP_HTPB_SandwichNew/output.old.20230114143947', 'AP_HTPB_SandwichNew/output.old.20230114144030', 'AP_HTPB_SandwichNew/output.old.20230114143628', 'AP_HTPB_SandwichNew/output.old.20230114120001', 'AP_HTPB_SandwichNew/output.old.20230114131812', 'AP_HTPB_SandwichNew/output.old.20230114144059', 'AP_HTPB_SandwichNew/output.old.20230114131756', 'AP_HTPB_SandwichNew/output.old.20230114153849', 'AP_HTPB_SandwichNew/output.old.20230114131200', 'AP_HTPB_SandwichNew/output.old.20230114124015', 'AP_HTPB_SandwichNew/output.old.20230114144008', 'AP_HTPB_SandwichNew/output.old.20230114121902', 'AP_HTPB_SandwichNew/output.old.20230114120007', 'AP_HTPB_SandwichNew/output.old.20230114115921', 'AP_HTPB_SandwichNew/output.old.20230114130926', 'AP_HTPB_SandwichNew/output.old.20230114120252', 'AP_HTPB_SandwichNew/output.old.20230114131744', 'AP_HTPB_SandwichNew/output.old.20230114131808', 'AP_HTPB_SandwichNew/output.old.20230114160345', 'AP_HTPB_SandwichNew/output.old.20230114121106', 'AP_HTPB_SandwichNew/output.old.20230114155508', 'AP_HTPB_SandwichNew/output.old.20230114143959', 'AP_HTPB_SandwichNew/output.old.20230114122422', 'AP_HTPB_SandwichNew/output.old.20230114140204', 'AP_HTPB_SandwichNew/output.old.20230114142035', 'AP_HTPB_SandwichNew/output.old.20230114125607', 'AP_HTPB_SandwichNew/output.old.20230114120532', 'AP_HTPB_SandwichNew/output.old.20230114135647', 'AP_HTPB_SandwichNew/output.old.20230114160337', 'AP_HTPB_SandwichNew/output.old.20230114143913', 'AP_HTPB_SandwichNew/output.old.20230114160402', 'AP_HTPB_SandwichNew/output.old.20230114131856', 'AP_HTPB_SandwichNew/output.old.20230114123219', 'AP_HTPB_SandwichNew/output.old.20230114124252', 'AP_HTPB_SandwichNew/output.old.20230114131723', 'AP_HTPB_SandwichNew/output.old.20230114130129', 'AP_HTPB_SandwichNew/output.old.20230114131835', 'AP_HTPB_SandwichNew/output.old.20230114151419', 'AP_HTPB_SandwichNew/output.old.20230114131851', 'AP_HTPB_SandwichNew/output.old.20230114121625', 'AP_HTPB_SandwichNew/output.old.20230114160410', 'AP_HTPB_SandwichNew/output.old.20230114133258', 'AP_HTPB_SandwichNew/output.old.20230114152510', 'AP_HTPB_SandwichNew/output.old.20230114144040', 'AP_HTPB_SandwichNew/output.old.20230114155223', 'AP_HTPB_SandwichNew/output.old.20230114160358', 'AP_HTPB_SandwichNew/output.old.20230114125845', 'AP_HTPB_SandwichNew/output.old.20230114134057', 'AP_HTPB_SandwichNew/output.old.20230114131917', 'AP_HTPB_SandwichNew/output.old.20230114143930', 'AP_HTPB_SandwichNew/output.old.20230114144020', 'AP_HTPB_SandwichNew/output.old.20230114131944', 'AP_HTPB_SandwichNew/output', 'AP_HTPB_SandwichNew/output.old.20230114125048', 'AP_HTPB_SandwichNew/output.old.20230114160030', 'AP_HTPB_SandwichNew/output.old.20230114135138', 'AP_HTPB_SandwichNew/output.old.20230114144025', 'AP_HTPB_SandwichNew/output.old.20230114144118', 'AP_HTPB_SandwichNew/output.old.20230114160353', 'AP_HTPB_SandwichNew/output.old.20230114131731', 'AP_HTPB_SandwichNew/output.old.20230114130403', 'AP_HTPB_SandwichNew/output.old.20230114150317', 'AP_HTPB_SandwichNew/output.old.20230114131825', 'AP_HTPB_SandwichNew/output.old.20230114144012', 'AP_HTPB_SandwichNew/output.old.20230114151942', 'AP_HTPB_SandwichNew/output.old.20230114154657', 'AP_HTPB_SandwichNew/output.old.20230114133019', 'AP_HTPB_SandwichNew/output.old.20230114141001', 'AP_HTPB_SandwichNew/output.old.20230114143935', 'AP_HTPB_SandwichNew/output.old.20230114151700', 'AP_HTPB_SandwichNew/output.old.20230114152752', 'AP_HTPB_SandwichNew/output.old.20230114155749', 'AP_HTPB_SandwichNew/output.old.20230114131438', 'AP_HTPB_SandwichNew/output.old.20230114141239', 'AP_HTPB_SandwichNew/output.old.20230114144944', 'AP_HTPB_SandwichNew/output.old.20230114154937']
 


gf = 0
for record in var:
    
    fld = record
    drt = "contourCurves"
    subfile = "AP_HTPB_Sandwich"
    usr = getpass.getuser()
    prt = "/home/"+usr+"/solidphase/"+fld+"/"

    path = os.path.join(prt,drt)

    try: 
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
            try:
                steps = float(a["stop_time"]) / float(a["amr.plot_dt"])
            except:
                steps = float(a["stop_time"]) / float(a["timestep"])
        else:
            g = ""
            for i in a["Status"]:
                if i <= '9' and i >= '0':
                    g += i 
            steps = float(g) / 100 * float(a["stop_time"]) / float(a["amr.plot_dt"])
        print(steps)
        OpenDatabase("localhost:/home/"+usr+"/solidphase/"+fld+"/celloutput.visit", 0)


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
            SaveWindowAtts.compression = SaveWindowAtts.None
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
            
        DeleteActivePlots()
        OpenDatabase("localhost:/home/"+usr+"/solidphase/"+fld+"/celloutput.visit")
        
    except: 
        gf += 1
        print(gf)
            

    
