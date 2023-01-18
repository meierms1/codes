#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:54:02 2022

@author: mmeierdo
"""
import simba 

db = simba.open()
table = db.getTable("PureAP")
records = table.get()
namelist = [] 
for record in records:
    fld = record['DIR']
    namelist.append(fld)
    
print(namelist)