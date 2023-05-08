#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:15:24 2022

@author: mmeierdo
"""
import numpy as np
import matplotlib.pyplot as plt
def mf(vf):
    return (vf * 1957) / (vf * 1957 +(1-vf) * 920)

loc = ["1","2","3","4","5"]
loc1 = ["/home/mmeierdo/SpherePackTools/NewPacks/" +i + "/volumes" for i in loc]
loc2 = ["/home/mmeierdo/SpherePackTools/NewPacks/" +i + "/pack3d.out" for i in loc]

vol = []
r = [[],[],[],[],[]]
for i in loc1:
    data = [line.strip() for line in open(i, 'r')]
    data = data[0]
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.split(",")
    data = [float(j) for j in data]
    data = [mf(j) for j in data]
    vol.append(data)

vol = np.reshape(vol, (-1,1))
print(vol)
plt.figure()
plt.hist(vol)

c=0
for i in loc2:
    f = np.loadtxt(i)
    for j in f:
        r[c].append(j[3])
    c+=1

for i in r:
    plt.figure()
    plt.hist(i)





plt.show()


