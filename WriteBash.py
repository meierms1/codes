#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:15:24 2022

@author: mmeierdo
"""
import numpy as np

name = "/home/mmeierdo/solidphase/BulkBashheat.sh"
name = "/home/mmeierdo/Paper_Folder/BulkBash.sh"
def mf(vf):
    return (vf * 1957) / (vf * 1957 +(1-vf) * 920)

loc = ["60","65","70","75","80"]
loc = ["/home/mmeierdo/SpherePackTools/NewPacks/" +i + "/volumes" for i in loc]

vol = []
for i in loc:
    data = [line.strip() for line in open(i, 'r')]
    data = data[0]
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.split(",")
    data = [float(j) for j in data]
    data = [mf(j) for j in data]
    vol.append(data)


P =  [1.0, 2.0, 3.0, 4.0]
c2 = [1.0e2, 1.0e3, 1.0e4,1.0e5, 1.0e6] 
c1 = [] #[0.01,0.001,0.0001,0.1]
c3 = [40.0,100.0,200.0,300.0]#[1.1114e3,1.4e4,1.4e5]
c4 = [1.51e4, 1.51e5, 1.51e6]


local = "/home/mmeierdo/Paper_Folder/results/updated2d/output"

var1 = "pressure.P"
var2 = "phi.ic.psread.filename" 
var3 = "laser.ic.expression.region0"
var4 = "thermal.m_comb"
var5 = "thermal.massfraction"

var1 =  " " + var1 + "="; var2 =  " " + var2 + "="; var3 =  " " + var3 + "="; var4 =  " " + var4 + "="; var5 = " " + var5 + "=";

standart = "mpirun -np 8 ~/alamo/bin/alamo-2d-g++ ~/alamo/inputpack"
n = 0
para = []
#for i in range(2,3): 
for k in [60,65,70,75,80]:
    if k == 60: i = 1
    elif k == 65: i = 2
    elif k == 70: i = 3
    elif k == 75: i = 4
    elif k == 80: i = 5
    for j in [12,13,14,15,16,17,18,19]:
        var = "/home/mmeierdo/SpherePackTools/NewPacks/"+ str(k) +"/"+ str(j) +".xyr"
        c1.append(var)
        if vol[i-1][j-12] <= 0.8:
            para.append(vol[i-1][j-12])
        else:
            para.append(0.8)
    for j in [1,2,3,4,5,6,7,8]:
        var = "/home/mmeierdo/SpherePackTool/NewPacks/"+str(k)+"/"+str(j)+".xyr"
        c1.append(var)
        if vol[i-1][j-1] <= 0.8:
            para.append(vol[i-1][j-1])
        else:
            para.append(0.8)
    
c2 = ["'(t<0.05)*(t>0.005)*" + str(i)+"'" for i in c2] 

with open(name, "w") as namei:    
    for p in P:
        for i,j in zip(c1,para):
            n += 1
            namei.write(standart + var1 + str(p) +var2+i+var5+str(j)+ " plot_file=" + local + "; notify-send Done" +str(n)+ "; \n")
            #namei.write(standart + var1 + str(p) + " plot_file=" + local + "; notify-send Done" +str(n)+ "; \n")


print(n)



