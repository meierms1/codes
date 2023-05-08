#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:01:34 2023

@author: mmeierdo
"""
import matplotlib.pyplot as plt

P_alamo = [3.02,4.37,7.3]
P_real = [2.5,5.1,7.8]

P = [2.0,4.0,6.0]



plt.plot(P, P_alamo, label = "Alamo")
plt.plot(P, P_real, label = "Data")
plt.xlabel("Pressure [MPa]")
plt.ylabel("Burn Rate [mm/s]")
plt.legend()
