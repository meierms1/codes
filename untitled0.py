#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 09:09:26 2022

@author: maycon
"""

import numpy as np
import matplotlib.pyplot as plt

n = "60pack"

A = 1.45e5
E = 11000
t1 = 300/1000
t2 = 2000/1000

T = np.linspace(t1, t2, 60)

mob =lambda e, a:  a * np.exp(-e / T)
#plt.plot(T, mob(7500,1.03e3), label = "1")
plt.plot(T, mob(11,1.45e2), label = "2" )
#plt.plot(T, mob(11000,1.45e2), label = "2" )
plt.legend()