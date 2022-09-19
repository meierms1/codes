#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:59:45 2022

@author: meierms
"""
import matplotlib.pyplot as plt

P = [0.5, 2, 4, 6]

R1 = [1.916,3.364,6.391,11.93]
R2 = [1.76,3.18,6.23,11.85]

E = [1.793,3.03,5.27] 

plt.loglog(P[:-1], E, "--o",label = "Knot Results")
#plt.loglog(P, R1)
plt.loglog(P[:-1], R2[:-1], "--s", label = "Alamo Results")
plt.legend()
plt.xlabel("Pressure")
plt.ylabel("Flame Speed")
plt.title("loglog plot P x Speed")