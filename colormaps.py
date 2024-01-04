#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:08:34 2023

@author: mmeierdo
"""
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np 

lsc = plt.get_cmap("coolwarm", 8)
lsc = plt.get_cmap("coolwarm", 24)

col = []
for i in range(lsc.N):
    col.append(colors.rgb2hex(lsc(i)[:3]))

print(col)
if (False):
    i = 0; j = 3
#col = np.flip(col)
    while i < j:
        col[i], col[j] = col[j], col[i]
        i+=1
        j-=1
    i=0; j=3
    while i<4:
        if (i%2):
            col[i], col[j] = col[j], col[i]
            i+=1
            j+=1
        
if (True):
    col = [col[0],col[3],col[20], col[23]]
    col2 = []
    for i in col:
        col2.append(i)
        col2.append(i)
    col = col2
print(col)    
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=col)