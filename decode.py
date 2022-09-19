#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:55:07 2022

@author: mmeierdo
"""

import crypt  
import random, string
from itertools import permutations as pt
import multiprocessing

h1 = '$6$PTt8xM3Y$J8kwCgtZ3f/WTAf.DFhD1JBi8Dgy0Bn2X5Ko3RwdhMjhquHDM8h9y42pC64gwRWYKqP.EQ3.5xjjxpNj4QiSx1' 
h2 = '$6$CjIbw9/f$ZYw7UZ9l7jeKYp9JUxgLso4WOlm64DKSRcav.8S4cE8GGf3YgJXQJdUXHfZWcgJV.r1x.NUryz2UVUzx3Nu.O.' 
h3 = "$6$uRwire5y$fB87R49nB5V7NFDv0cQx0/wnqioQ.LMshax7vChCNxyWNfwrOT8DLp8nPuJByo3GrrFBikVUsvL2ceO.GTL0O."
w = 'berfomet'

s = '$6$PTt8xM3Y$J8kwCgtZ3f' 
s2 = '$6$CjIbw9' 
s3 = "$6$uRwire5y$"

alp = string.printable[10:36]
charL = 8

def generate(charL):
    outs = '' 
    while len(outs) < charL:
        outs += random.choice(alp)
    print(outs)
    return outs

def conv(tp):
    f = "" 
    for i in tp:
        f += i
    return f


for i in pt(alp, charL):
    guess = conv(i)
    print(guess)
    v = crypt.crypt(guess, salt = s)
    if v == h1:
        print(guess)
        break 

    
    
