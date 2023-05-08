#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:15:24 2022

@author: mmeierdo
"""
#name = "/home/mmeierdo/solidphase/BulkBashSandwich.sh"
name = "/home/mmeierdo/solidphase/BulkBashAP.sh"

P = [0.8, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0]
var1 = " pressure.P="

tandart = "mpirun -np 8 ~/alamo/bin/alamo-2d-g++ ~/alamo/inputpack"
n = 0
with open(name, "w") as namei:    
    for p in P:
        n += 1
        namei.write(tandart + var1 + str(p)+";\n")


print(n)



