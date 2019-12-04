#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	Created on Sept 2019

	Elecetric Dynmatic Chapter 2
	
	@author: Z.Y.Wang @ BNU
	'''

import numpy as np
#from scipy.interpolate import Rbf 
import matplotlib.pyplot as plt
from matplotlib import cm
import os
from matplotlib import font_manager as fm, rcParams

##------------parameters settings-----------------##
map_sides = 1000
half_ms = 500

magnif = 1e-1

R0 = 200
circle_width = 10

ep0 = 1#vaccum dielectric constant
ep_max = 10*ep0
ep_min = 1*ep0
#maxium and minium of dielectric constant
frames = 10

E0 = 100

##------------matrix set-----------------##

eps = np.linspace(ep_min,ep_max,frames)#a series of dielectric constant
map_data = np.zeros(shape=map_sides,dtype='float')
fig_data = np.zeros(shape=(map_sides,map_sides,frames),dtype='float')
diagram_data = np.zeros(shape=(map_sides,map_sides),dtype='float')
dipolephi_data = np.zeros(shape=(map_sides,map_sides,frames),dtype='float')
R = np.zeros(shape=(map_sides,map_sides),dtype='float')
#R is polar diameter

##------------computing-----------------##

def symm(x):
	if x in range(half_ms):
		return 1
	elif x in range(half_ms,map_sides):
		return -1
	else:
		return 0

for i in range(map_sides):
	for j in range(map_sides):
		R[i,j] = np.sqrt((i-map_sides/2)**2+(j-map_sides/2)**2)
		map_data[j] = -1*E0*(j-map_sides/2)
		if  i in range(half_ms) and j in range(half_ms):
			dipolephi_data[i,j,:] = symm(j)*((eps[:]-ep0)/(eps[:]+2*ep0))*E0*(j-map_sides/2)*R0**3/R[i,j]**3
		elif i in range(half_ms,map_sides) and j in range(half_ms):
			dipolephi_data[i,j,:] = symm(j)*dipolephi_data[map_sides-i-1,j,:]
		elif i in range(half_ms) and j in range(half_ms,map_sides):
			dipolephi_data[i,j,:] = symm(j)*dipolephi_data[i,map_sides-j-1,:]	
		else:
			dipolephi_data[i,j,:] = symm(j)*dipolephi_data[map_sides-i-1,map_sides-j-1,:]



for i in range(map_sides):
	for j in range(map_sides):
			if R[i,j] < R0 - circle_width/2:
				fig_data[i,j,:] = map_data[j]*(3*ep0/(eps[:]+2*ep0))
			elif R[i,j] > R0 + circle_width/2 :
				fig_data[i,j,:] = map_data[j] + dipolephi_data[i,j,:]
			else:
				fig_data[i,j,:] = -1e6

fig_data = fig_data*magnif

##------------data writting & figures making-----------------##

fig, ax = plt.subplots()
fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")
prop = fm.FontProperties(fname=fpath)

for k in range(frames):
	#diagram_data[:,:] = fig_data[:,:,k]
	#np.savetxt('map_data.dat',diagram_data)
	plt.imshow(fig_data[:,:,k],cmap='YlGnBu',vmin=-5e3,vmax=5e3)
	plt.axis('off')
	ax.set_title(r'$\epsilon_r =%.2f$'%eps[k], fontproperties=prop,fontsize=20)
	plt.savefig('./figures/fig%d.png'%(k+1))

exit()