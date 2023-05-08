#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:15:24 2022

@author: mmeierdo
"""
import numpy as np

name = "/home/mmeierdo/solidphase/BulkBashAP.sh"

def mf(vf):
    return (vf * 1957) / (vf * 1957 +(1-vf) * 920)

P =  [1.0, 2.0, 3.0, 4.0, 6.0]

local = "/home/mmeierdo/solidphase/zeropressure/output"

var1 = "pressure.P"
var1 =  " " + var1 + "=";

standart = "mpirun -np 8 ~/alamo/bin/alamo-2d-g++ ~/alamo/inputap"
n = 0
with open(name, "w") as namei:    
    for p in P:
        namei.write(standart + var1 + str(p) + " plot_file=" + local + "; notify-send Done" +str(n)+ "; \n")
        n += 1
print(n)



