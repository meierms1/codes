#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:20:52 2022

@author: meierms
"""
import numpy as np
import matplotlib.pyplot as plt
from CURVE import curve, outliers, reader
import getpass, time

#var = ["shape1MPA", "shape2MPA", "shape4MPA", "output"] #["output4MPa", "output2", "output3"] 
#names = ["P=1MPa", "P=2MPa", "P=4MPa", "new"] 
var = ["output2", "output4", "output6"] ;  names = ["P=2MPa", "P=4MPa", "P=6MPa"]

st = [100,100,100]# ,100,100]
dt = [0.5e-3,0.1,0.1]# ,0.1,0.1]
#var = ["outputap"]
#names = ["AP"]] 4567

xsize = 10
ysize = 8
bar = 4
usr = getpass.getuser()
subfile = "Paper"

j = 00
fig1, ax = plt.subplots(figsize=(xsize,ysize))
fig2, bx = plt.subplots(figsize=(xsize,ysize))
fig3, cx = plt.subplots(figsize=(xsize,ysize))

h = time.localtime()
name = "/home/"+usr+"/solidphase/" +subfile+ "/Record_" + str(h[2]) + "_" + str(h[3]) + "_" + str(h[4])

inlab = False

for i in var: 
    print(i)
    if not inlab:
        time_, point, speed, c = curve(i, subfile=subfile)
    else: 
        time_, point, speed, c = reader(i, st[j] , dt[j])
    zero_mean = np.mean(speed)
    nspeed = outliers(speed, bar=bar)
    nmean = np.mean(nspeed)
    z = int(len(speed) / 2)
    hmean = np.mean(nspeed[z:])

    print(names[j] +": --No-Filter: " + str(zero_mean) + " --Filtered: "  + str(nmean) + " --Hon: " + str(hmean))
    print("Final Position: ", max(point))
    ax.plot(time_, point, label = names[j])
    bx.plot(time_[:-1], speed, label = names[j])
    cx.plot(time_[:-1], nspeed, label = names[j])
    
    j += 1

    with open(name, "a") as namei: np.savetxt(namei,nspeed); namei.write("###########\n" ) ; np.savetxt(namei,[zero_mean, nmean, hmean] ) ; namei.write("####!!###!!####\n")

 
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
    

