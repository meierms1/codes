#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 08:44:16 2022

@author: mmeierdo
"""
a = {} 
with open("input") as f:
    for line in f: 
        if line[0] != "#" and line[0] != "\n" and line[0] != " ":
            #print(line)
            k,v = line.split(" = ")
            v = v.split(" #")[0]
            a[k] = v
            
special = ["geometry.prob_lo", "geometry.prob_hi", "amr.n_cell", "phi.ic.laminate.center"]
for i in a.keys():
    a[i] = a[i].replace("\n", "")
    if " " in a[i]:
        if i not in special:
            a[i] = a[i].replace(" ", '')
     
k = []
for i in a.keys():
    temp = i.replace(".", "_")
    k.append(temp)

j = 0   
for i in a.keys(): 
    if a[i][0] >= '0' and a[i][0] <= '9':
        if ' ' in a[i]:
            hold = a[i].split(" ")
            #print(hold)
            exec("%s = %f" % (k[j]+"_x", float(hold[0]) ) )
            exec("%s = %f" % (k[j]+"_y", float(hold[1]) ) )
            exec("%s = %f" % (k[j]+"_z", float(hold[2]) ) )
        else:
            exec("%s = %f" % (k[j], float(a[i]) ) )
    else:
        exec("%s = %r" % (k[j],a[i]) )
    j += 1


