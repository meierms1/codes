#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:15:24 2022

@author: mmeierdo
"""
name = "/home/mmeierdo/solidphase/BulkBashPureAP.sh"

ap = [50.0,100.0,200.0,300.0,400.0,500.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0,2000.0,2200.0,2400.0,2600.0,2800.0,3000.0]

htpb = [3000]
comb = [-300.0]

local = "/home/mmeierdo/solidphase/PureAP/output"

P = [0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0]

var1 = "pressure.P"
var2 = "thermal.mlocal_comb"
var3 = "thermal.mlocal_htpb"
var4 = "thermal.mlocal_ap"

var1 =  " " + var1 + "= "; var2 =  " " + var2 + "= "; var3 =  " " + var3 + "= "; var4 =  " " + var4 + "= "; 

standart = "mpirun -np 8 ~/alamo/bin/alamo-2d-g++ ~/alamo/inputb "
n = 0
with open(name, "w") as namei:
    
    for i in ap:
        for j in htpb:
            for k in comb:
                for p in P:
                    n += 1
                    namei.write(standart + var1 + str(p) + var2 + str(k) + var3 + str(j) + var4 + str(i) + " plot_file=" + local + "; notify-send: Done" +str(n)+ " \n")
    
print(n)