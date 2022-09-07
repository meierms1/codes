#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:19:12 2022

@author: maycon
"""

import sys

read = "google" #sys.argv[0]
var = read.lower()

num2 = ["a", "b", "c"]
num3 = ["d", "e", "f"]
num4 = ["g", "h", "i"]
num5 = ["j", "k", "l"]
num6 = ["m", "n", "o"]
num7 = ["p", "q", "r", "s"]
num8 = ["t", "u", "v"]
num9 = ["w", "x", "y","z"]
num0 = ["+"]

vowel = ["a", "e", "i", "o", "u"]

var1 = []
var2 = []
var3 = []

for i in var:
    if i in num2:
        var1.append(2)
    elif i in num3:
        var1.append(3)
    elif i in num4:
        var1.append(4)
    elif i in num5:
        var1.append(5)
    elif i in num6:
        var1.append(6)
    elif i in num7:
        var1.append(7)
    elif i in num8:
        var1.append(8)
    elif i in num9:
        var1.append(9)
    elif i in num0:
        var1.append(0)
    else:
        var1.append(i)
        
    if i in vowel: 
        var2.append(i.upper())
    else:
        var3.append(i)
   
if len(var) >= 4:
    ad = ["-"]
else:
    ad = []
    for i in range(5-len(var)):
        ad.append("-")
    
ovar = var3 + var2 + ad + var1
ov = "" 
for i in ovar:
    ov = ov + str(i)

print(ov)


    

    