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
halfp = int(pixels/2)
perc_2 = 4*pi*eps*c**3
##------------matrix settings-----------------##
E = np.zeros(shape=(pixels,pixels),dtype='complex')#complex electric field intensity
B = np.zeros(shape=(pixels,pixels),dtype='complex')#complex magnetic field intensity
R = np.zeros(shape=(pixels,pixels),dtype='float')#radius or the distance from the map centre
L = np.zeros(pixels,dtype='float')#any axes of x or y
N = np.logspace(-0.9,-0.3,3)/l#contours label numbers

##---------------computing--------------------##

E_file = './E_map.dat'
E = np.loadtxt(E_file,dtype='complex')
E = np.transpose(E)
E = -1*E/l


##------------data writting & figures making-----------------##

fig= plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")

prop = fm.FontProperties(fname=fpath)
ax2.imshow(E.real,cmap='jet',vmin=-1/l,vmax=1/l)
ax2.axis('off')
# plt.colorbar()
a = plt.contour(abs(E.real),N,linewidths=1,cmap = 'rainbow')

plt.clabel(a,fontsize=5)
ax2.set_title('E field intensity and its contours', fontproperties=prop,fontsize=17)

ax1.imshow(E.real,cmap='YlGnBu',vmin=-1/l,vmax=1/l)
ax1.axis('off')
ax1.set_title('E field of a magnetic dipole radiation', fontproperties=prop,fontsize=17)

plt.show()
plt.savefig('dipole_B_radiation.png',dpi=600)
exit()