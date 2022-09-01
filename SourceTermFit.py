#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 08:57:32 2022

@author: maycon
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from scipy.integrate import simpson as sp 

p = [0.1, 1, 2, 6, 10] ## MPa Units, Accepts: [0.1, 1, 2, 6, 10] 
def fitline(P, xx, low, high):
    k1 = 0.46 * P + 0.42 - 1
    k2 = 1.14 * P + 0.323 - 1 
    k3 = 1.0

    a = 1.0
 
    max_fun = -0.0990568*P**2 + 2.79722*P + 0.322469 #1.713 * P + 1.98

    k4 = np.log(max_fun - k2/2 - k1/2) / (0.5*(1-0.5))

    phi = np.linspace(0,1, 101)

    fun = lambda i:  (k1) * i + (k2) * (1-i) + k3 * np.exp(k4 * i * (1 - i) / a) 

    y = [fun(i) for i in phi]
    
    z = []
    for i in xx:
        val = i
        if i < low:
            phi = 1
        elif i > high: 
            phi = 0
        else: 
            phi = 1 - (( low - val ) * (1 - 0) / (low - high) )
        z.append(fun(phi))
        
    return y, z

df = pd.read_csv("heatfluxdata2.csv", dtype=np.float64, skiprows=1)

df_1atm_x =   df.values[:108,8]
df_1atm_y =   df.values[:108,9]

df_10atm_x =  df.values[:50,6]
df_10atm_y =  df.values[:50,7]

df_20atm_x =  df.values[:91,4]
df_20atm_y =  df.values[:91,5]

df_60atm_x =  df.values[:113,2]
df_60atm_y =  df.values[:113,3]

df_100atm_x = df.values[:171,0]
df_100atm_y = df.values[:171,1]

a = 1.0 

for P in p: 

    if P == 10:
        xx = df_100atm_x
        yy = df_100atm_y
        low  = 200 - 10 * a**2.6
        high = 200 + 10 * a**2.6
    elif P == 6: 
        xx = df_60atm_x
        yy = df_60atm_y
        low  = 200 - 13 *a**2
        high = 200 + 10 * a**2
    elif P == 2:
        xx = df_20atm_x
        yy = df_20atm_y
        low = 180
        high = 220
    elif P == 1:
        xx = df_10atm_x
        yy = df_10atm_y
        low = 165
        high = 225
    elif P == 0.1:
        xx = df_1atm_x
        yy = df_1atm_y
        low = 190
        high = 210
        
    y,z = fitline(P, xx, low, high)
    plt.plot(xx, yy, label = "Experiment "+str(P)+"MPa" , c = "black" )
    plt.plot(xx, z, label = "Model "+str(P)+"MPa" , ls = "-.")
plt.legend(prop={'size': 9}) 
plt.xlabel("Spacial Variable" ) 
plt.ylabel("Heat Flux - [kW / cm^2]" )
plt.title("Heat Flux Data Fitting")
plt.savefig("EpsFit", format = "eps" )
plt.savefig("PngFit", format = "png" )

'''    
int_exp = sp(yy,xx)    
int_mod = sp(z,xx)
error = 100 * abs(int_exp - int_mod) / int_exp 
print("Data Integral: "  + str(int_exp))
print("Model Integral: " + str(int_mod))
print("%Error: " + str(error))

plt.figure()
plt.plot(xx, yy, label = "experiment", c = "black" )
plt.plot(xx, z, label = "Model", c = "red" , ls = "-.")
plt.legend()
plt.xlabel("Spacial Variable" ) 
plt.ylabel("Heat Flux - [kW / cm^2]" )
plt.title("Model Fit" )
plt.figtext(0.14, 0.7, "Integral %Error " + str(round(error, 2)))
''' 
    