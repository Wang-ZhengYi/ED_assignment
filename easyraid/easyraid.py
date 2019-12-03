#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Nov. 2019
	
	Electric Dynamic Chapter 5

	@author: ZYW @ BNU
'''
import numpy as np
import matplotlib.pyplot as plt

def E2E(c,eps,pixels,l,P_tt):
	E = np.zeros(shape=(pixels,pixels),dtype='float')
	R = np.zeros(shape=(pixels,pixels),dtype='float')
	c = 1#speed of light
	eps = 1#vaccum dielectirc number
	perc_2e = 4*np.pi*eps*c**3
	xx = np.linspace(-1*pixels//2,pixels//2,pixels)
	yy = np.linspace(-1*pixels//2,pixels//2,pixels)
	x,y = np.meshgrid(xx,yy)
	k = 2*np.pi/l
	R = abs(x+y*1.0j)
	E = P_tt*(np.cos(k*R))*x/R**2/perc_2e
	return E

def E2B(c,eps,pixels,l,P_tt):
	B = np.zeros(shape=(pixels,pixels),dtype='float')
	c = 1#speed of light
	eps = 1#vaccum dielectirc number
	perc_2b = 4*np.pi*eps*c**2
	xx = np.linspace(-1*pixels//2,pixels//2,pixels)
	yy = np.linspace(-1*pixels//2,pixels//2,pixels)
	x,y = np.meshgrid(xx,yy)
	k = 2*np.pi/l
	R = abs(x+y*1.0j)
	B = P_tt*(np.cos(k*R))*x/R**2/perc_2b
	return B

# def Atenna(N,theta,l)