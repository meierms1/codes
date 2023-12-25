#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:20:52 2022
@author: meierms
"""
import numpy as np
import getpass, time
import os, shutil
import sys

path = "/mmfs1/home/mmeierdo/homogeneous"
save_folder = "curve"
remove_existing_folder = 0 # 0 doesnt remove and cancel process, 1 removes the folder
var = os.listdir(path)
#var = ["output-2d"] # Overwrite list of directories
if "results" in var:
    var.pop(var.index("results"))            
print(var) 
print(f"Number of records: {len(var)}")
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
    if "amr.plot_dt" in a.keys():
        plot_dt = float(a["amr.plot_dt"])
    else:
        plot_dt = float(a["timestep"]) * float(a["amr.plot_int"])
    if a["Status"][0] == "C":
        try:
            steps = float(a["stop_time"]) / plot_dt
        except:
            steps = float(a["stop_time"]) / float(a["plot_int"])
    else:
        g = ""
        for i in a["Status"]:
            if i <= '9' and i >= '0':
                g += i 
        steps = float(g) / 100 * float(a["stop_time"]) / plot_dt

    
    return int(steps), plot_dt, a["pressure.P"], a["thermal.massfraction"], a["phi.ic.constant.value"]

def curve(path, steps, dt, rround = 2, smooth=False, nread = 2):
    xtime = [0.0]
    time = []
    for i in range(int(steps)+1):
        time.append(round(dt*i, rround))
    c = 0
    listtrack=[]
    for i in range(int(steps)):
        if i < 10: 
            add = "000"
        elif i < 100 and i >=  10:
            add = "00"
        elif i < 1000 and i >= 100:
            add = "0"
        else: 
            add = "" 
        var = path + "/visit" + add + str(i) + ".curve"
        try:
            df = np.loadtxt(var)
            x = df[:,0]
            local = max(x)
            xtime.append(local)
        except:
            adv = 0.0
            if (xtime[-1] != 0.0): adv = xtime[-1] + (xtime[-1] - xtime[-2]) / 2
            xtime.append(adv)
            listtrack.append(var)
            c += 1   
    fixind = []; fixval = [] 
    for i in range(len(xtime)):
        if xtime[i] < xtime[i-1] and i < len(xtime) -1 and i > 2:
            newval = (xtime[i-1] + xtime[i+1])/2
            fixind.append(i)
            fixval.append(newval)
    j=0
    for i in fixind:
        xtime[i] = fixval[j]
        j+=1
    if smooth == True:
        print("called")
        nn = nread; ni=0
        xtime = moveave(xtime, n = nn)
        while ni < nn-1:
            xtime.append(xtime[-1])
            ni+=1
    xx = [1000 * i for i in xtime]
    dx = []
    for i in range(int(steps)):
        value = (xtime[i+1] - xtime[i]) / dt
        dx.append(value)
    
    dxmm = [i*1000 for i in dx]
    
    for i in dxmm:
        if  i > 50:
            listtrack.append(dxmm.index(i))

    print("list: ",listtrack)        
    return time, xx, dxmm,c 

def outliers(x, bar = 2):
    xmean = np.mean(x)
    var = xmean * bar
    xn = []
    for i in x:
        if abs(i) > var: 
            xn.append(xmean)
        else:
            xn.append(i)           
    return xn 
                    
def moveave(vec, n=2):    
    ans = []; i=0
    while i < len(vec) - n + 1:
        window = vec[i : i+n]        
        ans.append(np.sum(window) / n)
        i += 1
    return ans

counter = 0 
for record in var:
    print(record)
    record_path = os.path.join(path,record)
    steps, dt, pressure, massfraction, phi = read_metadata(record_path)
    time_, point, speed, _ = curve(os.path.join(record_path, save_folder), int(steps), dt, rround = 4)
    #input_info = np.array([["pressure", "massfraction","phi"], [pressure, massfraction, phi]])
    input_info = np.array([float(pressure),float(massfraction), float(phi)])
    if not os.path.isdir(path+"/results/"+record):
        os.mkdir(path+"/results/"+record)

    name = path+"/results/"+record+"/time.txt"
    with open(name, "a") as namei: 
        np.savetxt(namei, time_); namei.write("\n") 

    name = path+"/results/"+record+"/point.txt"
    with open(name, "a") as namei: 
        np.savetxt(namei, point); namei.write("\n") 

    name = path+"/results/"+record+"/speed.txt"
    with open(name, "a") as namei: 
        np.savetxt(namei, speed); namei.write("\n") 

    name = path+"/results/"+record+"/inputs.txt"
    with open(name, "a") as namei: 
        np.savetxt(namei,input_info); namei.write("\n")

    print(f"Progress {counter}/{len(var)} ")
    counter+=1 
