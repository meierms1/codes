#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:15:24 2022

@author: mmeierdo
"""
#name = "/home/mmeierdo/solidphase/BulkBashSandwich.sh"
name = "/home/mmeierdo/solidphase/BulkBashPureAP.sh"

P = [1.0, 2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0] #[1.0, 2.0, 4.0]
c1 = [12000.0] #[0, 12000.0,20000.0,25000.0, 27000]
c2 = [int(1)] #[0.01,0.001,0.0001,0.1]
c3 = [10]#[1.4e3,1.4e4,1.4e5]
c4 = [1.45e8]


local = "/home/mmeierdo/solidphase/PureAP3/output"

var1 = "pressure.P"
var2 = "thermal.mlocal_ap"
var3 = "pressure.mob_ap"
var4 = "thermal.modeling_ap"
var5 = "thermal.m_ap"

var1 =  " " + var1 + "= "; var2 =  " " + var2 + "= "; var3 =  " " + var3 + "= "; var4 =  " " + var4 + "= "; var5 = " " + var5 + "=";

standart = "mpirun -np 8 ~/alamo/bin/alamo-2d-g++ ~/alamo/inputap"
n = 0
with open(name, "w") as namei:
    
    for i in c3:
        for j in c2:        
            for k in c1:
                for p in P:
                    for q in c4:                    
                        n += 1
                        namei.write(standart + var1 + str(p) + var2 + str(k) + var3 + str(j) + var4 + str(i) + var5 + str(q) + " plot_file=" + local + "; notify-send Done" +str(n)+ "; \n")


print(n)
