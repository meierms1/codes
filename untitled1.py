#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 10:16:42 2022

@author: mmeierdo
"""
import numpy as np
import matplotlib.pyplot as plt

phi = 0.5
P = [0.5,0.8,1.0,2.0, 3.0, 4.0]
rate = [1.79,1.98,2.15,3.04,4.1,5.4]
T = [400,600,800,1000,1200,1400,1600]

m_ap = 1.1
m_h = 0.5
m_c = 13.0

E_ap = 1050
E_h = 1200
E_c = 1200

zn = [] 
mb = []
for j in T:
    z = []
    m = []
    exp_ap = - E_ap / j
    exp_h = - E_h / j
    exp_c = - E_c / j
    
    for i in range(len(P)):
        p = P[i]
        er = rate[i]
        mm_ap = (m_ap + p / 100) * p * np.exp(exp_ap) * phi 
        mm_h = m_h * np.exp(exp_h) * (1.0 - phi) 
        mm_c = m_c * p * np.exp(exp_c) * phi * (1.0 - phi) 

        m.append(mm_ap + mm_h + mm_c)
        r = ( - m_ap - m_h + er ) / (np.exp(exp_c) * phi * (1.0 - phi) ) 
        z.append(r)
    mb.append(m)
    zn.append(z)
    
for k in range(len(P)):
    plt.plot(P,zn[k], label = str(T[k]))
plt.legend()
  
plt.figure()
plt.plot(P, zn[3])

