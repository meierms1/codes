#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:20:52 2022

@author: meierms
"""
import numpy as np
import matplotlib.pyplot as plt
from CURVE import curve

htime, hm, hspeed, c = curve("output_htpb")
hmean = np.mean(hspeed)
aptime, apm, apspeed, c = curve("output_pureap")
apmean = np.mean(apspeed)
mtime, mpm, mspeed, c = curve("output_mix")
mmean = np.mean(mspeed) 

print(hmean)
print(apmean)
print(mmean)

plt.figure()
plt.plot(htime, hm, label = "htpb")
plt.plot(aptime, apm, label = "AP")
plt.plot(mtime, mpm, label = "comb")
plt.legend()
plt.xlabel("time [s]")
plt.ylabel("Location [m]")
plt.title("Interface Location")


plt.figure()
plt.plot(htime[:-1], hspeed, label = "HTPB")
plt.plot(aptime[:-1], apspeed, label = "AP" )
plt.plot(mtime[:-1], mspeed, label = "comb")
plt.legend()
plt.xlabel("time [s] ")
plt.ylabel("velocity [mm/s]" )
plt.title("burn rate" )