#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:59:45 2022

@author: meierms
"""
import matplotlib.pyplot as plt

P = [0.5, 2, 4, 6]
P_ap = [2,3,4,6]

R1 = [1.916,3.364,6.391,11.93]
R2 = [1.76,3.18,6.23,11.85]
R_ap = [2.58,3.75,5.2,9.73]

E = [1.793,3.03,5.27] 
E_ap = [2.48,3.77,5.098,7.7]

plt.loglog(P[:-1], E, "-o",label = "AP/HTPB - Knot Results")
plt.loglog(P[:-1], R2[:-1], "--s", label = "AP/HTPB - Alamo Results")

plt.loglog(P_ap, E_ap, "-o", label = "Pure AP - Knot Results")
plt.loglog(P_ap, R_ap, "--s", label = "Pure AP - Alamo Results")

plt.legend()
plt.xlabel("Pressure")
plt.ylabel("Flame Speed")
plt.title("loglog plot P x Speed")