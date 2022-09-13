#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:20:52 2022

@author: meierms
"""
import numpy as np
import matplotlib.pyplot as plt
from CURVE import curve, outliers, reader

var = ["outputap100","outputap200", "outputap300"] #, "outputmix400", "output500"] 
names = ["100","200", "300"] #, "400", "500"] 
st = [100,100,100]# ,100,100]
dt = [0.1,0.1,0.1]# ,0.1,0.1]
#var = ["outputap"]
#names = ["AP"]] 4567

xsize = 10
ysize = 8
bar = 4
inlab = True

j = 0
fig1, ax = plt.subplots(figsize=(xsize,ysize))
fig2, bx = plt.subplots(figsize=(xsize,ysize))
fig3, cx = plt.subplots(figsize=(xsize,ysize))

for i in var: 
    print(i)
    if not inlab:
        time, point, speed, c = curve(i)
    else: 
        time, point, speed, c = reader(i, st[j] , dt[j])
    zero_mean = np.mean(speed)
    nspeed = outliers(speed, bar=bar)
    nmean = np.mean(nspeed)

    print(names[j] +": --No-Filter: " + str(zero_mean) + " -- Filtered: "  + str(nmean))
    
    ax.plot(time, point, label = names[j])
    bx.plot(time[:-1], speed, label = names[j])
    cx.plot(time[:-1], nspeed, label = names[j])
    
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
    
