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

var = ["output1100","output1300" ,"output1400","output1500", "output1700", "output1900"]#["output_1","output_2", "output_02", "output_002"]
names = ["1100", "1300","1400","1500", "1700", "1900"] #["P=2.0MPa","P=3.0MPa", "P=4.0MPa", "P=6.0MPa"] #, "400", "500"] 
st = [100,100,100]# ,100,100]
dt = [0.1,0.1,0.1]# ,0.1,0.1]
#var = ["outputap"]
#names = ["AP"]] 4567

xsize = 10
ysize = 8
bar = 4
usr = getpass.getuser()

j = 0
fig1, ax = plt.subplots(figsize=(xsize,ysize))
fig2, bx = plt.subplots(figsize=(xsize,ysize))
fig3, cx = plt.subplots(figsize=(xsize,ysize))

h = time.localtime()
name = "/home/"+usr+"/solidphase/outs/Record_" + str(h[2]) + "_" + str(h[3]) + "_" + str(h[4])

#with open(name, "a") as namei: 
#    np.savetxt(var[0] + var[1])
inlab = False
if usr == "mmeierdo":
    inlab = True
    
for i in var: 
    print(i)
    if not inlab:
        time_, point, speed, c = curve(i)
    else: 
        time_, point, speed, c = reader(i, st[j] , dt[j])
    zero_mean = np.mean(speed)
    nspeed = outliers(speed, bar=bar)
    nmean = np.mean(nspeed)
    z = int(len(speed) / 2)
    hmean = np.mean(nspeed[z:])

    print(names[j] +": --No-Filter: " + str(zero_mean) + " --Filtered: "  + str(nmean) + " --Hon: " + str(hmean))
    print(max(point))
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
    
