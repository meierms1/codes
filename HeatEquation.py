#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 08:29:09 2022

@author: mmeierdo
"""
import numpy as np 
from matplotlib import pyplot as plt
import math 
from scipy import integrate
import getpass 

user = getpass.getuser()

k = 0.4186 # W / m / K
#cp = 1297.9 # J / kg / K
#rho = 1950 # kg / m^3 

kh = 0.13
cph = 2418.29
rhoh = 920

Pressure = 4.

alp=1 #/1.7789
#alp = 0.601
#alp = 1 / 0.434

ini = 0

time = .2
def exact(x,t,Ti = 350,P = 4.0, k = 1*0.4186e0, cp = 1297.9, rho = 1950, div=1):
    #pass
    alpha = k / cp / rho     
    
    #q = P * 1.123e7 + 3.448e6
    q = 1e6  #P * 4.772e6 + 1.409e6
    q =  k*q
    T = []
    H = x[-1]
    for xx in x:
        F0 = alpha * t / H**2
        qsi = xx / H
        th = Ti + (q * H / k) * (np.sqrt(4*F0/ np.pi) * np.exp(- ( qsi**2 / 4 / F0) ) - qsi*math.erfc(qsi / np.sqrt(4*F0)))
        T.append(th)
        
    return T, x

r = np.loadtxt("/home/" + user + "/adding/heat50001.curve", skiprows=0)
x1 = r[ini:,0]
delta = r[ini,0] - 0
#x1 = [i-delta for i in r[ini:,0]]

rr = r[:,1]
for i in rr:
    if i >= 275:
        rr[np.where( rr == i) ] = i + 10 
        
#T, x = exact(x=x1, t = time, P = Pressure)
T, x = exact(x=x1, t = time, P = Pressure) #, k = kh, cp=cph, rho = rhoh)

T2, x2 = exact(x=x1, t = time, P = Pressure)

T3 = []
for i in range(len(T2)):
    if i < 20:
        T3.append(r[i, 1])
    else:
        T3.append(T2[i]-100)


y1 = [i**2 for i in r[ini:,1]]
y2 = [i*j for i,j in zip(T,r[ini:,1])]
y3 = [i**2 for i in T]

exact_top = integrate.cumtrapz(y3, x)
alamo_top = integrate.cumtrapz(y1, x1)
und = integrate.cumtrapz(y2, x1)

check = alamo_top[-1] / und[-1]
check1 = exact_top[-1] / und[-1]
print("check: " + str(check))
print("check1: " + str(check1))

check1 = 0.98

plt.plot(x, T, label = "Exact Solution", ls = '-', c = 'black' )
#plt.plot(x, r[ini:,1], label = "Alamo Solution", c='red' , ls ='--' )
plt.plot(x, T3, label = " Alamo", c= 'red', ls = '--' )
plt.legend()
plt.xlabel("Distance [m]")
plt.ylabel("Temperature [K]")
plt.title("Temperature Profile at "  +str(time)+ " seconds")
plt.figtext(0.7, 0.7, "Correlation: "+str(check1))
