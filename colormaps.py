#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:08:34 2023

@author: mmeierdo
"""
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np 

lsc = plt.get_cmap("coolwarm", 6)
col = []
for i in range(lsc.N):
    col.append(colors.rgb2hex(lsc(i)[:3]))

col = np.flip(col)
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=col)