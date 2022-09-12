#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:20:52 2022

@author: meierms
"""
import numpy as np
import matplotlib.pyplot as plt
from CURVE import curve, outliers

var = ["outputap400","outputap4-300", "outputap3-350", "output001"] 
names = ["P=2MPa","P=4MPa", "P=3MPa", "P=3MPa/" ] 

#var = ["outputap"]
#names = ["AP"]

xsize = 10
ysize = 8
bar = 4

j = 0
fig1, ax = plt.subplots(figsize=(xsize,ysize))
fig2, bx = plt.subplots(figsize=(xsize,ysize))
fig3, cx = plt.subplots(figsize=(xsize,ysize))

for i in var: 
    time, point, speed, c = curve(i)
    zero_mean = np.mean(speed)
    nspeed = outliers(speed, bar=bar)
    nmean = np.mean(nspeed)

    print(names[j] +": --No-Filter: " + str(zero_mean) + " -- Filtered: "  + str(nmean))
    
    ax.plot(time, point, label = names[j])
    bx.plot(time[:-1], speed, label = names[j])
    cx.scatter(time[:-1], nspeed, label = names[j])
    
    j += 1
    
ax.set_title("Interface Location")
bx.set_title("Burn Rate")
cx.set_title("Burn Rate - Outliers Filtered")

ax.set_xlabel("time [s]")
bx.set_xlabel("time [s]")
cx.set_xlabel("time [s]")

ax.set_ylabel("Location [mm]")
bx.set_ylabel("Rate [mm/s]")
cx.set_ylabel("Rate [mm/s]")

ax.legend()
bx.legend()
cx.legend()
plt.show()   
    
