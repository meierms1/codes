#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:43:25 2022

@author: meierms
"""

import sys 
import numpy as np
import getpass 

def curve(fld, drt = "contourCurves", subfile ="outs2", rround = 2, smooth=False, nread = 2):
    usr = getpass.getuser()

    path = "/home/"+usr+"/alamo/inputs/Scitech/"+ fld +"/" 
    #path = "/home/meier/fs/" + fld + "/"
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
    #print(a.keys)
    if "amr.plot_dt" in a.keys():
        deltat = float(a["amr.plot_dt"])
    else: 
        deltat = float(a["amr.plot_int"]) * float(a["timestep"])
        
    if a["Status"][0] == "C":
        steps = int(float(a["stop_time"]) / deltat)
        #steps = int(10000)
    else:
        g = ""
        for i in a["Status"]:
            if i <= '9' and i >= '0':
                g += i 
        steps = int(float(g) / 100 * float(a["stop_time"]) / deltat)

    dt = deltat

    try: 
        print("zeta: ", a["phi.zeta_0"])
    except: 
        pass
    print("Pressure: ", a["pressure.P"])
    print("Type: ", a["phi.ic.type"])
    print("N. Steps: " ,steps)
    #print("Mass Fraction: ", a["thermal.massfraction"])
    print("dt:", dt)

    xtime = [0.0]
    time = []

    for i in range(steps+1):
        time.append(round(dt*i, rround))

    c = 0
    listtrack=[]
    for i in range(steps):
        if i < 10: 
            add = "000"
        elif i < 100 and i >=  10:
            add = "00"
        elif i < 1000 and i >= 100:
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
    for i in range(steps):
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

def reader(drt, steps, dt, rround = 2):
    usr = getpass.getuser()
    path = "/home/"+usr+"/alamo/inputs/review/log/contourCurves_" + drt 
    xtime = [0.0]
    time = []
    c = 0
    for i in range(steps+1):
        time.append(round(dt*i, rround))
        
    for i in range(steps):
        if i < 10: 
            add = "000"
        elif i < 100 and i >=  11:
            add = "00"
        elif i < 1000 and i > 101:
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
            xtime.append(0.0)
            c += 1

    xx = [1000 * i for i in xtime]

    dx = []
    for i in range(steps):
        value = (xtime[i+1] - xtime[i]) / dt
        dx.append(value)        
    dxmm = [i*1000 for i in dx]          
    return time, xx, dxmm,c