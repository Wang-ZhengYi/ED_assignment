#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Nov. 2019
	
	Electric Dynamic Chapter 5

	@author: ZYW @ BNU
	'''
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import font_manager as fm, rcParams

##------------parameters settings-----------------##

c = 1#speed of light
eps = 1#vaccum dielectirc number
pi = np.pi
l = 300#wave length
k = 2*pi/l#wave number
P_tt = 1000#acceleration of electic dipole
pixels = 1024#resolution of the map

##------------matrix settings-----------------##

E = np.zeros(shape=(pixels,pixels),dtype='complex')#complex electric field intensity
B = np.zeros(shape=(pixels,pixels),dtype='complex')#complex magnetic field intensity
R = np.zeros(shape=(pixels,pixels),dtype='float')#radius or the distance from the map centre
N = np.logspace(-0.9,-0.3,3)#contours label numbers

##---------------computing--------------------##
for i in range(pixels):
	for j in range(pixels):
		R[i,j] = np.sqrt((i-pixels/2)**2+(j-pixels/2)**2)
		E[i,j] = P_tt*(np.cos(k*R[i,j])+1.0j*np.sin(k*R[i,j]))*(j-pixels/2)/R[i,j]**2/4/pi


##------------data writting & figures making-----------------##
fig= plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")

prop = fm.FontProperties(fname=fpath)
ax2.imshow(E.real,cmap='afmhot',vmin=-1,vmax=1)
ax2.axis('off')
# plt.colorbar()
a = plt.contour(abs(E.real),N,linewidth=0.01,cmap = 'rainbow')

plt.clabel(a,fontsize=5)
ax2.set_title('E field and its contours', fontproperties=prop,fontsize=17)

ax1.imshow(E.real,cmap='YlGnBu',vmin=-1,vmax=1)
ax1.axis('off')
ax1.set_title('E field of a dipole radiation', fontproperties=prop,fontsize=17)

plt.show()
plt.savefig('dipole_radiation.png')
exit()