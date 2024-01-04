#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:20:52 2022

@author: meierms
"""
import numpy as np
import matplotlib.pyplot as plt
from CURVE import curve, outliers, reader, moveave
import getpass, time
import colormaps 


#var = ["output.old.20230822155325", "output.old.20230822161245", "output.old.20230822162842", "output.old.20230822165215", "output.old.20230822171528","output.old.20230822174340","output.old.20230822180520","output"]
#var = ["81","82","83","84","85", "862","87","88"]
var = ["81","85","82","862","83", "87","84","88"]
names1 = ["2.0","2.0","3.0","3.0","4.0","4.0","6.0","6.0"]
names2 = ["60%","76%","60%","76%","60%","76%","60%","76%"]
names = ["Pressure="+i+" Mass Frac="+j for i,j in zip(names1, names2)]
names = names[:len(var)] 

var = ["output-laminatev"]
names = ["Rate"]

xsize = 10
ysize = 8

usr = getpass.getuser()
subfile = "review"

j = 0
fig1, ax = plt.subplots(figsize=(xsize,ysize))

fig2, bx = plt.subplots(figsize=(xsize,ysize))
fig3, cx = plt.subplots(figsize=(xsize,ysize))
fig4, (dx1, dx) = plt.subplots(1, 2,figsize=(xsize*2,ysize*0.63))
h = time.localtime()
name = "/home/"+usr + "/Record_" + str(h[2]) + "_" + str(h[3]) + "_" + str(h[4])

nn = 20
bar = 2
inlab = False
sm = [] 
for i in var: 
    print(i)
    time_, point, speed, c = curve(i, subfile=subfile, rround = 4, smooth=True, nread = 4)
    zero_mean = np.mean(speed)
    nspeed = outliers(speed, bar=bar)
    mvspeed = moveave(speed, n=nn)
    nmean = np.mean(nspeed)
    z = int(len(speed) / 2)
    hmean = np.mean(nspeed[z:])
    sm.append(np.convolve(nspeed, np.ones(6)))
    print(names[j] +": --No-Filter: " + str(zero_mean) + " --Filtered: "  + str(nmean) + " --Hon: " + str(hmean))
    print("Final Position: ", max(point))
    if (True):
        ax.plot(time_, point, label = names[j])
        dx1.plot(time_, point, label = names[j])
        dx.plot(time_[:-nn], mvspeed, label = names[j])
    else:
        ax.plot(time_, point, label = names[j], ls = 'dashdot')
        dx1.plot(time_, point, label = names[j], ls = 'dashdot')
        dx.plot(time_[:-nn], mvspeed, label = names[j], ls = 'dashdot')
    bx.plot(time_[:-1], speed, label = names[j])
    cx.plot(time_[:-1], nspeed, label = names[j])
    #dx1.plot(time_, point, label = names[j])
    #dx.plot(time_[:-nn], mvspeed, label = names[j])
    j += 1

    with open(name, "a") as namei: np.savetxt(namei,nspeed); namei.write("###########\n" ) ; np.savetxt(namei,[zero_mean, nmean, hmean] ) ; namei.write("####!!###!!####\n")


#ax.set_title("Interface Location")
#bx.set_title("Burn Rate")
#cx.set_title("Burn Rate - Outliers Filtered")

ax.axvline(x= 0.045, color = "red", label = "Laser", alpha = 0.6, ls = "--")
bx.axvline(x= 0.045, color = "red", label = "Laser", alpha = 0.6, ls = "--")
cx.axvline(x= 0.045, color = "red", label = "Laser", alpha = 0.6, ls = "--")
dx.axvline(x= 0.045, color = "red", label = "Laser", alpha = 0.6, ls = "--")
dx1.axvline(x= 0.045, color = "red", label = "Laser", alpha = 0.6, ls = "--")

ax.set_xlabel("time [s]")
bx.set_xlabel("time [s]")
cx.set_xlabel("time [s]")
dx1.set_xlabel("Time [s]",  fontsize="12")
dx.set_xlabel("Time [s]",  fontsize="12")

ax.set_ylabel("Location [mm]")
dx1.set_ylabel("Location [mm]", fontsize="12")
bx.set_ylabel("Burn Rate [mm/s]")
cx.set_ylabel("Rate [mm/s]")
dx.set_ylabel("Burn Rate [mm/s]", fontsize="12")



ax.grid()
bx.grid()
cx.grid()
dx1.grid()
dx.grid()

ax.legend()
bx.legend()
cx.legend()
dx1.legend(loc="lower left", bbox_to_anchor=(0.17, 0.99, 0, 0), ncol = 4, fontsize="12")

dx.tick_params(axis='both', which='major', labelsize=12)
dx1.tick_params(axis='both', which='major', labelsize=12)
#fig4.tight_layout()
fig1.savefig(fname = "/home/meier/location2.pdf", dpi = 600, format="pdf")
fig4.savefig(fname = "/home/meier/smoothed3.pdf", dpi = 600, format="pdf")
fig2.savefig(fname = "/home/meier/rate2.pdf", dpi = 600, format="pdf")
plt.show()   
    

