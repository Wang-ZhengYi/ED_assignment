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
l = 100#wave length
k = 2*pi/l#wave number
P_tt = 1000#acceleration of electic dipole
pixels = 1024#resolution of the map
halfp = int(pixels/2)
perc_2 = 4*pi*eps*c**3
##------------matrix settings-----------------##

E = np.zeros(shape=(pixels,pixels),dtype='complex')#complex electric field intensity
E_L = np.zeros(pixels,dtype='float')
B = np.zeros(shape=(pixels,pixels),dtype='complex')#complex magnetic field intensity
R = np.zeros(shape=(pixels,pixels),dtype='float')#radius or the distance from the map centre
L = np.zeros(pixels,dtype='float')#any axes of x or y
N = np.logspace(-0.9,-0.3,3)#contours label numbers

##---------------computing--------------------##

for i in range(halfp):
	for j in range(halfp):
		R[i,j] = abs((i-pixels/2)+(j-pixels/2)*1.0j)
		L[i] = i
ell = np.linspace(-1*halfp,halfp,pixels)
E[0:halfp,0:halfp] = P_tt*(np.exp(1.0j*k*R[0:halfp,0:halfp]))*(L[0:halfp]-halfp)/R[0:halfp,0:halfp]**2/perc_2
E[0:halfp,halfp:pixels] = -1*E[0:halfp,-1*halfp:-1*pixels:-1]
E[halfp:pixels,0:halfp] = E[-1*halfp-1:-1*pixels-1:-1,0:halfp]
E[halfp:pixels,halfp:pixels] = -1*E[-1*halfp-1:-1*pixels-1:-1,-1*halfp-1:-1*pixels-1:-1]
np.savetxt('E_map.dat',E)
E_L[:] = E[0,:].real

##------------data writting & figures making-----------------##

fig= plt.figure()
fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")

prop = fm.FontProperties(fname=fpath)


ax1 = plt.axes([0.05,0.52,0.4,0.4])
ax1.imshow(E.real,cmap='YlGnBu',vmin=-1,vmax=1)
ax1.axis('off')
ax1.set_title('E field of a dipole radiation', fontproperties=prop,fontsize=15)


ax2 = plt.axes([0.55,0.52,0.4,0.4])
ax2.imshow(E.real,cmap='afmhot',vmin=-1,vmax=1)
ax2.axis('off')
a = plt.contour(abs(E.real),N,linewidths=0.3,cmap = 'rainbow')
plt.clabel(a,fontsize=5)
ax2.set_title('E field and its contours', fontproperties=prop,fontsize=15)



ax3 = plt.axes([0.1,0.05,0.8,0.4])
ax3.plot(ell,E_L.real)
ax3.set_title('E field intensity in radiation direction', fontproperties=prop,fontsize=15)
ax3.grid(True)

# plt.show()

plt.savefig('dipole_radiation.png',dpi=600)
exit()