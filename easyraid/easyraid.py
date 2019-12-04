#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Nov. 2019
	
	Electric Dynamic Chapter 5

	@author: ZYW @ BNU
'''
import numpy as np
import matplotlib.pyplot as plt

def E2E(l,P_tt,pixels):
	E  = np.zeros(shape=(pixels,pixels),dtype='float')
	xx = np.linspace(-1*pixels//2,pixels//2,pixels)
	yy = np.linspace(-1*pixels//2,pixels//2,pixels)
	x,y = np.meshgrid(xx,yy)
	k = 2*np.pi/l
	R = abs(x+y*1.0j)
	E = P_tt*(np.cos(k*R))*x/R**2/4/np.pi
	return E

def E2B(l,P_tt,pixels):
	B = np.zeros(shape=(pixels,pixels),dtype='float')
	xx = np.linspace(-1*pixels//2,pixels//2,pixels)
	yy = np.linspace(-1*pixels//2,pixels//2,pixels)
	x,y = np.meshgrid(xx,yy)
	k = 2*np.pi/l
	R = abs(x+y*1.0j)
	B = P_tt*(np.cos(k*R))*x/R**2/4/np.pi
	return B

def E4H(Q,l,omega,plots):
	theta = np.linspace(0.001,2*np.pi,plots)
	r_0 = 36*Q**2*l**4*omega**6
	r = r_0*(np.cos(theta)*np.sin(theta))**2
	return theta,r

def Atenna(N,wavelength,l,plots):
	k = 2*np.pi/wavelength
	theta = np.linspace(0.001,2*np.pi,plots)
	r_0 = (np.cos(np.pi*np.cos(theta)/2)/np.sin(theta))**2
	r = r_0*(np.sin(N*k*l*np.cos(theta)/2)/np.sin(k*l*np.cos(theta)/2))**2
	return theta,r


