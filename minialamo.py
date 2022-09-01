#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:54:38 2022

@author: mmeierdo
"""

from PythonV import *
import numpy as np 

def polynomial(w0, w1, w12):
    v0 = w0
    v1 = 0.0
    v2 = -5.0 * w1 + 16 * w12 - 11 * w0
    v3 = 14 * w1 - 32 * w12 + 18 * w0
    v4 = -8 * w1 + 16 * w12 - 8 * w0
    return [v0,v1,v2,v3,v4]    
    

def eta(etaold, dt, mob, red):
    return etaold - mob * dt * red
    
def heat(ql, P, alpha, phi, a1,a2,a3, b1, b2,b3, c1,z1,z2):
    k1 = a1 * P + b1 - (z1 / z2)
    k2 = a2 * P + b3 - (z1 / z2)
    k3 = np.log((c1 * P ** 2 + a3 * P + b3) - k1 / 2 - k2 / 2 ) / 0.25
    
    m1 = 1
    m2 = 1 
    m3 = 1 
    
    qflux = m1 * k1 * phi + m2 * k2 * (1 - phi) + m3 * (z1 / z2) * np.exp(k3 * phi * (1 - phi))
    
    qdot = ql + qflux / 10 / alpha 
    
    return qdot

def temp():
    pass

def mass(etaold, etanew, dt, rho):
    return -rho * (etanew - etaold) / dt

def alpha(etaold, k, rho, cp):
    return etaold * k / rho / cp

def mob(P, T, E1, E2, E3, A1, A2, A3, phi):
    p1 = (A1 + P/100) * P * np.exp(- E1 / T) * phi 
    p2 = A2 * np.exp(-E2 / T) * (1 - phi)
    p3 = A3 * P * np.exp(-E3 / T) * phi * (1 - phi)
    return p1 + p2 + p3


