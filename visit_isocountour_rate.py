#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:45:28 2022

@author: mmeierdo
"""

import visit
import os, shutil
import sys

path = "/mmfs1/home/mmeierdo/Homogeneous"
save_folder = "curve"
remove_existing_folder = 0 # 0 doesnt remove and cancel process, 1 removes the folder

var = os.listdir(path)
#var = ["output-laminatev"] # Overwrite list of directories

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

def read_metadata(path):
    a={}
    with open(path + "/metadata") as f:
        for line in f: 
            if line[0] != "#" and line[0] != "\n" and line[0] != " ":
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
    return steps 

def isocontour_loop(path, steps, nodecell = "celloutput.visit", save_lastframe = False):   
    OpenDatabase("localhost:"+path+"/"+nodecell, 0)
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
        if i == steps-1 and save_lastframe == True: 
            savepic(path)
        TimeSliderNextState()            
    DeleteActivePlots()
    OpenDatabase("localhost:"+path+"/"+nodecell)        


counter = 0
for record in var:
    record_path = os.path.join(path,record)
    if not os.path.isdir(record_path):
        raise ValueError("This record does not exist")
    try: 
        os.mkdir(record_path+"/"+save_folder)
    except: 
        if remove_existing_folder == 1:
            shutil.rmtree(record_path+"/"+save_folder)
            os.mkdir(record_path+"/"+save_folder)
        else:
            raise ValueError("Trying to create folder that already exists")    
    steps = read_metadata(record_path)
    isocontour_loop(record_path, steps)
    counter += 1
print(f"{counter} total records were sucessfully processed")

    


            

    
