#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:43:25 2022

@author: meierms
"""

import sys 
import numpy as np
import matplotlib.pyplot as plt

fld = "output_pureap" 

drt = "countourCurves" 
'''
fld = sys.argv[1]
if sys.argv[2]:
    drt += str(sys.argv[2])
#'''
path = "/home/meierms/solidphase/outs/"+ fld +"/" 

a={}
with open(path + "metadata") as f:
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
    steps = int(float(a["stop_time"]) / float(a["amr.plot_dt"]))
else:
    g = ""
    for i in a["Status"]:
        if i <= '9' and i >= '0':
            g += i 
    steps = int(float(g) / 100 * float(a["stop_time"]) / float(a["amr.plot_dt"]))

dt = float(a["amr.plot_dt"]) 

print(steps)
print(dt)

xtime = [0.0]
time = []

for i in range(steps+1):
    time.append(round(dt*i, 2))

c = 0
for i in range(steps):
    if i < 10: 
        add = "000"
    elif i < 100 and i >=  11:
        add = "00"
    elif i < 1000 and i > 101:
        add = "0"
    else: 
        add = "" 
    
    var = path + drt + "/visit" + add + str(i) + ".curve"
    
    try:
        df = np.loadtxt(var)
        x = df[:,0]
        local = max(x)
        xtime.append(local)
    except:
        xtime.append(0.0)
        c += 1

xx = [1000 * i for i in xtime]
        
plt.figure()
plt.plot(time, xx)
plt.xlabel("time [s]")
plt.ylabel("Location [m]")
plt.title("Interface Location")

dx = []
for i in range(steps):
    value = (xtime[i+1] - xtime[i]) / dt
    dx.append(value)
    
dxmm = [i*1000 for i in dx]
dxmm2 = []
for i in dxmm: 
    if i > 0.8 or i < -4:
        dxmm2.append(0.0)
    else: 
        dxmm2.append(i)
           
plt.figure()
plt.plot(time[:-1], dxmm2)
plt.xlabel("time [s] ")
plt.ylabel("velocity [mm/s]" )
plt.title("burn rate [" + fld + "]" )