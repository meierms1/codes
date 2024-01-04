#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:15:06 2023

@author: meier
"""
import numpy as np 
import matplotlib.pyplot as plt

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def moving_averages(x, n):
    return np.convolve(x, np.ones(n), 'valid') / n

dirs = ['output-anchor','output-double-circle','output-simple-circle','output-star']

home = "/home/meier/Paper_Scitech/"
file = "/area.curve"
sv = [home for i in dirs]
dirs = [home + i + file for i in dirs]

data = [] 

n=10


for i in dirs:
    data.append(np.loadtxt(i))
    
first = data[0]
x,y = first[:,0], first[:,1]
plt.figure()
plt.plot(x,y, c="black")
plt.ylabel("Surface Area [m]")
plt.xlabel("Timestep [-]")
plt.title("Anchor")
plt.grid()
plt.savefig(fname= sv[0] + "/anchor.pdf", dpi = 600, format = "pdf")

first = data[1]
x,y = first[:,0], first[:,1]
plt.figure()
plt.plot(x,y,c="black")
plt.ylabel("Surface Area [m]")
plt.xlabel("Timestep [-]")
plt.title("Double Circle")
plt.grid()
plt.savefig(fname= sv[1] + "/doublecircle.pdf", dpi = 600, format = "pdf")

first = data[2]
x,y = first[:,0], first[:,1]
plt.figure()
f = 10
plt.plot(x[:-f],y[:-f], c="black")
plt.ylabel("Surface Area [m]")
plt.xlabel("Timestep [-]")
plt.title("Simple Circle")
plt.grid()
plt.savefig(fname= sv[2] + "/simplecircle.pdf", dpi = 600, format = "pdf")

first = data[3]
x,y = first[:,0], first[:,1]
plt.figure()
plt.plot(x,y, c="black")
plt.ylabel("Surface Area [m]")
plt.xlabel("Timestep [-]")
plt.title("Star")
plt.grid()
plt.savefig(fname= sv[3] + "/star.pdf", dpi = 600, format = "pdf")
