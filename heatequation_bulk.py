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

def exact(x,t,Ti = 300,P = 4.0, k = 1*0.4186e0, cp = 1297.9, rho = 1950, div=1):
    alpha = k / cp / rho     
    q = 1e6  
    q = k * q
    T = []
    H = x[-1]
    for xx in x:
        F0 = alpha * t / H**2
        qsi = xx / H
        th = Ti + (q * H / k) * (np.sqrt(4*F0/ np.pi) * np.exp(- ( qsi**2 / 4 / F0) ) - qsi*math.erfc(qsi / np.sqrt(4*F0)))
        T.append(th)
        
    return T, x


def alamo(name, time, ini=0, Pressure = 4.0):
    r = np.loadtxt(name, skiprows=0)
    x1 = r[ini:, 0] 
    rr = r[:,1]    
    T, x = exact(x=x1, t=time, P=Pressure)   
    T2, x2 = exact(x=x1, t = time, P = Pressure)   
    return T, rr, x
    

def check(T, r, x, x1):
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
    
    return check, check1

k = 0.4186 # W / m / K
Pressure = 4.
alp=1 

ini = 0
time = [.5,.4,.3,.2,.1,0.01]
time = [i - 0.00 for i in time]
files = ["/home/" + user + "/adding/heat50000.curve",
         "/home/" + user + "/adding/heat50001.curve",
         "/home/" + user + "/adding/heat50002.curve",
         "/home/" + user + "/adding/heat50003.curve",
         "/home/" + user + "/adding/heat50004.curve",
         "/home/" + user + "/adding/heat50005.curve",
         ]


c = ['orangered','darkorange','gold','yellowgreen','seagreen', "lightseagreen"] 
cc = 0
for i,j in zip(files, time):
    T,r,x = alamo(i,j)  
    if cc == 0:
        plt.plot(x, T, label = "Exact Solutions", ls = '-', c = 'black' )
    else:
        plt.plot(x, T, ls = '-', c = 'black' )
    plt.plot(x, r, label = str(j) + "s Alamo Solution", c= c[cc], ls = '-.' )
    cc += 1


plt.legend()
plt.xlabel("Distance [m]")
plt.ylabel("Temperature [K]")
#plt.title("Temperature Profile at "  +str(time)+ " seconds")
plt.savefig(fname="/home/mmeierdo/heat",format="pdf", dpi=600)
plt.grid()
#plt.figtext(0.7, 0.7, "Correlation: "+str(check1))

#rr = r[:,1]
#for i in rr:
#    if i >= 275:
#        rr[np.where( rr == i) ] = i + 10 
        

#T3 = []
#for i in range(len(T2)):
#    if i < 20:
#        T3.append(r[i, 1])
#    else:
#        T3.append(T2[i]-100)