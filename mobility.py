#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:35:24 2022

@author: meierms
"""

import numpy as np
import matplotlib.pyplot as plt

end = 1500

T = np.linspace(270, end, end - 270)

n = 1 # [1,2,3,4,5]

P = 4
pp = 4

E = 11000.0

m = 1.45e5

mob = lambda i,j: m * P**i * np.exp(-E / j)

po =lambda i: 1.22 * i**1.042 

tt = []
for i in T:
    j = mob(n, i)
    if j <= 20:
        tt.append(j)
    else:
        tt.append(20)
ref = [po(pp) for i in T]

plt.figure()
plt.plot(T, mob(n, T), label = "Arrhenius Law")
plt.plot(T, tt, label = "cut")
plt.plot(T, ref, label = "Power Law")
plt.xlabel("Temperature")
plt.ylabel("Mobility")
plt.title("Pressure = 4MPa")
plt.legend()

print(po(pp))
print(mob(n, 950))
